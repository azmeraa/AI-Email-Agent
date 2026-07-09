# AI-Email-Agent

A privacy-focused, local-first AI email agent built with LangChain and Ollama. Features intelligent drafting, secure local inference, and a human-in-the-loop (HITL) approval gate for reliable automation.

## Features
- **Local LLM Engine:** Powered by Ollama (llama3.1) for complete data privacy.
- **HITL Security:** Explicit approval gate before any email is sent.
- **Modular Design:** Built for easy integration with databases and external APIs.

## Setup
1. Install [Ollama](https://ollama.com/) and run `ollama pull llama3.1`.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the agent: `python core/agent.py`