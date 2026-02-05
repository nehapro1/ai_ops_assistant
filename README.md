# AI Ops Assistant 🤖

A multi-agent system designed to handle operational tasks including weather checks and GitHub repository searches. Built with FastAPI, Groq (Llama 3.3), and integrated third-party APIs.

## 🏗️ Architecture Explanation
The system follows a **Multi-Agent Orchestration** pattern:
* **Planner Agent:** Receives the user query and breaks it down into a sequence of tool-specific steps (JSON output).
* **Executor Agent:** Dynamically maps tool names to Python functions and executes API calls (GitHub & Open-Meteo).
* **Verifier Agent:** Reviews the raw outputs to ensure they satisfy the user's original intent before providing a final answer.

## 🛠️ Integrated APIs
1.  **Open-Meteo API:** Used for real-time weather data (requires geocoding for coordinates).
2.  **GitHub Search API:** Used to find top-rated repositories based on stars and relevance.

## 🚀 Local Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone <your-repo-url>
   cd ai_ops_assistant

2. Create a Virtual Environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:

Bash
pip install -r requirements.txt

4. Environment Variables: Create a .env file in the root directory based on .env.example:

Plaintext
GROQ_API_KEY=your_actual_groq_api_key
5. Run the Server:

Bash
uvicorn main:app --reload


🧪 Example Prompts
"What is the weather in London?"

"Find me top Python repositories for Machine Learning on GitHub."

"How is the weather in New York and find me a GitHub repo for 'fastapi'?"


Known Limitations / Tradeoffs
Rate Limits: The GitHub API is used without a token, which has a strict limit of 60 requests/hour per IP.

Sequential Execution: Steps are executed one by one; for complex tasks, parallel execution could be implemented to save time.