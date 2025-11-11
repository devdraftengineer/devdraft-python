# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["BridgePaymentRail"]

BridgePaymentRail: TypeAlias = Literal[
    "ethereum",
    "solana",
    "polygon",
    "avalanche_c_chain",
    "base",
    "arbitrum",
    "optimism",
    "stellar",
    "tron",
    "bridge_wallet",
    "wire",
    "ach",
    "ach_push",
    "ach_same_day",
    "sepa",
    "swift",
    "spei",
]
