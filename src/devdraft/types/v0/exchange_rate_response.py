# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExchangeRateResponse"]


class ExchangeRateResponse(BaseModel):
    buy_rate: str
    """
    Rate for buying target currency (what you get when converting from source to
    target)
    """

    from_: str = FieldInfo(alias="from")
    """Source currency code (USD for USDC)"""

    midmarket_rate: str
    """Mid-market exchange rate from source to target currency"""

    sell_rate: str
    """
    Rate for selling target currency (what you pay when converting from target to
    source)
    """

    to: str
    """Target currency code (EUR for EURC)"""

    timestamp: Optional[str] = None
    """Timestamp when the exchange rate was last updated"""
