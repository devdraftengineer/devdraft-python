# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v0 import (
    transfer_create_direct_bank_params,
    transfer_create_direct_wallet_params,
    transfer_create_stablecoin_conversion_params,
    transfer_create_external_bank_transfer_params,
    transfer_create_external_stablecoin_transfer_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["TransfersResource", "AsyncTransfersResource"]


class TransfersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#with_streaming_response
        """
        return TransfersResourceWithStreamingResponse(self)

    def create_direct_bank(
        self,
        *,
        amount: float,
        destination_currency: str,
        payment_rail: str,
        source_currency: str,
        wallet_id: str,
        ach_reference: str | Omit = omit,
        sepa_reference: str | Omit = omit,
        wire_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a direct bank transfer

        Args:
          amount: The amount to transfer

          destination_currency: The destination currency

          payment_rail: The payment rail to use

          source_currency: The source currency

          wallet_id: The ID of the bridge wallet to transfer from

          ach_reference: ACH transfer reference

          sepa_reference: SEPA transfer reference

          wire_message: Wire transfer message

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v0/transfers/direct-bank",
            body=maybe_transform(
                {
                    "amount": amount,
                    "destination_currency": destination_currency,
                    "payment_rail": payment_rail,
                    "source_currency": source_currency,
                    "wallet_id": wallet_id,
                    "ach_reference": ach_reference,
                    "sepa_reference": sepa_reference,
                    "wire_message": wire_message,
                },
                transfer_create_direct_bank_params.TransferCreateDirectBankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_direct_wallet(
        self,
        *,
        amount: float,
        network: str,
        stable_coin_currency: str,
        wallet_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a direct wallet transfer

        Args:
          amount: The amount to transfer

          network: The network to use for the transfer

          stable_coin_currency: The stablecoin currency to use

          wallet_id: The ID of the bridge wallet to transfer from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v0/transfers/direct-wallet",
            body=maybe_transform(
                {
                    "amount": amount,
                    "network": network,
                    "stable_coin_currency": stable_coin_currency,
                    "wallet_id": wallet_id,
                },
                transfer_create_direct_wallet_params.TransferCreateDirectWalletParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_external_bank_transfer(
        self,
        *,
        destination_currency: str,
        destination_payment_rail: Literal["ach", "ach_push", "ach_same_day", "wire", "sepa", "swift", "spei"],
        external_account_id: str,
        source_currency: str,
        source_wallet_id: str,
        ach_reference: str | Omit = omit,
        amount: float | Omit = omit,
        sepa_reference: str | Omit = omit,
        spei_reference: str | Omit = omit,
        swift_charges: str | Omit = omit,
        swift_reference: str | Omit = omit,
        wire_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create an external bank transfer

        Args:
          destination_currency: The destination currency

          destination_payment_rail: The destination payment rail (fiat payment method)

          external_account_id: The external account ID for the bank transfer

          source_currency: The source currency

          source_wallet_id: The ID of the source bridge wallet

          ach_reference: ACH reference message (1-10 characters, only for ACH transfers)

          amount: The amount to transfer

          sepa_reference: SEPA reference message (6-140 characters, only for SEPA transfers)

          spei_reference: SPEI reference message (1-40 characters, only for SPEI transfers)

          swift_charges: SWIFT charges bearer (only for SWIFT transfers)

          swift_reference: SWIFT reference message (1-190 characters, only for SWIFT transfers)

          wire_message: Wire transfer message (1-256 characters, only for wire transfers)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v0/transfers/external-bank-transfer",
            body=maybe_transform(
                {
                    "destination_currency": destination_currency,
                    "destination_payment_rail": destination_payment_rail,
                    "external_account_id": external_account_id,
                    "source_currency": source_currency,
                    "source_wallet_id": source_wallet_id,
                    "ach_reference": ach_reference,
                    "amount": amount,
                    "sepa_reference": sepa_reference,
                    "spei_reference": spei_reference,
                    "swift_charges": swift_charges,
                    "swift_reference": swift_reference,
                    "wire_message": wire_message,
                },
                transfer_create_external_bank_transfer_params.TransferCreateExternalBankTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_external_stablecoin_transfer(
        self,
        *,
        beneficiary_id: str,
        destination_currency: str,
        source_currency: str,
        source_wallet_id: str,
        amount: float | Omit = omit,
        blockchain_memo: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create an external stablecoin transfer

        Args:
          beneficiary_id: Beneficiary ID for the stablecoin transfer

          destination_currency: The destination currency

          source_currency: The source currency

          source_wallet_id: The ID of the source bridge wallet

          amount: The amount to transfer

          blockchain_memo: Blockchain memo for the transfer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v0/transfers/external-stablecoin-transfer",
            body=maybe_transform(
                {
                    "beneficiary_id": beneficiary_id,
                    "destination_currency": destination_currency,
                    "source_currency": source_currency,
                    "source_wallet_id": source_wallet_id,
                    "amount": amount,
                    "blockchain_memo": blockchain_memo,
                },
                transfer_create_external_stablecoin_transfer_params.TransferCreateExternalStablecoinTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_stablecoin_conversion(
        self,
        *,
        amount: float,
        destination_currency: str,
        source_currency: str,
        source_network: str,
        wallet_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a stablecoin conversion

        Args:
          amount: The amount to convert

          destination_currency: The destination currency

          source_currency: The source currency

          source_network: The source network

          wallet_id: The ID of the bridge wallet to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v0/transfers/stablecoin-conversion",
            body=maybe_transform(
                {
                    "amount": amount,
                    "destination_currency": destination_currency,
                    "source_currency": source_currency,
                    "source_network": source_network,
                    "wallet_id": wallet_id,
                },
                transfer_create_stablecoin_conversion_params.TransferCreateStablecoinConversionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTransfersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransfersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTransfersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransfersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#with_streaming_response
        """
        return AsyncTransfersResourceWithStreamingResponse(self)

    async def create_direct_bank(
        self,
        *,
        amount: float,
        destination_currency: str,
        payment_rail: str,
        source_currency: str,
        wallet_id: str,
        ach_reference: str | Omit = omit,
        sepa_reference: str | Omit = omit,
        wire_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a direct bank transfer

        Args:
          amount: The amount to transfer

          destination_currency: The destination currency

          payment_rail: The payment rail to use

          source_currency: The source currency

          wallet_id: The ID of the bridge wallet to transfer from

          ach_reference: ACH transfer reference

          sepa_reference: SEPA transfer reference

          wire_message: Wire transfer message

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v0/transfers/direct-bank",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "destination_currency": destination_currency,
                    "payment_rail": payment_rail,
                    "source_currency": source_currency,
                    "wallet_id": wallet_id,
                    "ach_reference": ach_reference,
                    "sepa_reference": sepa_reference,
                    "wire_message": wire_message,
                },
                transfer_create_direct_bank_params.TransferCreateDirectBankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_direct_wallet(
        self,
        *,
        amount: float,
        network: str,
        stable_coin_currency: str,
        wallet_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a direct wallet transfer

        Args:
          amount: The amount to transfer

          network: The network to use for the transfer

          stable_coin_currency: The stablecoin currency to use

          wallet_id: The ID of the bridge wallet to transfer from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v0/transfers/direct-wallet",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "network": network,
                    "stable_coin_currency": stable_coin_currency,
                    "wallet_id": wallet_id,
                },
                transfer_create_direct_wallet_params.TransferCreateDirectWalletParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_external_bank_transfer(
        self,
        *,
        destination_currency: str,
        destination_payment_rail: Literal["ach", "ach_push", "ach_same_day", "wire", "sepa", "swift", "spei"],
        external_account_id: str,
        source_currency: str,
        source_wallet_id: str,
        ach_reference: str | Omit = omit,
        amount: float | Omit = omit,
        sepa_reference: str | Omit = omit,
        spei_reference: str | Omit = omit,
        swift_charges: str | Omit = omit,
        swift_reference: str | Omit = omit,
        wire_message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create an external bank transfer

        Args:
          destination_currency: The destination currency

          destination_payment_rail: The destination payment rail (fiat payment method)

          external_account_id: The external account ID for the bank transfer

          source_currency: The source currency

          source_wallet_id: The ID of the source bridge wallet

          ach_reference: ACH reference message (1-10 characters, only for ACH transfers)

          amount: The amount to transfer

          sepa_reference: SEPA reference message (6-140 characters, only for SEPA transfers)

          spei_reference: SPEI reference message (1-40 characters, only for SPEI transfers)

          swift_charges: SWIFT charges bearer (only for SWIFT transfers)

          swift_reference: SWIFT reference message (1-190 characters, only for SWIFT transfers)

          wire_message: Wire transfer message (1-256 characters, only for wire transfers)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v0/transfers/external-bank-transfer",
            body=await async_maybe_transform(
                {
                    "destination_currency": destination_currency,
                    "destination_payment_rail": destination_payment_rail,
                    "external_account_id": external_account_id,
                    "source_currency": source_currency,
                    "source_wallet_id": source_wallet_id,
                    "ach_reference": ach_reference,
                    "amount": amount,
                    "sepa_reference": sepa_reference,
                    "spei_reference": spei_reference,
                    "swift_charges": swift_charges,
                    "swift_reference": swift_reference,
                    "wire_message": wire_message,
                },
                transfer_create_external_bank_transfer_params.TransferCreateExternalBankTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_external_stablecoin_transfer(
        self,
        *,
        beneficiary_id: str,
        destination_currency: str,
        source_currency: str,
        source_wallet_id: str,
        amount: float | Omit = omit,
        blockchain_memo: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create an external stablecoin transfer

        Args:
          beneficiary_id: Beneficiary ID for the stablecoin transfer

          destination_currency: The destination currency

          source_currency: The source currency

          source_wallet_id: The ID of the source bridge wallet

          amount: The amount to transfer

          blockchain_memo: Blockchain memo for the transfer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v0/transfers/external-stablecoin-transfer",
            body=await async_maybe_transform(
                {
                    "beneficiary_id": beneficiary_id,
                    "destination_currency": destination_currency,
                    "source_currency": source_currency,
                    "source_wallet_id": source_wallet_id,
                    "amount": amount,
                    "blockchain_memo": blockchain_memo,
                },
                transfer_create_external_stablecoin_transfer_params.TransferCreateExternalStablecoinTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_stablecoin_conversion(
        self,
        *,
        amount: float,
        destination_currency: str,
        source_currency: str,
        source_network: str,
        wallet_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a stablecoin conversion

        Args:
          amount: The amount to convert

          destination_currency: The destination currency

          source_currency: The source currency

          source_network: The source network

          wallet_id: The ID of the bridge wallet to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v0/transfers/stablecoin-conversion",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "destination_currency": destination_currency,
                    "source_currency": source_currency,
                    "source_network": source_network,
                    "wallet_id": wallet_id,
                },
                transfer_create_stablecoin_conversion_params.TransferCreateStablecoinConversionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TransfersResourceWithRawResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.create_direct_bank = to_raw_response_wrapper(
            transfers.create_direct_bank,
        )
        self.create_direct_wallet = to_raw_response_wrapper(
            transfers.create_direct_wallet,
        )
        self.create_external_bank_transfer = to_raw_response_wrapper(
            transfers.create_external_bank_transfer,
        )
        self.create_external_stablecoin_transfer = to_raw_response_wrapper(
            transfers.create_external_stablecoin_transfer,
        )
        self.create_stablecoin_conversion = to_raw_response_wrapper(
            transfers.create_stablecoin_conversion,
        )


class AsyncTransfersResourceWithRawResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.create_direct_bank = async_to_raw_response_wrapper(
            transfers.create_direct_bank,
        )
        self.create_direct_wallet = async_to_raw_response_wrapper(
            transfers.create_direct_wallet,
        )
        self.create_external_bank_transfer = async_to_raw_response_wrapper(
            transfers.create_external_bank_transfer,
        )
        self.create_external_stablecoin_transfer = async_to_raw_response_wrapper(
            transfers.create_external_stablecoin_transfer,
        )
        self.create_stablecoin_conversion = async_to_raw_response_wrapper(
            transfers.create_stablecoin_conversion,
        )


class TransfersResourceWithStreamingResponse:
    def __init__(self, transfers: TransfersResource) -> None:
        self._transfers = transfers

        self.create_direct_bank = to_streamed_response_wrapper(
            transfers.create_direct_bank,
        )
        self.create_direct_wallet = to_streamed_response_wrapper(
            transfers.create_direct_wallet,
        )
        self.create_external_bank_transfer = to_streamed_response_wrapper(
            transfers.create_external_bank_transfer,
        )
        self.create_external_stablecoin_transfer = to_streamed_response_wrapper(
            transfers.create_external_stablecoin_transfer,
        )
        self.create_stablecoin_conversion = to_streamed_response_wrapper(
            transfers.create_stablecoin_conversion,
        )


class AsyncTransfersResourceWithStreamingResponse:
    def __init__(self, transfers: AsyncTransfersResource) -> None:
        self._transfers = transfers

        self.create_direct_bank = async_to_streamed_response_wrapper(
            transfers.create_direct_bank,
        )
        self.create_direct_wallet = async_to_streamed_response_wrapper(
            transfers.create_direct_wallet,
        )
        self.create_external_bank_transfer = async_to_streamed_response_wrapper(
            transfers.create_external_bank_transfer,
        )
        self.create_external_stablecoin_transfer = async_to_streamed_response_wrapper(
            transfers.create_external_stablecoin_transfer,
        )
        self.create_stablecoin_conversion = async_to_streamed_response_wrapper(
            transfers.create_stablecoin_conversion,
        )
