# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    encrypted: bool
    """Whether webhook payloads should be encrypted"""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Whether the webhook is active and will receive events"""

    name: str
    """Name of the webhook for identification purposes"""

    signing_secret: str
    """Secret key used to sign webhook payloads for verification"""

    url: str
    """URL where webhook events will be sent"""
