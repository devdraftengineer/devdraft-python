# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AggregatedBalance"]


class AggregatedBalance(BaseModel):
    balances: List[List[object]]
    """Detailed breakdown of balances by wallet and chain"""

    currency: Literal["usdc", "eurc"]
    """The stablecoin currency"""

    total_balance: str
    """The total aggregated balance across all wallets and chains"""
