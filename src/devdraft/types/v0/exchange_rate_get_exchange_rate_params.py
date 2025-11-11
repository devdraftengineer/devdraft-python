# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExchangeRateGetExchangeRateParams"]


class ExchangeRateGetExchangeRateParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Source currency code (e.g., usd)"""

    to: Required[str]
    """Target currency code (e.g., eur)"""
