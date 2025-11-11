# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .bridge_payment_rail import BridgePaymentRail
from .stable_coin_currency import StableCoinCurrency

__all__ = ["PaymentIntentCreateBankParams"]


class PaymentIntentCreateBankParams(TypedDict, total=False):
    destination_currency: Required[Annotated[StableCoinCurrency, PropertyInfo(alias="destinationCurrency")]]
    """The stablecoin currency to convert FROM.

    This is the currency the customer will pay with.
    """

    destination_network: Required[Annotated[BridgePaymentRail, PropertyInfo(alias="destinationNetwork")]]
    """The blockchain network where the source currency resides.

    Determines gas fees and transaction speed.
    """

    source_currency: Required[Annotated[Literal["usd", "eur", "mxn"], PropertyInfo(alias="sourceCurrency")]]
    """The fiat currency to convert FROM.

    Must match the currency of the source payment rail.
    """

    source_payment_rail: Required[Annotated[BridgePaymentRail, PropertyInfo(alias="sourcePaymentRail")]]
    """The blockchain network where the source currency resides.

    Determines gas fees and transaction speed.
    """

    ach_reference: str
    """ACH reference (for ACH transfers)"""

    amount: str
    """Payment amount (optional for flexible amount)"""

    customer_address: str
    """Customer address"""

    customer_country: str
    """Customer country"""

    customer_country_iso: Annotated[str, PropertyInfo(alias="customer_countryISO")]
    """Customer country ISO code"""

    customer_email: str
    """Customer email address"""

    customer_first_name: str
    """Customer first name"""

    customer_last_name: str
    """Customer last name"""

    customer_province: str
    """Customer province/state"""

    customer_province_iso: Annotated[str, PropertyInfo(alias="customer_provinceISO")]
    """Customer province/state ISO code"""

    destination_address: Annotated[str, PropertyInfo(alias="destinationAddress")]
    """Destination wallet address.

    Supports Ethereum (0x...) and Solana address formats.
    """

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Customer phone number"""

    sepa_reference: str
    """SEPA reference (for SEPA transfers)"""

    wire_message: str
    """Wire transfer message (for WIRE transfers)"""
