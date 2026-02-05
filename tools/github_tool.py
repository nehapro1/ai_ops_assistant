import requests

def search_github(query: str):
    
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "My-AI-Ops-Assistant" 
    }
    
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"
    
    try:
        response = requests.get(url, headers=headers)
        
        
        if response.status_code == 403:
            return "Error: GitHub API Rate limit exceeded. Try again in a few minutes."
            
        data = response.json()
        items = data.get("items", [])[:3]
        
        if not items:
            return f"No results found for '{query}'. Try a different keyword."

        results = []
        for i in items:
            results.append(f"{i['full_name']} (⭐{i['stargazers_count']}): {i['html_url']}")
        
        return "\n".join(results)
        
    except Exception as e:
        return f"GitHub API error: {str(e)}"