# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["LiquidationAddressResponse"]


class LiquidationAddressResponse(BaseModel):
    id: str
    """Unique identifier for the liquidation address"""

    address: str
    """Liquidation address"""

    chain: str
    """Blockchain chain"""

    created_at: str
    """Creation timestamp"""

    currency: str
    """Currency"""

    customer_id: str
    """Customer ID this liquidation address belongs to"""

    state: str
    """Current state of the liquidation address"""

    updated_at: str
    """Last update timestamp"""

    bridge_wallet_id: Optional[str] = None
    """Bridge wallet ID"""

    custom_developer_fee_percent: Optional[str] = None
    """Custom developer fee percent"""

    destination_currency: Optional[str] = None
    """Destination currency"""

    destination_payment_rail: Optional[str] = None
    """Destination payment rail"""

    external_account_id: Optional[str] = None
    """External account ID"""

    prefunded_account_id: Optional[str] = None
    """Prefunded account ID"""
