from fastapi import FastAPI
from agents.planner import plan_task
from agents.executor import execute_plan
from agents.verifier import verify_and_finalize

app = FastAPI()

@app.get("/run")
async def run_assistant(query: str, debug: bool = False):
    print("--- Planning Phase ---")
    plan = plan_task(query)
    
    print("--- Execution Phase ---")
    results = execute_plan(plan)
    
    print("--- Verification Phase ---")
    final_output = verify_and_finalize(query, results)
    
    
    response = {
        "query": query,
        "status": final_output.get("status"),
        "answer": final_output.get("answer")
    }

    
    if debug:
        response["internal_details"] = {
            "plan": plan,
            "raw_results": results
        }
    
    return response