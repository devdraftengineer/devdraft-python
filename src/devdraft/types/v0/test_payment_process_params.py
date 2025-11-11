# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TestPaymentProcessParams"]


class TestPaymentProcessParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to charge"""

    currency: Required[str]
    """The currency code"""

    description: Required[str]
    """Description of the payment"""

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """Customer reference ID"""
