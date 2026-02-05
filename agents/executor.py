from tools.weather_tool import get_weather
from tools.github_tool import search_github


TOOL_MAP = {
    "get_weather": get_weather,
    "search_github": search_github
}

def execute_plan(plan):
    results = []
    for step in plan.get("steps", []):
        tool_name = step.get("tool")
        args = step.get("args", {})
        
        print(f"Agent Executor: Running {tool_name}...")
        
        
        tool_func = TOOL_MAP.get(tool_name)
        
        if tool_func:
            try:
                
                output = tool_func(**args)
            except Exception as e:
                output = f"Error executing {tool_name}: {str(e)}"
        else:
            output = f"Error: Tool {tool_name} unknown."
            
        results.append({"step": step["step"], "output": output})
            
    return results