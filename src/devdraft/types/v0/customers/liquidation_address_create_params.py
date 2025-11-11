# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..bridge_payment_rail import BridgePaymentRail

__all__ = ["LiquidationAddressCreateParams"]


class LiquidationAddressCreateParams(TypedDict, total=False):
    address: Required[str]
    """The liquidation address on the blockchain"""

    chain: Required[
        Literal["ethereum", "solana", "polygon", "avalanche_c_chain", "base", "arbitrum", "optimism", "stellar", "tron"]
    ]
    """The blockchain chain for the liquidation address"""

    currency: Required[Literal["usdc", "eurc", "dai", "pyusd", "usdt"]]
    """The currency for the liquidation address"""

    bridge_wallet_id: str
    """Bridge Wallet to send funds to"""

    custom_developer_fee_percent: str
    """Custom developer fee percentage (Base 100 percentage: 10.2% = "10.2")"""

    destination_ach_reference: str
    """Reference for ACH transactions"""

    destination_address: str
    """Crypto wallet address for crypto transfers"""

    destination_blockchain_memo: str
    """Memo for blockchain transactions"""

    destination_currency: Literal["usd", "eur", "mxn", "usdc", "eurc", "dai", "pyusd", "usdt"]
    """Currency for sending funds"""

    destination_payment_rail: BridgePaymentRail
    """The blockchain network where the source currency resides.

    Determines gas fees and transaction speed.
    """

    destination_sepa_reference: str
    """Reference for SEPA transactions"""

    destination_wire_message: str
    """Message for wire transfers"""

    external_account_id: str
    """External bank account to send funds to"""

    prefunded_account_id: str
    """Developer's prefunded account id"""

    return_address: str
    """Address to return funds on failed transactions (Not supported on Stellar)"""
