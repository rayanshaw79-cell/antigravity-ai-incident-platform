🚀 Antigravity AI Incident Platform

Antigravity AI Incident Platform is a backend system designed to detect, classify, and respond to AI model failures in a structured and operationally realistic way.

The platform demonstrates how AI behavior can be treated as observable system output, not just logs — enabling incident tracking, alerting, and collaboration across engineering and research teams.

🧠 What Problem This Solves

As AI systems grow more complex, failures such as hallucinations, policy violations, or unexpected outputs become operational incidents, not just model quirks.

This project shows how to:

- Test AI behavior programmatically
- Capture failures as structured incidents
- Classify severity
- Trigger real response workflows (Slack alerts)
- Design for extensibility (DBs, GraphQL, analytics)

🏗️ System Architecture

Core components:

1. FastAPI — REST API and orchestration layer
2. Antigravity (AI Testing Layer) — Executes AI tests and detects issues
3. Incident Service — Creates and manages incident records
4. Slack Notifications — Alerts teams for high-severity incidents
5. Config & Logging Layer — Environment-aware and production-ready

See docs/architecture.md and diagrams/architecture.png for full system design.

🔄 Incident Lifecycle

1. An API client submits an incident request
2. Antigravity executes an AI test run
3. Model output is analyzed for issues
4. An incident record is created
5. High-severity incidents trigger Slack alerts
6. The system returns a structured response
7. This mirrors real internal AI reliability workflows.

📡 API Overview
Health Check
GET /health

Create Incident
POST /api/v1/incidents

Example request:

{
  "title": "Model hallucinated compliance policy",
  "description": "The model cited a non-existent policy.",
  "severity": "high",
  "model_name": "gpt-4.1",
  "prompt_version": "v1.2.0"
}

Behavior:

- Validates input
- Runs Antigravity AI test
- Creates incident
- Sends Slack alert if severity is high/critical

⚠️ Slack Alerts

- High-severity incidents automatically notify teams via Slack using incoming webhooks.
- Alerts are severity-gated
- Integration is async and non-blocking
- Slack configuration is environment-based (.env)

🛠️ Tech Stack

- Python 3.12+
- FastAPI
- Pydantic v2
- Uvicorn
- HTTPX
- Async-first architecture

🔮 What I’d Build Next in Production

- Persistent storage (PostgreSQL + Alembic)
- Incident timelines & analytics
- GraphQL read APIs for incident exploration
- Role-based access control
- Real LLM evaluation harness integration
- PagerDuty / OpsGenie escalation

👤 Author Notes

This project was built to demonstrate system thinking around AI reliability, not just API development.

It focuses on:

- Clean architecture
- Operational realism
- Extensibility
- Clear engineering intent