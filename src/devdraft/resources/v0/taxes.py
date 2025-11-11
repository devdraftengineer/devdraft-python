# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v0 import tax_list_params, tax_create_params, tax_update_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v0.tax_create_response import TaxCreateResponse

__all__ = ["TaxesResource", "AsyncTaxesResource"]


class TaxesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TaxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return TaxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TaxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python#with_streaming_response
        """
        return TaxesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        percentage: float,
        active: bool | Omit = omit,
        app_ids: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxCreateResponse:
        """
        Creates a new tax rate that can be applied to products, invoices, and payment
        links.

        ## Use Cases

        - Set up sales tax for different regions
        - Create VAT rates for international customers
        - Configure state and local tax rates
        - Manage tax compliance requirements

        ## Example: Create Basic Sales Tax

        ```json
        {
          "name": "Sales Tax",
          "description": "Standard sales tax for retail transactions",
          "percentage": 8.5,
          "active": true
        }
        ```

        ## Required Fields

        - `name`: Tax name for identification (1-100 characters)
        - `percentage`: Tax rate percentage (0-100)

        ## Optional Fields

        - `description`: Explanation of what this tax covers (max 255 characters)
        - `active`: Whether this tax is currently active (default: true)
        - `appIds`: Array of app IDs where this tax should be available

        Args:
          name: Tax name. Used to identify and reference this tax rate.

          percentage: Tax percentage rate. Must be between 0 and 100.

          active: Whether this tax is currently active and can be applied.

          app_ids: Array of app IDs where this tax should be available. If not provided, tax will
              be available for the current app.

          description: Optional description explaining what this tax covers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v0/taxes",
            body=maybe_transform(
                {
                    "name": name,
                    "percentage": percentage,
                    "active": active,
                    "app_ids": app_ids,
                    "description": description,
                },
                tax_create_params.TaxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaxCreateResponse,
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
        Retrieves detailed information about a specific tax.

        ## Use Cases

        - View tax details
        - Verify tax configuration
        - Check tax status before applying to products

        ## Path Parameters

        - `id`: Tax UUID (required) - Must be a valid UUID format

        ## Example Request

        `GET /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000`

        ## Example Response

        ```json
        {
          "id": "tax_123456",
          "name": "Sales Tax",
          "description": "Standard sales tax for retail transactions",
          "percentage": 8.5,
          "active": true,
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
            f"/api/v0/taxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        app_ids: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        name: str | Omit = omit,
        percentage: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Updates an existing tax's information.

        ## Use Cases

        - Modify tax percentage rates
        - Update tax descriptions
        - Activate/deactivate taxes
        - Change tax names

        ## Path Parameters

        - `id`: Tax UUID (required) - Must be a valid UUID format

        ## Example Request

        `PUT /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000`

        ## Example Request Body

        ```json
        {
          "name": "Updated Sales Tax",
          "description": "Updated sales tax rate",
          "percentage": 9.0,
          "active": true
        }
        ```

        ## Notes

        - Only include fields that need to be updated
        - All fields are optional in updates
        - Percentage changes affect future calculations only

        Args:
          active: Whether this tax is currently active and can be applied

          app_ids: Array of app IDs where this tax should be available

          description: Detailed description of what this tax covers

          name: Tax name for identification and display purposes

          percentage: Tax rate as a percentage (0-100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/v0/taxes/{id}",
            body=maybe_transform(
                {
                    "active": active,
                    "app_ids": app_ids,
                    "description": description,
                    "name": name,
                    "percentage": percentage,
                },
                tax_update_params.TaxUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        active: bool | Omit = omit,
        name: str | Omit = omit,
        skip: float | Omit = omit,
        take: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieves a list of taxes with optional filtering and pagination.

        ## Use Cases

        - List all available tax rates
        - Search taxes by name
        - Filter active/inactive taxes
        - Export tax configuration

        ## Query Parameters

        - `skip`: Number of records to skip (default: 0, min: 0)
        - `take`: Number of records to return (default: 10, min: 1, max: 100)
        - `name`: Filter taxes by name (partial match, case-insensitive)
        - `active`: Filter by active status (true/false)

        ## Example Request

        `GET /api/v0/taxes?skip=0&take=20&active=true&name=Sales`

        ## Example Response

        ```json
        [
          {
            "id": "tax_123456",
            "name": "Sales Tax",
            "description": "Standard sales tax for retail transactions",
            "percentage": 8.5,
            "active": true,
            "created_at": "2024-03-20T10:00:00Z",
            "updated_at": "2024-03-20T10:00:00Z"
          }
        ]
        ```

        Args:
          active: Filter by active status

          name: Filter taxes by name (partial match, case-insensitive)

          skip: Number of records to skip for pagination

          take: Number of records to return (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/v0/taxes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active": active,
                        "name": name,
                        "skip": skip,
                        "take": take,
                    },
                    tax_list_params.TaxListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def delete(
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
        Deletes an existing tax.

        ## Use Cases

        - Remove obsolete tax rates
        - Clean up unused taxes
        - Comply with regulatory changes

        ## Path Parameters

        - `id`: Tax UUID (required) - Must be a valid UUID format

        ## Example Request

        `DELETE /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000`

        ## Warning

        This action cannot be undone. Consider deactivating the tax instead of deleting
        it if it has been used in transactions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v0/taxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint requires a tax ID in the URL path.

        Use DELETE /api/v0/taxes/{id}
        instead.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/api/v0/taxes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint requires a tax ID in the URL path.

        Use PUT /api/v0/taxes/{id}
        instead.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/api/v0/taxes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTaxesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTaxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTaxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTaxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python#with_streaming_response
        """
        return AsyncTaxesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        percentage: float,
        active: bool | Omit = omit,
        app_ids: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaxCreateResponse:
        """
        Creates a new tax rate that can be applied to products, invoices, and payment
        links.

        ## Use Cases

        - Set up sales tax for different regions
        - Create VAT rates for international customers
        - Configure state and local tax rates
        - Manage tax compliance requirements

        ## Example: Create Basic Sales Tax

        ```json
        {
          "name": "Sales Tax",
          "description": "Standard sales tax for retail transactions",
          "percentage": 8.5,
          "active": true
        }
        ```

        ## Required Fields

        - `name`: Tax name for identification (1-100 characters)
        - `percentage`: Tax rate percentage (0-100)

        ## Optional Fields

        - `description`: Explanation of what this tax covers (max 255 characters)
        - `active`: Whether this tax is currently active (default: true)
        - `appIds`: Array of app IDs where this tax should be available

        Args:
          name: Tax name. Used to identify and reference this tax rate.

          percentage: Tax percentage rate. Must be between 0 and 100.

          active: Whether this tax is currently active and can be applied.

          app_ids: Array of app IDs where this tax should be available. If not provided, tax will
              be available for the current app.

          description: Optional description explaining what this tax covers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v0/taxes",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "percentage": percentage,
                    "active": active,
                    "app_ids": app_ids,
                    "description": description,
                },
                tax_create_params.TaxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaxCreateResponse,
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
        Retrieves detailed information about a specific tax.

        ## Use Cases

        - View tax details
        - Verify tax configuration
        - Check tax status before applying to products

        ## Path Parameters

        - `id`: Tax UUID (required) - Must be a valid UUID format

        ## Example Request

        `GET /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000`

        ## Example Response

        ```json
        {
          "id": "tax_123456",
          "name": "Sales Tax",
          "description": "Standard sales tax for retail transactions",
          "percentage": 8.5,
          "active": true,
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
            f"/api/v0/taxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        app_ids: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        name: str | Omit = omit,
        percentage: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Updates an existing tax's information.

        ## Use Cases

        - Modify tax percentage rates
        - Update tax descriptions
        - Activate/deactivate taxes
        - Change tax names

        ## Path Parameters

        - `id`: Tax UUID (required) - Must be a valid UUID format

        ## Example Request

        `PUT /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000`

        ## Example Request Body

        ```json
        {
          "name": "Updated Sales Tax",
          "description": "Updated sales tax rate",
          "percentage": 9.0,
          "active": true
        }
        ```

        ## Notes

        - Only include fields that need to be updated
        - All fields are optional in updates
        - Percentage changes affect future calculations only

        Args:
          active: Whether this tax is currently active and can be applied

          app_ids: Array of app IDs where this tax should be available

          description: Detailed description of what this tax covers

          name: Tax name for identification and display purposes

          percentage: Tax rate as a percentage (0-100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/v0/taxes/{id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "app_ids": app_ids,
                    "description": description,
                    "name": name,
                    "percentage": percentage,
                },
                tax_update_params.TaxUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        active: bool | Omit = omit,
        name: str | Omit = omit,
        skip: float | Omit = omit,
        take: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieves a list of taxes with optional filtering and pagination.

        ## Use Cases

        - List all available tax rates
        - Search taxes by name
        - Filter active/inactive taxes
        - Export tax configuration

        ## Query Parameters

        - `skip`: Number of records to skip (default: 0, min: 0)
        - `take`: Number of records to return (default: 10, min: 1, max: 100)
        - `name`: Filter taxes by name (partial match, case-insensitive)
        - `active`: Filter by active status (true/false)

        ## Example Request

        `GET /api/v0/taxes?skip=0&take=20&active=true&name=Sales`

        ## Example Response

        ```json
        [
          {
            "id": "tax_123456",
            "name": "Sales Tax",
            "description": "Standard sales tax for retail transactions",
            "percentage": 8.5,
            "active": true,
            "created_at": "2024-03-20T10:00:00Z",
            "updated_at": "2024-03-20T10:00:00Z"
          }
        ]
        ```

        Args:
          active: Filter by active status

          name: Filter taxes by name (partial match, case-insensitive)

          skip: Number of records to skip for pagination

          take: Number of records to return (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/v0/taxes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active": active,
                        "name": name,
                        "skip": skip,
                        "take": take,
                    },
                    tax_list_params.TaxListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def delete(
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
        Deletes an existing tax.

        ## Use Cases

        - Remove obsolete tax rates
        - Clean up unused taxes
        - Comply with regulatory changes

        ## Path Parameters

        - `id`: Tax UUID (required) - Must be a valid UUID format

        ## Example Request

        `DELETE /api/v0/taxes/123e4567-e89b-12d3-a456-426614174000`

        ## Warning

        This action cannot be undone. Consider deactivating the tax instead of deleting
        it if it has been used in transactions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v0/taxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint requires a tax ID in the URL path.

        Use DELETE /api/v0/taxes/{id}
        instead.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/api/v0/taxes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """This endpoint requires a tax ID in the URL path.

        Use PUT /api/v0/taxes/{id}
        instead.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/api/v0/taxes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TaxesResourceWithRawResponse:
    def __init__(self, taxes: TaxesResource) -> None:
        self._taxes = taxes

        self.create = to_raw_response_wrapper(
            taxes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            taxes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            taxes.update,
        )
        self.list = to_raw_response_wrapper(
            taxes.list,
        )
        self.delete = to_raw_response_wrapper(
            taxes.delete,
        )
        self.delete_all = to_raw_response_wrapper(
            taxes.delete_all,
        )
        self.update_all = to_raw_response_wrapper(
            taxes.update_all,
        )


class AsyncTaxesResourceWithRawResponse:
    def __init__(self, taxes: AsyncTaxesResource) -> None:
        self._taxes = taxes

        self.create = async_to_raw_response_wrapper(
            taxes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            taxes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            taxes.update,
        )
        self.list = async_to_raw_response_wrapper(
            taxes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            taxes.delete,
        )
        self.delete_all = async_to_raw_response_wrapper(
            taxes.delete_all,
        )
        self.update_all = async_to_raw_response_wrapper(
            taxes.update_all,
        )


class TaxesResourceWithStreamingResponse:
    def __init__(self, taxes: TaxesResource) -> None:
        self._taxes = taxes

        self.create = to_streamed_response_wrapper(
            taxes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            taxes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            taxes.update,
        )
        self.list = to_streamed_response_wrapper(
            taxes.list,
        )
        self.delete = to_streamed_response_wrapper(
            taxes.delete,
        )
        self.delete_all = to_streamed_response_wrapper(
            taxes.delete_all,
        )
        self.update_all = to_streamed_response_wrapper(
            taxes.update_all,
        )


class AsyncTaxesResourceWithStreamingResponse:
    def __init__(self, taxes: AsyncTaxesResource) -> None:
        self._taxes = taxes

        self.create = async_to_streamed_response_wrapper(
            taxes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            taxes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            taxes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            taxes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            taxes.delete,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            taxes.delete_all,
        )
        self.update_all = async_to_streamed_response_wrapper(
            taxes.update_all,
        )
