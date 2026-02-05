🤖 AI Ops Assistant

A multi-agent system designed to handle operational tasks such as weather checks and GitHub repository searches.
Built using FastAPI, Groq (Llama 3.3), and integrated third-party APIs.

🏗️ Architecture Overview

The system follows a Multi-Agent Orchestration pattern to ensure:

Modularity

Scalability

Reliability

🧠 Planner Agent

Receives the user query

Uses an LLM to break the query into tool-specific steps

Outputs a structured JSON plan

⚙️ Executor Agent

Acts as a deterministic controller

Maps tool names to Python functions

Executes real-world API calls

✅ Verifier Agent

Validates raw outputs

Ensures the final response:

Matches the original user query

Is complete and accurate

🛠️ Integrated APIs
🌦️ Open-Meteo API

Provides real-time weather data

🧑‍💻 GitHub Search API

Fetches top repositories based on:

⭐ Star count

🔍 Keyword relevance

🚀 Local Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-url>
cd ai_ops_assistant

2️⃣ Create a Virtual Environment
python -m venv venv


Activate it:

Mac / Linux

source venv/bin/activate


Windows

venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Environment Variables

Create a .env file in the root directory (refer to .env.example):

GROQ_API_KEY=your_actual_groq_api_key

5️⃣ Run the Server
uvicorn main:app --reload

🧪 Example Prompts
🌦️ Weather

"What is the weather in London?"

"How is the weather in New York?"

🧑‍💻 GitHub Search

"Find top Python repositories for Machine Learning on GitHub"

"Find me a GitHub repo for FastAPI"

🔀 Combined Query

"How is the weather in New York and find me a GitHub repo for FastAPI?"

🔍 Usage & Debugging

By default, the API returns a clean, human-readable response suitable for production.

✅ Clean Answer
http://127.0.0.1:8000/run?query=How is the weather in London?

🛠️ Debug Mode (Agent Logs)

To inspect:

Planner steps

Executor API responses

Append debug=true:

http://127.0.0.1:8000/run?query=How is the weather in London?&debug=true

⚠️ Known Limitations & Tradeoffs
⏱️ GitHub API Rate Limits

Uses unauthenticated access

Limited to 60 requests/hour per IP

🔁 Sequential Execution

Agent steps run one-by-one

Parallel execution could reduce latency for complex queries

🧠 Context Window Constraints

Extremely long queries with many subtasks may hit LLM token limits during planning
