# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InvoiceCreateParams", "Item"]


class InvoiceCreateParams(TypedDict, total=False):
    currency: Required[Literal["usdc", "eurc"]]
    """Currency for the invoice"""

    customer_id: Required[str]
    """Customer ID"""

    delivery: Required[Literal["EMAIL", "MANUALLY"]]
    """Delivery method"""

    due_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Due date of the invoice"""

    email: Required[str]
    """Email address"""

    items: Required[Iterable[Item]]
    """Array of products in the invoice"""

    name: Required[str]
    """Name of the invoice"""

    partial_payment: Required[bool]
    """Allow partial payments"""

    payment_link: Required[bool]
    """Whether to generate a payment link"""

    payment_methods: Required[List[Literal["ACH", "BANK_TRANSFER", "CREDIT_CARD", "CASH", "MOBILE_MONEY", "CRYPTO"]]]
    """Array of accepted payment methods"""

    status: Required[Literal["DRAFT", "OPEN", "PASTDUE", "PAID", "PARTIALLYPAID"]]
    """Invoice status"""

    address: str
    """Address"""

    logo: str
    """Logo URL"""

    phone_number: str
    """Phone number"""

    send_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Send date"""

    tax_id: Annotated[str, PropertyInfo(alias="taxId")]
    """Tax ID"""


class Item(TypedDict, total=False):
    product_id: Required[str]
    """Product ID"""

    quantity: Required[float]
    """Quantity of the product"""
