# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .aggregated_balance import AggregatedBalance

__all__ = ["BalanceGetAllStablecoinBalancesResponse"]


class BalanceGetAllStablecoinBalancesResponse(BaseModel):
    eurc: AggregatedBalance
    """EURC balance aggregation"""

    total_usd_value: str
    """Total value in USD equivalent"""

    usdc: AggregatedBalance
    """USDC balance aggregation"""
