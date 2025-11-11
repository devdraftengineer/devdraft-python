# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v0 import invoice_list_params, invoice_create_params, invoice_update_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["InvoicesResource", "AsyncInvoicesResource"]


class InvoicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return InvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python#with_streaming_response
        """
        return InvoicesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        currency: Literal["usdc", "eurc"],
        customer_id: str,
        delivery: Literal["EMAIL", "MANUALLY"],
        due_date: Union[str, datetime],
        email: str,
        items: Iterable[invoice_create_params.Item],
        name: str,
        partial_payment: bool,
        payment_link: bool,
        payment_methods: List[Literal["ACH", "BANK_TRANSFER", "CREDIT_CARD", "CASH", "MOBILE_MONEY", "CRYPTO"]],
        status: Literal["DRAFT", "OPEN", "PASTDUE", "PAID", "PARTIALLYPAID"],
        address: str | Omit = omit,
        logo: str | Omit = omit,
        phone_number: str | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        tax_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a new invoice

        Args:
          currency: Currency for the invoice

          customer_id: Customer ID

          delivery: Delivery method

          due_date: Due date of the invoice

          email: Email address

          items: Array of products in the invoice

          name: Name of the invoice

          partial_payment: Allow partial payments

          payment_link: Whether to generate a payment link

          payment_methods: Array of accepted payment methods

          status: Invoice status

          address: Address

          logo: Logo URL

          phone_number: Phone number

          send_date: Send date

          tax_id: Tax ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v0/invoices",
            body=maybe_transform(
                {
                    "currency": currency,
                    "customer_id": customer_id,
                    "delivery": delivery,
                    "due_date": due_date,
                    "email": email,
                    "items": items,
                    "name": name,
                    "partial_payment": partial_payment,
                    "payment_link": payment_link,
                    "payment_methods": payment_methods,
                    "status": status,
                    "address": address,
                    "logo": logo,
                    "phone_number": phone_number,
                    "send_date": send_date,
                    "tax_id": tax_id,
                },
                invoice_create_params.InvoiceCreateParams,
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
        Get an invoice by ID

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
            f"/api/v0/invoices/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        id: str,
        *,
        currency: Literal["usdc", "eurc"],
        customer_id: str,
        delivery: Literal["EMAIL", "MANUALLY"],
        due_date: Union[str, datetime],
        email: str,
        items: Iterable[invoice_update_params.Item],
        name: str,
        partial_payment: bool,
        payment_link: bool,
        payment_methods: List[Literal["ACH", "BANK_TRANSFER", "CREDIT_CARD", "CASH", "MOBILE_MONEY", "CRYPTO"]],
        status: Literal["DRAFT", "OPEN", "PASTDUE", "PAID", "PARTIALLYPAID"],
        address: str | Omit = omit,
        logo: str | Omit = omit,
        phone_number: str | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        tax_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update an invoice

        Args:
          currency: Currency for the invoice

          customer_id: Customer ID

          delivery: Delivery method

          due_date: Due date of the invoice

          email: Email address

          items: Array of products in the invoice

          name: Name of the invoice

          partial_payment: Allow partial payments

          payment_link: Whether to generate a payment link

          payment_methods: Array of accepted payment methods

          status: Invoice status

          address: Address

          logo: Logo URL

          phone_number: Phone number

          send_date: Send date

          tax_id: Tax ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/v0/invoices/{id}",
            body=maybe_transform(
                {
                    "currency": currency,
                    "customer_id": customer_id,
                    "delivery": delivery,
                    "due_date": due_date,
                    "email": email,
                    "items": items,
                    "name": name,
                    "partial_payment": partial_payment,
                    "payment_link": payment_link,
                    "payment_methods": payment_methods,
                    "status": status,
                    "address": address,
                    "logo": logo,
                    "phone_number": phone_number,
                    "send_date": send_date,
                    "tax_id": tax_id,
                },
                invoice_update_params.InvoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
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
        Get all invoices

        Args:
          skip: Number of records to skip

          take: Number of records to take

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/v0/invoices",
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
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncInvoicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python#with_streaming_response
        """
        return AsyncInvoicesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        currency: Literal["usdc", "eurc"],
        customer_id: str,
        delivery: Literal["EMAIL", "MANUALLY"],
        due_date: Union[str, datetime],
        email: str,
        items: Iterable[invoice_create_params.Item],
        name: str,
        partial_payment: bool,
        payment_link: bool,
        payment_methods: List[Literal["ACH", "BANK_TRANSFER", "CREDIT_CARD", "CASH", "MOBILE_MONEY", "CRYPTO"]],
        status: Literal["DRAFT", "OPEN", "PASTDUE", "PAID", "PARTIALLYPAID"],
        address: str | Omit = omit,
        logo: str | Omit = omit,
        phone_number: str | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        tax_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a new invoice

        Args:
          currency: Currency for the invoice

          customer_id: Customer ID

          delivery: Delivery method

          due_date: Due date of the invoice

          email: Email address

          items: Array of products in the invoice

          name: Name of the invoice

          partial_payment: Allow partial payments

          payment_link: Whether to generate a payment link

          payment_methods: Array of accepted payment methods

          status: Invoice status

          address: Address

          logo: Logo URL

          phone_number: Phone number

          send_date: Send date

          tax_id: Tax ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v0/invoices",
            body=await async_maybe_transform(
                {
                    "currency": currency,
                    "customer_id": customer_id,
                    "delivery": delivery,
                    "due_date": due_date,
                    "email": email,
                    "items": items,
                    "name": name,
                    "partial_payment": partial_payment,
                    "payment_link": payment_link,
                    "payment_methods": payment_methods,
                    "status": status,
                    "address": address,
                    "logo": logo,
                    "phone_number": phone_number,
                    "send_date": send_date,
                    "tax_id": tax_id,
                },
                invoice_create_params.InvoiceCreateParams,
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
        Get an invoice by ID

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
            f"/api/v0/invoices/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        id: str,
        *,
        currency: Literal["usdc", "eurc"],
        customer_id: str,
        delivery: Literal["EMAIL", "MANUALLY"],
        due_date: Union[str, datetime],
        email: str,
        items: Iterable[invoice_update_params.Item],
        name: str,
        partial_payment: bool,
        payment_link: bool,
        payment_methods: List[Literal["ACH", "BANK_TRANSFER", "CREDIT_CARD", "CASH", "MOBILE_MONEY", "CRYPTO"]],
        status: Literal["DRAFT", "OPEN", "PASTDUE", "PAID", "PARTIALLYPAID"],
        address: str | Omit = omit,
        logo: str | Omit = omit,
        phone_number: str | Omit = omit,
        send_date: Union[str, datetime] | Omit = omit,
        tax_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update an invoice

        Args:
          currency: Currency for the invoice

          customer_id: Customer ID

          delivery: Delivery method

          due_date: Due date of the invoice

          email: Email address

          items: Array of products in the invoice

          name: Name of the invoice

          partial_payment: Allow partial payments

          payment_link: Whether to generate a payment link

          payment_methods: Array of accepted payment methods

          status: Invoice status

          address: Address

          logo: Logo URL

          phone_number: Phone number

          send_date: Send date

          tax_id: Tax ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/v0/invoices/{id}",
            body=await async_maybe_transform(
                {
                    "currency": currency,
                    "customer_id": customer_id,
                    "delivery": delivery,
                    "due_date": due_date,
                    "email": email,
                    "items": items,
                    "name": name,
                    "partial_payment": partial_payment,
                    "payment_link": payment_link,
                    "payment_methods": payment_methods,
                    "status": status,
                    "address": address,
                    "logo": logo,
                    "phone_number": phone_number,
                    "send_date": send_date,
                    "tax_id": tax_id,
                },
                invoice_update_params.InvoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
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
        Get all invoices

        Args:
          skip: Number of records to skip

          take: Number of records to take

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/v0/invoices",
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
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            cast_to=NoneType,
        )


class InvoicesResourceWithRawResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.create = to_raw_response_wrapper(
            invoices.create,
        )
        self.retrieve = to_raw_response_wrapper(
            invoices.retrieve,
        )
        self.update = to_raw_response_wrapper(
            invoices.update,
        )
        self.list = to_raw_response_wrapper(
            invoices.list,
        )


class AsyncInvoicesResourceWithRawResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.create = async_to_raw_response_wrapper(
            invoices.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            invoices.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            invoices.update,
        )
        self.list = async_to_raw_response_wrapper(
            invoices.list,
        )


class InvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.create = to_streamed_response_wrapper(
            invoices.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            invoices.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            invoices.update,
        )
        self.list = to_streamed_response_wrapper(
            invoices.list,
        )


class AsyncInvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.create = async_to_streamed_response_wrapper(
            invoices.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            invoices.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            invoices.update,
        )
        self.list = async_to_streamed_response_wrapper(
            invoices.list,
        )
