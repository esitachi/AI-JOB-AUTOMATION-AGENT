from typing import Dict, Any
from playwright.sync_api import sync_playwright
from .config import JOB_EMAIL, JOB_NAME

class JobBrowser:
    def __init__(self, headless: bool = True):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=headless)
        self.page = self.browser.new_page()

    def close(self):
        self.browser.close()
        self.p.stop()

    def open_site(self, url: str):
        self.page.goto(url, wait_until="load")

    def search_jobs(self, keywords: str, location: str):
        # These selectors are EXAMPLES. You must customize per site.
        try:
            self.page.fill("input[name='q']", keywords)
            self.page.fill("input[name='l']", location)
            self.page.click("button[type='submit']")
            self.page.wait_for_timeout(3000)
        except Exception as e:
            print("search_jobs error:", e)

    def open_job(self, job_index: int = 0):
        # Example selector: adjust based on target site
        jobs = self.page.query_selector_all("a.jobtitle, a[data-job-id]")
        if jobs and job_index < len(jobs):
            jobs[job_index].click()
            self.page.wait_for_timeout(3000)

    def fill_form(self):
        # Very generic example – customize to your sites
        try:
            if JOB_NAME:
                self.page.fill("input[name*='name']", JOB_NAME)
            if JOB_EMAIL:
                self.page.fill("input[name*='email']", JOB_EMAIL)

            # Example for upload: change selector & file path
            # self.page.set_input_files("input[type='file']", "resume.pdf")

            # Try clicking any button that looks like Apply/Submit
            for text in ["Apply", "Submit", "Next"]:
                btn = self.page.query_selector(f"text={text}")
                if btn:
                    btn.click()
                    self.page.wait_for_timeout(2000)
                    break
        except Exception as e:
            print("fill_form error:", e)

    def run_step(self, action: str, params: Dict[str, Any]):
        if action == "open_site":
            self.open_site(params["url"])
        elif action == "search_jobs":
            self.search_jobs(params["keywords"], params["location"])
        elif action == "open_job":
            self.open_job(params.get("job_index", 0))
        elif action == "fill_form":
            self.fill_form()
