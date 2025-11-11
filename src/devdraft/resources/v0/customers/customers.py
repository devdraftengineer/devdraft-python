# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v0 import (
    CustomerType,
    CustomerStatus,
    customer_list_params,
    customer_create_params,
    customer_update_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .liquidation_addresses import (
    LiquidationAddressesResource,
    AsyncLiquidationAddressesResource,
    LiquidationAddressesResourceWithRawResponse,
    AsyncLiquidationAddressesResourceWithRawResponse,
    LiquidationAddressesResourceWithStreamingResponse,
    AsyncLiquidationAddressesResourceWithStreamingResponse,
)
from ....types.v0.customer_type import CustomerType
from ....types.v0.customer_status import CustomerStatus

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def liquidation_addresses(self) -> LiquidationAddressesResource:
        return LiquidationAddressesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python#with_streaming_response
        """
        return CustomersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        first_name: str,
        last_name: str,
        phone_number: str,
        customer_type: CustomerType | Omit = omit,
        email: str | Omit = omit,
        status: CustomerStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Creates a new customer in the system with their personal and contact
        information.

        This endpoint allows you to register new customers and store their details for
        future transactions.

        ## Use Cases

        - Register new customers for payment processing
        - Store customer information for recurring payments
        - Maintain customer profiles for transaction history

        ## Example: Create New Customer

        ```json
        {
          "first_name": "John",
          "last_name": "Doe",
          "email": "john.doe@example.com",
          "phone_number": "+1-555-123-4567",
          "customer_type": "Startup",
          "status": "ACTIVE"
        }
        ```

        ## Required Fields

        - `first_name`: Customer's first name (1-100 characters)
        - `last_name`: Customer's last name (1-100 characters)
        - `phone_number`: Customer's phone number (max 20 characters)

        ## Optional Fields

        - `email`: Valid email address (max 255 characters)
        - `customer_type`: Type of customer account (Individual, Startup, Small
          Business, Medium Business, Enterprise, Non-Profit, Government)
        - `status`: Customer status (ACTIVE, BLACKLISTED, DEACTIVATED)

        Args:
          first_name: Customer's first name. Used for personalization and legal documentation.

          last_name: Customer's last name. Used for personalization and legal documentation.

          phone_number: Customer's phone number. Used for SMS notifications and verification. Include
              country code for international numbers.

          customer_type: Type of customer account. Determines available features and compliance
              requirements.

          email: Customer's email address. Used for notifications, receipts, and account
              management. Must be a valid email format.

          status: Current status of the customer account. Controls access to services and
              features.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v0/customers",
            body=maybe_transform(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "customer_type": customer_type,
                    "email": email,
                    "status": status,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieves detailed information about a specific customer.

        This endpoint allows you to fetch complete customer details including their
        contact information and status.

        ## Use Cases

        - View customer details
        - Verify customer information
        - Check customer status before processing payments

        ## Path Parameters

        - `id`: Customer UUID (required) - Must be a valid UUID format

        ## Example Request

        `GET /api/v0/customers/123e4567-e89b-12d3-a456-426614174000`

        ## Example Response

        ```json
        {
          "id": "cust_123456",
          "first_name": "John",
          "last_name": "Doe",
          "email": "john.doe@example.com",
          "phone_number": "+1-555-123-4567",
          "customer_type": "Enterprise",
          "status": "ACTIVE",
          "last_spent": 1250.5,
          "last_purchase_date": "2024-03-15T14:30:00Z",
          "created_at": "2024-03-20T10:00:00Z",
          "updated_at": "2024-03-20T10:00:00Z"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/v0/customers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        id: str,
        *,
        customer_type: CustomerType | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        phone_number: str | Omit = omit,
        status: CustomerStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Updates an existing customer's information.

        This endpoint allows you to modify customer details while preserving their core
        information.

        ## Use Cases

        - Update customer contact information
        - Change customer type
        - Modify customer status

        ## Path Parameters

        - `id`: Customer UUID (required) - Must be a valid UUID format

        ## Example Request

        `PATCH /api/v0/customers/123e4567-e89b-12d3-a456-426614174000`

        ## Example Request Body

        ```json
        {
          "first_name": "John",
          "last_name": "Smith",
          "phone_number": "+1-987-654-3210",
          "customer_type": "Small Business"
        }
        ```

        ## Notes

        - Only include fields that need to be updated
        - All fields are optional in updates
        - Status changes may require additional verification

        Args:
          customer_type: Type of customer account. Determines available features and compliance
              requirements.

          email: Customer's email address. Used for notifications, receipts, and account
              management. Must be a valid email format.

          first_name: Customer's first name. Used for personalization and legal documentation.

          last_name: Customer's last name. Used for personalization and legal documentation.

          phone_number: Customer's phone number. Used for SMS notifications and verification. Include
              country code for international numbers.

          status: Current status of the customer account. Controls access to services and
              features.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/api/v0/customers/{id}",
            body=maybe_transform(
                {
                    "customer_type": customer_type,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "status": status,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        email: str | Omit = omit,
        name: str | Omit = omit,
        skip: float | Omit = omit,
        status: CustomerStatus | Omit = omit,
        take: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieves a list of customers with optional filtering and pagination.

        This endpoint allows you to search and filter customers based on various
        criteria.

        ## Use Cases

        - List all customers with pagination
        - Search customers by name or email
        - Filter customers by status
        - Export customer data

        ## Query Parameters

        - `skip`: Number of records to skip (default: 0, min: 0)
        - `take`: Number of records to take (default: 10, min: 1, max: 100)
        - `status`: Filter by customer status (ACTIVE, BLACKLISTED, DEACTIVATED)
        - `name`: Filter by customer name (partial match, case-insensitive)
        - `email`: Filter by customer email (exact match, case-insensitive)

        ## Example Request

        `GET /api/v0/customers?skip=0&take=20&status=ACTIVE&name=John`

        ## Example Response

        ```json
        {
          "data": [
            {
              "id": "cust_123456",
              "first_name": "John",
              "last_name": "Doe",
              "email": "john.doe@example.com",
              "phone_number": "+1-555-123-4567",
              "customer_type": "Startup",
              "status": "ACTIVE",
              "created_at": "2024-03-20T10:00:00Z",
              "updated_at": "2024-03-20T10:00:00Z"
            }
          ],
          "total": 100,
          "skip": 0,
          "take": 10
        }
        ```

        Args:
          email: Filter customers by email (exact match, case-insensitive)

          name: Filter customers by name (partial match, case-insensitive)

          skip: Number of records to skip for pagination

          status: Filter customers by status

          take: Number of records to return (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/v0/customers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email": email,
                        "name": name,
                        "skip": skip,
                        "status": status,
                        "take": take,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def liquidation_addresses(self) -> AsyncLiquidationAddressesResource:
        return AsyncLiquidationAddressesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python#with_streaming_response
        """
        return AsyncCustomersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        first_name: str,
        last_name: str,
        phone_number: str,
        customer_type: CustomerType | Omit = omit,
        email: str | Omit = omit,
        status: CustomerStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Creates a new customer in the system with their personal and contact
        information.

        This endpoint allows you to register new customers and store their details for
        future transactions.

        ## Use Cases

        - Register new customers for payment processing
        - Store customer information for recurring payments
        - Maintain customer profiles for transaction history

        ## Example: Create New Customer

        ```json
        {
          "first_name": "John",
          "last_name": "Doe",
          "email": "john.doe@example.com",
          "phone_number": "+1-555-123-4567",
          "customer_type": "Startup",
          "status": "ACTIVE"
        }
        ```

        ## Required Fields

        - `first_name`: Customer's first name (1-100 characters)
        - `last_name`: Customer's last name (1-100 characters)
        - `phone_number`: Customer's phone number (max 20 characters)

        ## Optional Fields

        - `email`: Valid email address (max 255 characters)
        - `customer_type`: Type of customer account (Individual, Startup, Small
          Business, Medium Business, Enterprise, Non-Profit, Government)
        - `status`: Customer status (ACTIVE, BLACKLISTED, DEACTIVATED)

        Args:
          first_name: Customer's first name. Used for personalization and legal documentation.

          last_name: Customer's last name. Used for personalization and legal documentation.

          phone_number: Customer's phone number. Used for SMS notifications and verification. Include
              country code for international numbers.

          customer_type: Type of customer account. Determines available features and compliance
              requirements.

          email: Customer's email address. Used for notifications, receipts, and account
              management. Must be a valid email format.

          status: Current status of the customer account. Controls access to services and
              features.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v0/customers",
            body=await async_maybe_transform(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "customer_type": customer_type,
                    "email": email,
                    "status": status,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieves detailed information about a specific customer.

        This endpoint allows you to fetch complete customer details including their
        contact information and status.

        ## Use Cases

        - View customer details
        - Verify customer information
        - Check customer status before processing payments

        ## Path Parameters

        - `id`: Customer UUID (required) - Must be a valid UUID format

        ## Example Request

        `GET /api/v0/customers/123e4567-e89b-12d3-a456-426614174000`

        ## Example Response

        ```json
        {
          "id": "cust_123456",
          "first_name": "John",
          "last_name": "Doe",
          "email": "john.doe@example.com",
          "phone_number": "+1-555-123-4567",
          "customer_type": "Enterprise",
          "status": "ACTIVE",
          "last_spent": 1250.5,
          "last_purchase_date": "2024-03-15T14:30:00Z",
          "created_at": "2024-03-20T10:00:00Z",
          "updated_at": "2024-03-20T10:00:00Z"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/v0/customers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        id: str,
        *,
        customer_type: CustomerType | Omit = omit,
        email: str | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        phone_number: str | Omit = omit,
        status: CustomerStatus | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Updates an existing customer's information.

        This endpoint allows you to modify customer details while preserving their core
        information.

        ## Use Cases

        - Update customer contact information
        - Change customer type
        - Modify customer status

        ## Path Parameters

        - `id`: Customer UUID (required) - Must be a valid UUID format

        ## Example Request

        `PATCH /api/v0/customers/123e4567-e89b-12d3-a456-426614174000`

        ## Example Request Body

        ```json
        {
          "first_name": "John",
          "last_name": "Smith",
          "phone_number": "+1-987-654-3210",
          "customer_type": "Small Business"
        }
        ```

        ## Notes

        - Only include fields that need to be updated
        - All fields are optional in updates
        - Status changes may require additional verification

        Args:
          customer_type: Type of customer account. Determines available features and compliance
              requirements.

          email: Customer's email address. Used for notifications, receipts, and account
              management. Must be a valid email format.

          first_name: Customer's first name. Used for personalization and legal documentation.

          last_name: Customer's last name. Used for personalization and legal documentation.

          phone_number: Customer's phone number. Used for SMS notifications and verification. Include
              country code for international numbers.

          status: Current status of the customer account. Controls access to services and
              features.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/api/v0/customers/{id}",
            body=await async_maybe_transform(
                {
                    "customer_type": customer_type,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "status": status,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        email: str | Omit = omit,
        name: str | Omit = omit,
        skip: float | Omit = omit,
        status: CustomerStatus | Omit = omit,
        take: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieves a list of customers with optional filtering and pagination.

        This endpoint allows you to search and filter customers based on various
        criteria.

        ## Use Cases

        - List all customers with pagination
        - Search customers by name or email
        - Filter customers by status
        - Export customer data

        ## Query Parameters

        - `skip`: Number of records to skip (default: 0, min: 0)
        - `take`: Number of records to take (default: 10, min: 1, max: 100)
        - `status`: Filter by customer status (ACTIVE, BLACKLISTED, DEACTIVATED)
        - `name`: Filter by customer name (partial match, case-insensitive)
        - `email`: Filter by customer email (exact match, case-insensitive)

        ## Example Request

        `GET /api/v0/customers?skip=0&take=20&status=ACTIVE&name=John`

        ## Example Response

        ```json
        {
          "data": [
            {
              "id": "cust_123456",
              "first_name": "John",
              "last_name": "Doe",
              "email": "john.doe@example.com",
              "phone_number": "+1-555-123-4567",
              "customer_type": "Startup",
              "status": "ACTIVE",
              "created_at": "2024-03-20T10:00:00Z",
              "updated_at": "2024-03-20T10:00:00Z"
            }
          ],
          "total": 100,
          "skip": 0,
          "take": 10
        }
        ```

        Args:
          email: Filter customers by email (exact match, case-insensitive)

          name: Filter customers by name (partial match, case-insensitive)

          skip: Number of records to skip for pagination

          status: Filter customers by status

          take: Number of records to return (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/v0/customers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email": email,
                        "name": name,
                        "skip": skip,
                        "status": status,
                        "take": take,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            cast_to=NoneType,
        )


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            customers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            customers.update,
        )
        self.list = to_raw_response_wrapper(
            customers.list,
        )

    @cached_property
    def liquidation_addresses(self) -> LiquidationAddressesResourceWithRawResponse:
        return LiquidationAddressesResourceWithRawResponse(self._customers.liquidation_addresses)


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            customers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            customers.update,
        )
        self.list = async_to_raw_response_wrapper(
            customers.list,
        )

    @cached_property
    def liquidation_addresses(self) -> AsyncLiquidationAddressesResourceWithRawResponse:
        return AsyncLiquidationAddressesResourceWithRawResponse(self._customers.liquidation_addresses)


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            customers.update,
        )
        self.list = to_streamed_response_wrapper(
            customers.list,
        )

    @cached_property
    def liquidation_addresses(self) -> LiquidationAddressesResourceWithStreamingResponse:
        return LiquidationAddressesResourceWithStreamingResponse(self._customers.liquidation_addresses)


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            customers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            customers.list,
        )

    @cached_property
    def liquidation_addresses(self) -> AsyncLiquidationAddressesResourceWithStreamingResponse:
        return AsyncLiquidationAddressesResourceWithStreamingResponse(self._customers.liquidation_addresses)
