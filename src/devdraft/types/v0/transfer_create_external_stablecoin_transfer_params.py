# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransferCreateExternalStablecoinTransferParams"]


class TransferCreateExternalStablecoinTransferParams(TypedDict, total=False):
    beneficiary_id: Required[Annotated[str, PropertyInfo(alias="beneficiaryId")]]
    """Beneficiary ID for the stablecoin transfer"""

    destination_currency: Required[Annotated[str, PropertyInfo(alias="destinationCurrency")]]
    """The destination currency"""

    source_currency: Required[Annotated[str, PropertyInfo(alias="sourceCurrency")]]
    """The source currency"""

    source_wallet_id: Required[Annotated[str, PropertyInfo(alias="sourceWalletId")]]
    """The ID of the source bridge wallet"""

    amount: float
    """The amount to transfer"""

    blockchain_memo: str
    """Blockchain memo for the transfer"""
