from typing import List
from .schemas import Step
from .browser import JobBrowser

def execute_steps(steps: List[Step]):
    browser = JobBrowser(headless=False)  # set True to hide window
    try:
        for step in steps:
            print(f"Executing step {step.id}: {step.action}")
            browser.run_step(step.action, step.params)
    finally:
        browser.close()
