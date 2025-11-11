# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v0 import payment_link_list_params, payment_link_create_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["PaymentLinksResource", "AsyncPaymentLinksResource"]


class PaymentLinksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return PaymentLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#with_streaming_response
        """
        return PaymentLinksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        allow_mobile_payment: bool,
        allow_quantity_adjustment: bool,
        collect_address: bool,
        collect_tax: bool,
        currency: Literal["usdc", "eurc"],
        link_type: Literal["INVOICE", "PRODUCT", "COLLECTION", "DONATION"],
        title: str,
        url: str,
        amount: float | Omit = omit,
        cover_image: str | Omit = omit,
        customer_id: str | Omit = omit,
        custom_fields: object | Omit = omit,
        description: str | Omit = omit,
        expiration_date: Union[str, datetime] | Omit = omit,
        is_for_all_product: bool | Omit = omit,
        limit_payments: bool | Omit = omit,
        max_payments: float | Omit = omit,
        payment_for_id: str | Omit = omit,
        payment_link_products: Iterable[payment_link_create_params.PaymentLinkProduct] | Omit = omit,
        tax_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Creates a new payment link with the provided details.

        Supports both simple
        one-time payments and complex product bundles.

        Args:
          allow_mobile_payment: Whether to allow mobile payment

          allow_quantity_adjustment: Whether to allow quantity adjustment

          collect_address: Whether to collect address

          collect_tax: Whether to collect tax

          currency: Currency

          link_type: Type of the payment link

          title: Display title for the payment link. This appears on the checkout page and in
              customer communications.

          url: Unique URL slug for the payment link. Can be a full URL or just the path
              segment. Must be unique within your account.

          amount: Amount for the payment link

          cover_image: Cover image URL

          customer_id: Customer ID

          custom_fields: Custom fields

          description: Detailed description of what the customer is purchasing. Supports markdown
              formatting.

          expiration_date: Expiration date

          is_for_all_product: Whether the payment link is for all products

          limit_payments: Whether to limit payments

          max_payments: Maximum number of payments

          payment_for_id: Payment for ID

          payment_link_products: Array of products in the payment link

          tax_id: Tax ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v0/payment-links",
            body=maybe_transform(
                {
                    "allow_mobile_payment": allow_mobile_payment,
                    "allow_quantity_adjustment": allow_quantity_adjustment,
                    "collect_address": collect_address,
                    "collect_tax": collect_tax,
                    "currency": currency,
                    "link_type": link_type,
                    "title": title,
                    "url": url,
                    "amount": amount,
                    "cover_image": cover_image,
                    "customer_id": customer_id,
                    "custom_fields": custom_fields,
                    "description": description,
                    "expiration_date": expiration_date,
                    "is_for_all_product": is_for_all_product,
                    "limit_payments": limit_payments,
                    "max_payments": max_payments,
                    "payment_for_id": payment_for_id,
                    "payment_link_products": payment_link_products,
                    "tax_id": tax_id,
                },
                payment_link_create_params.PaymentLinkCreateParams,
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
        Get a payment link by ID

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
            f"/api/v0/payment-links/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
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
        Update a payment link

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/v0/payment-links/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        skip: str | Omit = omit,
        take: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get all payment links

        Args:
          skip: Number of records to skip (must be non-negative)

          take: Number of records to take (must be positive)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/v0/payment-links",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "skip": skip,
                        "take": take,
                    },
                    payment_link_list_params.PaymentLinkListParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncPaymentLinksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#with_streaming_response
        """
        return AsyncPaymentLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        allow_mobile_payment: bool,
        allow_quantity_adjustment: bool,
        collect_address: bool,
        collect_tax: bool,
        currency: Literal["usdc", "eurc"],
        link_type: Literal["INVOICE", "PRODUCT", "COLLECTION", "DONATION"],
        title: str,
        url: str,
        amount: float | Omit = omit,
        cover_image: str | Omit = omit,
        customer_id: str | Omit = omit,
        custom_fields: object | Omit = omit,
        description: str | Omit = omit,
        expiration_date: Union[str, datetime] | Omit = omit,
        is_for_all_product: bool | Omit = omit,
        limit_payments: bool | Omit = omit,
        max_payments: float | Omit = omit,
        payment_for_id: str | Omit = omit,
        payment_link_products: Iterable[payment_link_create_params.PaymentLinkProduct] | Omit = omit,
        tax_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Creates a new payment link with the provided details.

        Supports both simple
        one-time payments and complex product bundles.

        Args:
          allow_mobile_payment: Whether to allow mobile payment

          allow_quantity_adjustment: Whether to allow quantity adjustment

          collect_address: Whether to collect address

          collect_tax: Whether to collect tax

          currency: Currency

          link_type: Type of the payment link

          title: Display title for the payment link. This appears on the checkout page and in
              customer communications.

          url: Unique URL slug for the payment link. Can be a full URL or just the path
              segment. Must be unique within your account.

          amount: Amount for the payment link

          cover_image: Cover image URL

          customer_id: Customer ID

          custom_fields: Custom fields

          description: Detailed description of what the customer is purchasing. Supports markdown
              formatting.

          expiration_date: Expiration date

          is_for_all_product: Whether the payment link is for all products

          limit_payments: Whether to limit payments

          max_payments: Maximum number of payments

          payment_for_id: Payment for ID

          payment_link_products: Array of products in the payment link

          tax_id: Tax ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v0/payment-links",
            body=await async_maybe_transform(
                {
                    "allow_mobile_payment": allow_mobile_payment,
                    "allow_quantity_adjustment": allow_quantity_adjustment,
                    "collect_address": collect_address,
                    "collect_tax": collect_tax,
                    "currency": currency,
                    "link_type": link_type,
                    "title": title,
                    "url": url,
                    "amount": amount,
                    "cover_image": cover_image,
                    "customer_id": customer_id,
                    "custom_fields": custom_fields,
                    "description": description,
                    "expiration_date": expiration_date,
                    "is_for_all_product": is_for_all_product,
                    "limit_payments": limit_payments,
                    "max_payments": max_payments,
                    "payment_for_id": payment_for_id,
                    "payment_link_products": payment_link_products,
                    "tax_id": tax_id,
                },
                payment_link_create_params.PaymentLinkCreateParams,
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
        Get a payment link by ID

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
            f"/api/v0/payment-links/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
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
        Update a payment link

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/v0/payment-links/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        skip: str | Omit = omit,
        take: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get all payment links

        Args:
          skip: Number of records to skip (must be non-negative)

          take: Number of records to take (must be positive)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/v0/payment-links",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "skip": skip,
                        "take": take,
                    },
                    payment_link_list_params.PaymentLinkListParams,
                ),
            ),
            cast_to=NoneType,
        )


class PaymentLinksResourceWithRawResponse:
    def __init__(self, payment_links: PaymentLinksResource) -> None:
        self._payment_links = payment_links

        self.create = to_raw_response_wrapper(
            payment_links.create,
        )
        self.retrieve = to_raw_response_wrapper(
            payment_links.retrieve,
        )
        self.update = to_raw_response_wrapper(
            payment_links.update,
        )
        self.list = to_raw_response_wrapper(
            payment_links.list,
        )


class AsyncPaymentLinksResourceWithRawResponse:
    def __init__(self, payment_links: AsyncPaymentLinksResource) -> None:
        self._payment_links = payment_links

        self.create = async_to_raw_response_wrapper(
            payment_links.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            payment_links.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            payment_links.update,
        )
        self.list = async_to_raw_response_wrapper(
            payment_links.list,
        )


class PaymentLinksResourceWithStreamingResponse:
    def __init__(self, payment_links: PaymentLinksResource) -> None:
        self._payment_links = payment_links

        self.create = to_streamed_response_wrapper(
            payment_links.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payment_links.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            payment_links.update,
        )
        self.list = to_streamed_response_wrapper(
            payment_links.list,
        )


class AsyncPaymentLinksResourceWithStreamingResponse:
    def __init__(self, payment_links: AsyncPaymentLinksResource) -> None:
        self._payment_links = payment_links

        self.create = async_to_streamed_response_wrapper(
            payment_links.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payment_links.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            payment_links.update,
        )
        self.list = async_to_streamed_response_wrapper(
            payment_links.list,
        )
