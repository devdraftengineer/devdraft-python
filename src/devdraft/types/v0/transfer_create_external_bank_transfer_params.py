# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransferCreateExternalBankTransferParams"]


class TransferCreateExternalBankTransferParams(TypedDict, total=False):
    destination_currency: Required[Annotated[str, PropertyInfo(alias="destinationCurrency")]]
    """The destination currency"""

    destination_payment_rail: Required[
        Annotated[
            Literal["ach", "ach_push", "ach_same_day", "wire", "sepa", "swift", "spei"],
            PropertyInfo(alias="destinationPaymentRail"),
        ]
    ]
    """The destination payment rail (fiat payment method)"""

    external_account_id: Required[str]
    """The external account ID for the bank transfer"""

    source_currency: Required[Annotated[str, PropertyInfo(alias="sourceCurrency")]]
    """The source currency"""

    source_wallet_id: Required[Annotated[str, PropertyInfo(alias="sourceWalletId")]]
    """The ID of the source bridge wallet"""

    ach_reference: str
    """ACH reference message (1-10 characters, only for ACH transfers)"""

    amount: float
    """The amount to transfer"""

    sepa_reference: str
    """SEPA reference message (6-140 characters, only for SEPA transfers)"""

    spei_reference: str
    """SPEI reference message (1-40 characters, only for SPEI transfers)"""

    swift_charges: str
    """SWIFT charges bearer (only for SWIFT transfers)"""

    swift_reference: str
    """SWIFT reference message (1-190 characters, only for SWIFT transfers)"""

    wire_message: str
    """Wire transfer message (1-256 characters, only for wire transfers)"""
