from pydantic import BaseModel
from typing import List, Dict, Any

class PlanRequest(BaseModel):
    job_title: str
    location: str
    target_sites: List[str]  # e.g. ["indeed.com", "naukri.com"]

class Step(BaseModel):
    id: int
    action: str
    params: Dict[str, Any]

class PlanResponse(BaseModel):
    steps: List[Step]

class ExecuteRequest(BaseModel):
    steps: List[Step]
