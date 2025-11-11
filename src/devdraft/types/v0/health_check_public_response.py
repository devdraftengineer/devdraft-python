# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HealthCheckPublicResponse"]


class HealthCheckPublicResponse(BaseModel):
    status: Literal["ok", "error"]
    """Basic health status of the service.

    Returns "ok" when the service is responding.
    """

    timestamp: datetime
    """ISO 8601 timestamp when the health check was performed."""

    version: str
    """Current version of the API service."""
