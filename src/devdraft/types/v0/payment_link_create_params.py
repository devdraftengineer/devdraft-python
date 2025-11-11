# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PaymentLinkCreateParams", "PaymentLinkProduct"]


class PaymentLinkCreateParams(TypedDict, total=False):
    allow_mobile_payment: Required[Annotated[bool, PropertyInfo(alias="allowMobilePayment")]]
    """Whether to allow mobile payment"""

    allow_quantity_adjustment: Required[Annotated[bool, PropertyInfo(alias="allowQuantityAdjustment")]]
    """Whether to allow quantity adjustment"""

    collect_address: Required[Annotated[bool, PropertyInfo(alias="collectAddress")]]
    """Whether to collect address"""

    collect_tax: Required[Annotated[bool, PropertyInfo(alias="collectTax")]]
    """Whether to collect tax"""

    currency: Required[Literal["usdc", "eurc"]]
    """Currency"""

    link_type: Required[
        Annotated[Literal["INVOICE", "PRODUCT", "COLLECTION", "DONATION"], PropertyInfo(alias="linkType")]
    ]
    """Type of the payment link"""

    title: Required[str]
    """Display title for the payment link.

    This appears on the checkout page and in customer communications.
    """

    url: Required[str]
    """Unique URL slug for the payment link.

    Can be a full URL or just the path segment. Must be unique within your account.
    """

    amount: float
    """Amount for the payment link"""

    cover_image: Annotated[str, PropertyInfo(alias="coverImage")]
    """Cover image URL"""

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """Customer ID"""

    custom_fields: Annotated[object, PropertyInfo(alias="customFields")]
    """Custom fields"""

    description: str
    """Detailed description of what the customer is purchasing.

    Supports markdown formatting.
    """

    expiration_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Expiration date"""

    is_for_all_product: Annotated[bool, PropertyInfo(alias="isForAllProduct")]
    """Whether the payment link is for all products"""

    limit_payments: Annotated[bool, PropertyInfo(alias="limitPayments")]
    """Whether to limit payments"""

    max_payments: Annotated[float, PropertyInfo(alias="maxPayments")]
    """Maximum number of payments"""

    payment_for_id: Annotated[str, PropertyInfo(alias="paymentForId")]
    """Payment for ID"""

    payment_link_products: Annotated[Iterable[PaymentLinkProduct], PropertyInfo(alias="paymentLinkProducts")]
    """Array of products in the payment link"""

    tax_id: Annotated[str, PropertyInfo(alias="taxId")]
    """Tax ID"""


class PaymentLinkProduct(TypedDict, total=False):
    product_id: Required[Annotated[str, PropertyInfo(alias="productId")]]
    """UUID of the product to include in this payment link.

    Must be a valid product from your catalog.
    """

    quantity: Required[int]
    """Quantity of this product to include. Must be at least 1."""
