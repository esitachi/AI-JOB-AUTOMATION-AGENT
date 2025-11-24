from typing import List
import json
from openai import OpenAI
from .schemas import PlanRequest, Step, PlanResponse
from .config import OPENAI_API_KEY, OPENAI_MODEL

SYSTEM_PROMPT = """
You are an AI assistant that creates step-by-step browser automation plans
for applying to jobs.

You must output JSON with a list of steps. Each step has:
- id: integer
- action: one of ["open_site", "search_jobs", "open_job", "fill_form"]
- params: dictionary for that action.

Do NOT include anything except valid JSON.
"""

def build_plan_fallback(req: PlanRequest) -> PlanResponse:
    """Fallback plan when OpenAI is not available"""
    # Get first target site or default to indeed.com
    first_site = req.target_sites[0] if req.target_sites else "indeed.com"
    if not first_site.startswith("http"):
        first_site = f"https://{first_site}"
    
    steps = [
        Step(id=1, action="open_site", params={"url": first_site}),
        Step(id=2, action="search_jobs", params={"keywords": req.job_title, "location": req.location}),
        Step(id=3, action="open_job", params={"job_index": 0}),
        Step(id=4, action="fill_form", params={}),
    ]
    return PlanResponse(steps=steps)

def build_plan(req: PlanRequest) -> PlanResponse:
    # Check if API key is configured
    if not OPENAI_API_KEY:
        print("Warning: OPENAI_API_KEY not set. Using fallback plan.")
        return build_plan_fallback(req)
    
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        user_prompt = f"""
Create a browser automation plan to apply for '{req.job_title}' jobs in '{req.location}'.
Target job sites: {", ".join(req.target_sites)}.

Use these step types only:
- open_site: params={{"url": "..."}}
- search_jobs: params={{"keywords": "...", "location": "..."}}
- open_job: params={{"job_index": 0}}
- fill_form: params={{"upload_resume": true, "fill_name": true, "fill_email": true}}

Return 4–8 steps.
"""

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
        )

        data = response.choices[0].message.content
        obj = json.loads(data)

        steps = [Step(**step) for step in obj["steps"]]
        return PlanResponse(steps=steps)
    
    except Exception as e:
        print(f"Error calling OpenAI: {e}. Using fallback plan.")
        return build_plan_fallback(req)
