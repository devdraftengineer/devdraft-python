# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v0 import BridgePaymentRail
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v0.customers import liquidation_address_create_params
from ....types.v0.bridge_payment_rail import BridgePaymentRail
from ....types.v0.customers.liquidation_address_response import LiquidationAddressResponse
from ....types.v0.customers.liquidation_address_list_response import LiquidationAddressListResponse

__all__ = ["LiquidationAddressesResource", "AsyncLiquidationAddressesResource"]


class LiquidationAddressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LiquidationAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LiquidationAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiquidationAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#with_streaming_response
        """
        return LiquidationAddressesResourceWithStreamingResponse(self)

    def create(
        self,
        customer_id: str,
        *,
        address: str,
        chain: Literal[
            "ethereum", "solana", "polygon", "avalanche_c_chain", "base", "arbitrum", "optimism", "stellar", "tron"
        ],
        currency: Literal["usdc", "eurc", "dai", "pyusd", "usdt"],
        bridge_wallet_id: str | Omit = omit,
        custom_developer_fee_percent: str | Omit = omit,
        destination_ach_reference: str | Omit = omit,
        destination_address: str | Omit = omit,
        destination_blockchain_memo: str | Omit = omit,
        destination_currency: Literal["usd", "eur", "mxn", "usdc", "eurc", "dai", "pyusd", "usdt"] | Omit = omit,
        destination_payment_rail: BridgePaymentRail | Omit = omit,
        destination_sepa_reference: str | Omit = omit,
        destination_wire_message: str | Omit = omit,
        external_account_id: str | Omit = omit,
        prefunded_account_id: str | Omit = omit,
        return_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiquidationAddressResponse:
        """Create a new liquidation address for a customer.

        Liquidation addresses allow
              customers to automatically liquidate cryptocurrency holdings to fiat or other
              stablecoins based on configured parameters.

              **Required fields:**
              - chain: Blockchain network (ethereum, polygon, arbitrum, base)
              - currency: Stablecoin currency (usdc, eurc, dai, pyusd, usdt)
              - address: Valid blockchain address

              **At least one destination must be specified:**
              - external_account_id: External bank account
              - prefunded_account_id: Developer's prefunded account
              - bridge_wallet_id: Bridge wallet
              - destination_address: Crypto wallet address

              **Payment Rails:**
              Different payment rails have different requirements:
              - ACH: Requires external_account_id, supports destination_ach_reference
              - SEPA: Requires external_account_id, supports destination_sepa_reference
              - Wire: Requires external_account_id, supports destination_wire_message
              - Crypto: Requires destination_address, supports destination_blockchain_memo

        Args:
          address: The liquidation address on the blockchain

          chain: The blockchain chain for the liquidation address

          currency: The currency for the liquidation address

          bridge_wallet_id: Bridge Wallet to send funds to

          custom_developer_fee_percent: Custom developer fee percentage (Base 100 percentage: 10.2% = "10.2")

          destination_ach_reference: Reference for ACH transactions

          destination_address: Crypto wallet address for crypto transfers

          destination_blockchain_memo: Memo for blockchain transactions

          destination_currency: Currency for sending funds

          destination_payment_rail: The blockchain network where the source currency resides. Determines gas fees
              and transaction speed.

          destination_sepa_reference: Reference for SEPA transactions

          destination_wire_message: Message for wire transfers

          external_account_id: External bank account to send funds to

          prefunded_account_id: Developer's prefunded account id

          return_address: Address to return funds on failed transactions (Not supported on Stellar)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._post(
            f"/api/v0/customers/{customer_id}/liquidation_addresses",
            body=maybe_transform(
                {
                    "address": address,
                    "chain": chain,
                    "currency": currency,
                    "bridge_wallet_id": bridge_wallet_id,
                    "custom_developer_fee_percent": custom_developer_fee_percent,
                    "destination_ach_reference": destination_ach_reference,
                    "destination_address": destination_address,
                    "destination_blockchain_memo": destination_blockchain_memo,
                    "destination_currency": destination_currency,
                    "destination_payment_rail": destination_payment_rail,
                    "destination_sepa_reference": destination_sepa_reference,
                    "destination_wire_message": destination_wire_message,
                    "external_account_id": external_account_id,
                    "prefunded_account_id": prefunded_account_id,
                    "return_address": return_address,
                },
                liquidation_address_create_params.LiquidationAddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiquidationAddressResponse,
        )

    def retrieve(
        self,
        liquidation_address_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiquidationAddressResponse:
        """
        Retrieve a specific liquidation address by its ID for a given customer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not liquidation_address_id:
            raise ValueError(
                f"Expected a non-empty value for `liquidation_address_id` but received {liquidation_address_id!r}"
            )
        return self._get(
            f"/api/v0/customers/{customer_id}/liquidation_addresses/{liquidation_address_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiquidationAddressResponse,
        )

    def list(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiquidationAddressListResponse:
        """
        Retrieve all liquidation addresses associated with a specific customer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get(
            f"/api/v0/customers/{customer_id}/liquidation_addresses",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiquidationAddressListResponse,
        )


class AsyncLiquidationAddressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLiquidationAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLiquidationAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiquidationAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#with_streaming_response
        """
        return AsyncLiquidationAddressesResourceWithStreamingResponse(self)

    async def create(
        self,
        customer_id: str,
        *,
        address: str,
        chain: Literal[
            "ethereum", "solana", "polygon", "avalanche_c_chain", "base", "arbitrum", "optimism", "stellar", "tron"
        ],
        currency: Literal["usdc", "eurc", "dai", "pyusd", "usdt"],
        bridge_wallet_id: str | Omit = omit,
        custom_developer_fee_percent: str | Omit = omit,
        destination_ach_reference: str | Omit = omit,
        destination_address: str | Omit = omit,
        destination_blockchain_memo: str | Omit = omit,
        destination_currency: Literal["usd", "eur", "mxn", "usdc", "eurc", "dai", "pyusd", "usdt"] | Omit = omit,
        destination_payment_rail: BridgePaymentRail | Omit = omit,
        destination_sepa_reference: str | Omit = omit,
        destination_wire_message: str | Omit = omit,
        external_account_id: str | Omit = omit,
        prefunded_account_id: str | Omit = omit,
        return_address: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiquidationAddressResponse:
        """Create a new liquidation address for a customer.

        Liquidation addresses allow
              customers to automatically liquidate cryptocurrency holdings to fiat or other
              stablecoins based on configured parameters.

              **Required fields:**
              - chain: Blockchain network (ethereum, polygon, arbitrum, base)
              - currency: Stablecoin currency (usdc, eurc, dai, pyusd, usdt)
              - address: Valid blockchain address

              **At least one destination must be specified:**
              - external_account_id: External bank account
              - prefunded_account_id: Developer's prefunded account
              - bridge_wallet_id: Bridge wallet
              - destination_address: Crypto wallet address

              **Payment Rails:**
              Different payment rails have different requirements:
              - ACH: Requires external_account_id, supports destination_ach_reference
              - SEPA: Requires external_account_id, supports destination_sepa_reference
              - Wire: Requires external_account_id, supports destination_wire_message
              - Crypto: Requires destination_address, supports destination_blockchain_memo

        Args:
          address: The liquidation address on the blockchain

          chain: The blockchain chain for the liquidation address

          currency: The currency for the liquidation address

          bridge_wallet_id: Bridge Wallet to send funds to

          custom_developer_fee_percent: Custom developer fee percentage (Base 100 percentage: 10.2% = "10.2")

          destination_ach_reference: Reference for ACH transactions

          destination_address: Crypto wallet address for crypto transfers

          destination_blockchain_memo: Memo for blockchain transactions

          destination_currency: Currency for sending funds

          destination_payment_rail: The blockchain network where the source currency resides. Determines gas fees
              and transaction speed.

          destination_sepa_reference: Reference for SEPA transactions

          destination_wire_message: Message for wire transfers

          external_account_id: External bank account to send funds to

          prefunded_account_id: Developer's prefunded account id

          return_address: Address to return funds on failed transactions (Not supported on Stellar)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._post(
            f"/api/v0/customers/{customer_id}/liquidation_addresses",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "chain": chain,
                    "currency": currency,
                    "bridge_wallet_id": bridge_wallet_id,
                    "custom_developer_fee_percent": custom_developer_fee_percent,
                    "destination_ach_reference": destination_ach_reference,
                    "destination_address": destination_address,
                    "destination_blockchain_memo": destination_blockchain_memo,
                    "destination_currency": destination_currency,
                    "destination_payment_rail": destination_payment_rail,
                    "destination_sepa_reference": destination_sepa_reference,
                    "destination_wire_message": destination_wire_message,
                    "external_account_id": external_account_id,
                    "prefunded_account_id": prefunded_account_id,
                    "return_address": return_address,
                },
                liquidation_address_create_params.LiquidationAddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiquidationAddressResponse,
        )

    async def retrieve(
        self,
        liquidation_address_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiquidationAddressResponse:
        """
        Retrieve a specific liquidation address by its ID for a given customer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not liquidation_address_id:
            raise ValueError(
                f"Expected a non-empty value for `liquidation_address_id` but received {liquidation_address_id!r}"
            )
        return await self._get(
            f"/api/v0/customers/{customer_id}/liquidation_addresses/{liquidation_address_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiquidationAddressResponse,
        )

    async def list(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiquidationAddressListResponse:
        """
        Retrieve all liquidation addresses associated with a specific customer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._get(
            f"/api/v0/customers/{customer_id}/liquidation_addresses",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiquidationAddressListResponse,
        )


class LiquidationAddressesResourceWithRawResponse:
    def __init__(self, liquidation_addresses: LiquidationAddressesResource) -> None:
        self._liquidation_addresses = liquidation_addresses

        self.create = to_raw_response_wrapper(
            liquidation_addresses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            liquidation_addresses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            liquidation_addresses.list,
        )


class AsyncLiquidationAddressesResourceWithRawResponse:
    def __init__(self, liquidation_addresses: AsyncLiquidationAddressesResource) -> None:
        self._liquidation_addresses = liquidation_addresses

        self.create = async_to_raw_response_wrapper(
            liquidation_addresses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            liquidation_addresses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            liquidation_addresses.list,
        )


class LiquidationAddressesResourceWithStreamingResponse:
    def __init__(self, liquidation_addresses: LiquidationAddressesResource) -> None:
        self._liquidation_addresses = liquidation_addresses

        self.create = to_streamed_response_wrapper(
            liquidation_addresses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            liquidation_addresses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            liquidation_addresses.list,
        )


class AsyncLiquidationAddressesResourceWithStreamingResponse:
    def __init__(self, liquidation_addresses: AsyncLiquidationAddressesResource) -> None:
        self._liquidation_addresses = liquidation_addresses

        self.create = async_to_streamed_response_wrapper(
            liquidation_addresses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            liquidation_addresses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            liquidation_addresses.list,
        )
