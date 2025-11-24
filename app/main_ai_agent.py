from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from .schemas import PlanRequest, PlanResponse, ExecuteRequest
from .planner import build_plan
from .executor import execute_steps

app = FastAPI(title="AI WEB AUTOMATION AGENT")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def read_root():
    # Serve the frontend HTML file
    index_path = os.path.join(static_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "AI Web Automation Agent running"}

# 1) LLM planner
@app.post("/plan", response_model=PlanResponse)
def create_plan(req: PlanRequest):
    try:
        plan = build_plan(req)
        return plan
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate plan: {str(e)}")

# 2) Multi-step executor
@app.post("/execute")
def execute_plan(req: ExecuteRequest):
    execute_steps(req.steps)
    return {"status": "ok", "message": "Execution finished on server"}
