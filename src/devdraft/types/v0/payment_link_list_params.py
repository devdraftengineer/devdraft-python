# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PaymentLinkListParams"]


class PaymentLinkListParams(TypedDict, total=False):
    skip: str
    """Number of records to skip (must be non-negative)"""

    take: str
    """Number of records to take (must be positive)"""
