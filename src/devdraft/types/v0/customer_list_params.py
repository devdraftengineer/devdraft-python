# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .customer_status import CustomerStatus

__all__ = ["CustomerListParams"]


class CustomerListParams(TypedDict, total=False):
    email: str
    """Filter customers by email (exact match, case-insensitive)"""

    name: str
    """Filter customers by name (partial match, case-insensitive)"""

    skip: float
    """Number of records to skip for pagination"""

    status: CustomerStatus
    """Filter customers by status"""

    take: float
    """Number of records to return (max 100)"""
