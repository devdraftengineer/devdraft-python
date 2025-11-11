# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WebhookResponse"]


class WebhookResponse(BaseModel):
    id: str
    """Unique identifier for the webhook"""

    created_at: str
    """Timestamp when the webhook was created"""

    delivery_stats: object
    """Webhook delivery statistics"""

    encrypted: bool
    """Whether webhook payloads are encrypted"""

    is_active: bool = FieldInfo(alias="isActive")
    """Whether the webhook is currently active"""

    name: str
    """Name of the webhook"""

    updated_at: str
    """Timestamp when the webhook was last updated"""

    url: str
    """URL where webhook events are sent"""
