from app.services.antigravity.client import AntigravityClient
from fastapi import APIRouter, status
from datetime import datetime
import uuid

from app.models.incidents import IncidentCreate, IncidentResponse

router = APIRouter(prefix="/incidents", tags=["incidents"])


@router.post(
    "",
    response_model=IncidentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_incident(payload: IncidentCreate):
    """
    Create a new AI incident record.

    This endpoint simulates incident creation and will later
    be backed by persistent storage.
    """
    client = AntigravityClient()

    test_result = await client.run_test(
    model_name=payload.model_name,
    prompt=payload.description or payload.title,
    prompt_version=payload.prompt_version,
)

    return IncidentResponse(
    id=test_result["run_id"],
    title=payload.title,
    severity=payload.severity,
    model_name=payload.model_name,
    created_at=test_result["executed_at"],
)

