# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WebhookListParams"]


class WebhookListParams(TypedDict, total=False):
    skip: float
    """Number of records to skip (default: 0)"""

    take: float
    """Number of records to return (default: 10)"""
