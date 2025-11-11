# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TransferCreateDirectWalletParams"]


class TransferCreateDirectWalletParams(TypedDict, total=False):
    amount: Required[float]
    """The amount to transfer"""

    network: Required[str]
    """The network to use for the transfer"""

    stable_coin_currency: Required[Annotated[str, PropertyInfo(alias="stableCoinCurrency")]]
    """The stablecoin currency to use"""

    wallet_id: Required[Annotated[str, PropertyInfo(alias="walletId")]]
    """The ID of the bridge wallet to transfer from"""
