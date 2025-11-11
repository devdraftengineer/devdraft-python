# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .customer_type import CustomerType
from .customer_status import CustomerStatus

__all__ = ["CustomerUpdateParams"]


class CustomerUpdateParams(TypedDict, total=False):
    customer_type: CustomerType
    """Type of customer account.

    Determines available features and compliance requirements.
    """

    email: str
    """Customer's email address.

    Used for notifications, receipts, and account management. Must be a valid email
    format.
    """

    first_name: str
    """Customer's first name. Used for personalization and legal documentation."""

    last_name: str
    """Customer's last name. Used for personalization and legal documentation."""

    phone_number: str
    """Customer's phone number.

    Used for SMS notifications and verification. Include country code for
    international numbers.
    """

    status: CustomerStatus
    """Current status of the customer account.

    Controls access to services and features.
    """
