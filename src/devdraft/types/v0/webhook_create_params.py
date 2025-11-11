# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    encrypted: Required[bool]
    """Whether webhook payloads should be encrypted"""

    is_active: Required[Annotated[bool, PropertyInfo(alias="isActive")]]
    """Whether the webhook is active and will receive events"""

    name: Required[str]
    """Name of the webhook for identification purposes"""

    url: Required[str]
    """URL where webhook events will be sent"""

    signing_secret: str
    """Secret key used to sign webhook payloads for verification"""
