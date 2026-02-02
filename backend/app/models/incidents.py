from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class IncidentCreate(BaseModel):
    title: str = Field(..., example="Model hallucinated policy reference")
    description: Optional[str] = Field(
        None, example="The model cited a non-existent policy section."
    )
    severity: str = Field(..., example="high")
    model_name: str = Field(..., example="gpt-4.1")
    prompt_version: Optional[str] = Field(None, example="v1.2.0")


class IncidentResponse(BaseModel):
    id: str
    title: str
    severity: str
    model_name: str
    created_at: datetime
