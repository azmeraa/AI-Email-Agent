AI Email Task Automation Agent
An intelligent, local-first automation agent designed to synchronize, categorize, and extract actionable tasks from email communications. This project utilizes LLM-driven semantic analysis and robust local database management to bridge the gap between communication and execution.

1. System Architecture & Pipeline
The system operates on a modular, decoupled pipeline. Each stage is an independent script, which allows for granular testing and debugging.

Ingestion Layer (read_inbox.py): Connects to the mail server and performs an idempotent write to the emails table.

Intelligence Layer (categorize_emails.py): Communicates with the local Ollama API. It performs zero-shot classification, transforming unstructured text into structured categorical data.

Extraction Layer (extract_tasks.py): Performs deep-text analysis to identify action items, assigning both priority and due dates using JSON-formatted responses.

Presentation Layer (daily_brief.py): An analytics script that performs aggregate queries (GROUP BY) to provide a workload summary.

2. Database Schema & ERD
The system utilizes a relational schema to maintain data integrity.

emails table: The source of truth for raw communication.

tasks table: A normalized table linked via email_id (Foreign Key). This allows one email to potentially spawn multiple tasks if needed.

3. Best Practices for Junior Developers
Idempotency: Always use CREATE TABLE IF NOT EXISTS and check for existing records before inserting (e.g., in extract_tasks.py) to prevent duplicate data.

Environment Variables: While this project uses hardcoded paths for simplicity, in a production environment, use a .env file to manage database paths and API endpoints.

Error Handling: Notice the use of try-except blocks around network calls. Always anticipate LLM latency or service downtime when building AI-integrated tools.

Local-First Philosophy: By keeping all processing on the local machine (Ollama + SQLite), we eliminate latency issues associated with remote cloud LLMs and maintain 100% data privacy.

4. Maintenance & Troubleshooting
Database Locked? If the database is locked, ensure no other terminal session is holding an open transaction on email_agent.db.

LLM Timeout: If the AI categorization is slow, ensure your hardware resources (RAM/GPU) are sufficient for the llama3 model.

Modifying Priorities: To update task priority, use the SQLite CLI:

SQL
UPDATE tasks SET priority = 'High' WHERE id = [TASK_ID];
5. Deployment Roadmap
Clone the Repo: git clone https://github.com/azmeraa/AI-Email-Agent.git

Dependencies: Ensure requests and sqlite3 are installed.

Automate: Add brief.bat to your Windows Startup folder to receive your report automatically upon login.

How this helps junior experts:
Architectural Awareness: It explains why we decouple the scripts (modular design).

Database Integrity: It teaches the importance of Foreign Keys and Idempotency.

Operational Maturity: It adds a "Troubleshooting" section, which is exactly what a senior-level engineer would want a junior to have on hand.