# AI Ops Assistant 🤖

A multi-agent system designed to handle operational tasks including weather checks and GitHub repository searches. Built with FastAPI, Groq (Llama 3.3), and integrated third-party APIs.

## 🏗️ Architecture Explanation
The system follows a **Multi-Agent Orchestration** pattern to ensure modularity and reliability:
* **Planner Agent:** Receives the user query and uses an LLM to break it down into a sequence of tool-specific steps (JSON output).
* **Executor Agent:** A deterministic controller that dynamically maps tool names to Python functions and executes real-world API calls.
* **Verifier Agent:** Reviews the raw outputs against the original query to ensure the final answer is accurate and complete.

## 🛠️ Integrated APIs
1. **Open-Meteo API:** Used for real-time weather data.
2. **GitHub Search API:** Used to find top-rated repositories based on stars and relevance.

## 🚀 Local Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone <your-repo-url>
   cd ai_ops_assistant
Create a Virtual Environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

Bash
pip install -r requirements.txt
Environment Variables: Create a .env file in the root directory based on .env.example:

Plaintext
GROQ_API_KEY=your_actual_groq_api_key
Run the Server:

Bash
uvicorn main:app --reload
🧪 Example Prompts
"What is the weather in London?"

"Find me top Python repositories for Machine Learning on GitHub."

"How is the weather in New York and find me a GitHub repo for 'fastapi'?"

🔍 Usage & Debugging
The API returns a clean, human-readable answer by default to provide a production-ready experience.

To inspect the internal multi-agent coordination (Planner's steps and Executor's raw data), append the debug=true parameter to your request:

Clean Answer: http://127.0.0.1:8000/run?query=How is the weather in London?

Agent Logs: http://127.0.0.1:8000/run?query=How is the weather in London?&debug=true

⚠️ Known Limitations / Tradeoffs
Rate Limits: The GitHub API is used without a token, which has a strict limit of 60 requests/hour per IP.

Sequential Execution: Steps are currently executed one by one; for complex tasks, parallel execution could be implemented to reduce latency.

Context Window: Extremely long queries with many sub-tasks may hit LLM token limits during the planning phase.