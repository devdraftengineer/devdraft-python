# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HealthCheckResponse"]


class HealthCheckResponse(BaseModel):
    authenticated: bool
    """Indicates whether the request was properly authenticated.

    Always true for this endpoint since authentication is required.
    """

    database: Literal["connected", "error"]
    """Database connectivity status.

    Shows "connected" when database is accessible, "error" when connection fails.
    """

    message: str
    """Human-readable message describing the current health status and any issues."""

    status: Literal["ok", "error"]
    """Overall health status of the service.

    Returns "ok" when healthy, "error" when issues detected.
    """

    timestamp: datetime
    """ISO 8601 timestamp when the health check was performed."""

    version: str
    """Current version of the API service.

    Useful for debugging and compatibility checks.
    """
