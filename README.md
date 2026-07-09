\# ?? AI Email Task Automation Agent



An intelligent, local-first automation agent designed to synchronize, categorize, and extract actionable tasks from email communications. This project bridges the gap between raw communication and actionable execution using local AI.



\---



\## ??? 1. System Architecture \& Pipeline



The system operates on a modular, decoupled pipeline. Each stage is an independent script, which allows for granular testing, debugging, and replacement without affecting the entire system.







\* \*\*Ingestion Layer (`read\_inbox.py`):\*\* Connects to the mail server via IMAP, fetches raw message data, and performs an idempotent write to the `emails` table.



\* \*\*Intelligence Layer (`categorize\_emails.py`):\*\* Communicates with the local Ollama API (llama3). It performs zero-shot classification, transforming unstructured text into structured categorical metadata.



\* \*\*Extraction Layer (`extract\_tasks.py`):\*\* Performs deep-text analysis to identify specific action items, assigning priorities and due dates by parsing JSON-formatted LLM responses.



\* \*\*Presentation Layer (`daily\_brief.py`):\*\* An analytics script that performs aggregate queries (GROUP BY) to provide a prioritized workload summary and status updates.



\---



\## ?? 2. Database Schema \& ERD



The system utilizes a relational schema to ensure high data integrity and efficient querying.







\* \*\*`emails` table:\*\* Acts as the primary source of truth. It stores metadata, subject lines, body content, and the AI-generated category.



\* \*\*`tasks` table:\*\* A normalized table linked via an `email\_id` (Foreign Key). This allows for a one-to-many relationship, where a single complex email can spawn multiple distinct task items.



\---



\## ?? 3. Best Practices for Junior Developers



Adhering to these principles ensures the codebase remains clean, professional, and scalable.



\* \*\*Idempotency:\*\* Always use `CREATE TABLE IF NOT EXISTS` and verify the existence of records before insertion. This prevents duplicate data during re-runs.



\* \*\*Environment Management:\*\* While this project uses hardcoded paths, junior developers should migrate to `.env` files to manage database paths and API endpoints, promoting clean code configuration.



\* \*\*Resilient Error Handling:\*\* Note the use of `try-except` blocks around network-dependent calls. Always anticipate LLM latency or IMAP service downtime.



\* \*\*Local-First Philosophy:\*\* By keeping all processing on the local machine (Ollama + SQLite), we eliminate third-party cloud costs and maintain 100% data privacy.



\---



\## ?? 4. Maintenance \& Troubleshooting



Technical issues can occur in local AI pipelines. Use this reference guide to resolve common bottlenecks.



| Issue | Potential Cause | Troubleshooting Steps |

| :--- | :--- | :--- |

| \*\*Database Locked\*\* | Concurrent access | Ensure no other terminal/browser has an open transaction. |

| \*\*LLM Latency\*\* | Hardware constraints | Ensure RAM/GPU is not saturated; monitor Ollama process. |

| \*\*Task Priority\*\* | Logic error | Modify directly via SQLite: `UPDATE tasks SET priority = 'High' WHERE id = \[ID];` |



\---



\## ?? 5. Deployment Roadmap



1\. \*\*Clone:\*\* `git clone https://github.com/azmeraa/AI-Email-Agent.git`



2\. \*\*Dependencies:\*\* Ensure Python `requests` and `sqlite3` libraries are installed.



3\. \*\*Local AI:\*\* Ensure `Ollama` is active and the `llama3` model is pulled locally.



4\. \*\*Automation:\*\* For daily productivity, move `brief.bat` to your Windows Startup folder to generate your report automatically upon system login.



\---



\## ?? Why This Structure Matters



\* \*\*Architectural Awareness:\*\* Decoupled scripts teach developers the importance of modularity in enterprise applications.



\* \*\*Data Integrity:\*\* Managing Foreign Keys and Idempotency is foundational for any Database Administrator (DBA) career.



\* \*\*Operational Maturity:\*\* Building a "Troubleshooting" section develops the mindset of a senior-level engineer.

