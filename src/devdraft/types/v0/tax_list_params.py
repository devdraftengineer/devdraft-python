# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TaxListParams"]


class TaxListParams(TypedDict, total=False):
    active: bool
    """Filter by active status"""

    name: str
    """Filter taxes by name (partial match, case-insensitive)"""

    skip: float
    """Number of records to skip for pagination"""

    take: float
    """Number of records to return (max 100)"""
