# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .bridge_payment_rail import BridgePaymentRail
from .stable_coin_currency import StableCoinCurrency

__all__ = ["PaymentIntentCreateStableParams"]


class PaymentIntentCreateStableParams(TypedDict, total=False):
    destination_network: Required[Annotated[BridgePaymentRail, PropertyInfo(alias="destinationNetwork")]]
    """The blockchain network where the source currency resides.

    Determines gas fees and transaction speed.
    """

    source_currency: Required[Annotated[StableCoinCurrency, PropertyInfo(alias="sourceCurrency")]]
    """The stablecoin currency to convert FROM.

    This is the currency the customer will pay with.
    """

    source_network: Required[Annotated[BridgePaymentRail, PropertyInfo(alias="sourceNetwork")]]
    """The blockchain network where the source currency resides.

    Determines gas fees and transaction speed.
    """

    amount: str
    """Payment amount in the source currency.

    Omit for flexible amount payments where users specify the amount during
    checkout.
    """

    customer_address: str
    """Customer's full address.

    Required for compliance in certain jurisdictions and high-value transactions.
    """

    customer_country: str
    """Customer's country of residence. Used for compliance and tax reporting."""

    customer_country_iso: Annotated[str, PropertyInfo(alias="customer_countryISO")]
    """Customer's country ISO 3166-1 alpha-2 code.

    Used for automated compliance checks.
    """

    customer_email: str
    """Customer's email address.

    Used for transaction notifications and receipts. Highly recommended for all
    transactions.
    """

    customer_first_name: str
    """Customer's first name.

    Used for transaction records and compliance. Required for amounts over $1000.
    """

    customer_last_name: str
    """Customer's last name.

    Used for transaction records and compliance. Required for amounts over $1000.
    """

    customer_province: str
    """Customer's state or province. Required for US and Canadian customers."""

    customer_province_iso: Annotated[str, PropertyInfo(alias="customer_provinceISO")]
    """Customer's state or province ISO code. Used for automated tax calculations."""

    destination_address: Annotated[str, PropertyInfo(alias="destinationAddress")]
    """The wallet address where converted funds will be sent.

    Supports Ethereum (0x...) and Solana address formats.
    """

    destination_currency: Annotated[StableCoinCurrency, PropertyInfo(alias="destinationCurrency")]
    """The stablecoin currency to convert FROM.

    This is the currency the customer will pay with.
    """

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Customer's phone number with country code.

    Used for SMS notifications and verification.
    """
