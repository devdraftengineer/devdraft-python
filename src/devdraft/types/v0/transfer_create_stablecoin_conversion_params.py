# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransferCreateStablecoinConversionParams"]


class TransferCreateStablecoinConversionParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to convert"""

    destination_currency: Required[Annotated[str, PropertyInfo(alias="destinationCurrency")]]
    """The destination currency"""

    source_currency: Required[Annotated[str, PropertyInfo(alias="sourceCurrency")]]
    """The source currency"""

    source_network: Required[Annotated[str, PropertyInfo(alias="sourceNetwork")]]
    """The source network"""

    wallet_id: Required[Annotated[str, PropertyInfo(alias="walletId")]]
    """The ID of the bridge wallet to use"""
