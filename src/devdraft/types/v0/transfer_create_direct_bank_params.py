# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransferCreateDirectBankParams"]


class TransferCreateDirectBankParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to transfer"""

    destination_currency: Required[Annotated[str, PropertyInfo(alias="destinationCurrency")]]
    """The destination currency"""

    payment_rail: Required[Annotated[str, PropertyInfo(alias="paymentRail")]]
    """The payment rail to use"""

    source_currency: Required[Annotated[str, PropertyInfo(alias="sourceCurrency")]]
    """The source currency"""

    wallet_id: Required[Annotated[str, PropertyInfo(alias="walletId")]]
    """The ID of the bridge wallet to transfer from"""

    ach_reference: str
    """ACH transfer reference"""

    sepa_reference: str
    """SEPA transfer reference"""

    wire_message: str
    """Wire transfer message"""
