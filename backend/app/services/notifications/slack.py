import httpx
from app.core.config import settings


class SlackNotifier:
    """
    Sends incident alerts to Slack using Incoming Webhooks.
    """

    async def send_incident_alert(
        self,
        *,
        incident_id: str,
        title: str,
        severity: str,
        model_name: str,
    ) -> None:
        if not settings.slack_webhook_url:
            return  # Slack not configured (safe no-op)

        message = {
            "text": f":rotating_light: *AI Incident Detected*",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": (
                            f"*Severity:* `{severity}`\n"
                            f"*Model:* `{model_name}`\n"
                            f"*Title:* {title}\n"
                            f"*Incident ID:* `{incident_id}`"
                        ),
                    },
                }
            ],
        }

        async with httpx.AsyncClient(timeout=5) as client:
            await client.post(settings.slack_webhook_url, json=message)
