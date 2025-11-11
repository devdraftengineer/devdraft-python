# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InvoiceListParams"]


class InvoiceListParams(TypedDict, total=False):
    skip: float
    """Number of records to skip"""

    take: float
    """Number of records to take"""
