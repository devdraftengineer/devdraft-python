# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v0.aggregated_balance import AggregatedBalance
from ...types.v0.balance_get_all_stablecoin_balances_response import BalanceGetAllStablecoinBalancesResponse

__all__ = ["BalanceResource", "AsyncBalanceResource"]


class BalanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BalanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return BalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#with_streaming_response
        """
        return BalanceResourceWithStreamingResponse(self)

    def get_all_stablecoin_balances(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BalanceGetAllStablecoinBalancesResponse:
        """
        Retrieves both USDC and EURC balances across all wallets for the specified app.

        This comprehensive endpoint provides:

        - Complete USDC balance aggregation with detailed breakdown
        - Complete EURC balance aggregation with detailed breakdown
        - Total USD equivalent value across both currencies
        - Individual wallet and chain-specific balance details

        ## Use Cases

        - Complete financial dashboard overview
        - Multi-currency balance reporting
        - Comprehensive wallet management
        - Cross-currency analytics and reporting

        ## Response Format

        The response includes separate aggregations for each currency plus a combined
        USD value estimate, providing complete visibility into stablecoin holdings.
        """
        return self._get(
            "/api/v0/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceGetAllStablecoinBalancesResponse,
        )

    def get_eurc(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AggregatedBalance:
        """
        Retrieves the total EURC balance across all wallets for the specified app.

        This endpoint aggregates EURC balances from all associated wallets and provides:

        - Total EURC balance across all chains and wallets
        - Detailed breakdown by individual wallet and blockchain network
        - Contract addresses and wallet identifiers for each balance

        ## Use Cases

        - Dashboard balance display
        - European market operations
        - Euro-denominated financial reporting
        - Cross-currency balance tracking

        ## Response Format

        The response includes both the aggregated total and detailed breakdown, enabling
        comprehensive euro stablecoin balance management.
        """
        return self._get(
            "/api/v0/balance/eurc",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AggregatedBalance,
        )

    def get_usdc(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AggregatedBalance:
        """
        Retrieves the total USDC balance across all wallets for the specified app.

        This endpoint aggregates USDC balances from all associated wallets and provides:

        - Total USDC balance across all chains and wallets
        - Detailed breakdown by individual wallet and blockchain network
        - Contract addresses and wallet identifiers for each balance

        ## Use Cases

        - Dashboard balance display
        - Financial reporting and reconciliation
        - Real-time balance monitoring
        - Multi-chain balance aggregation

        ## Response Format

        The response includes both the aggregated total and detailed breakdown, allowing
        for comprehensive balance tracking and wallet-specific analysis.
        """
        return self._get(
            "/api/v0/balance/usdc",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AggregatedBalance,
        )


class AsyncBalanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBalanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBalanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#with_streaming_response
        """
        return AsyncBalanceResourceWithStreamingResponse(self)

    async def get_all_stablecoin_balances(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BalanceGetAllStablecoinBalancesResponse:
        """
        Retrieves both USDC and EURC balances across all wallets for the specified app.

        This comprehensive endpoint provides:

        - Complete USDC balance aggregation with detailed breakdown
        - Complete EURC balance aggregation with detailed breakdown
        - Total USD equivalent value across both currencies
        - Individual wallet and chain-specific balance details

        ## Use Cases

        - Complete financial dashboard overview
        - Multi-currency balance reporting
        - Comprehensive wallet management
        - Cross-currency analytics and reporting

        ## Response Format

        The response includes separate aggregations for each currency plus a combined
        USD value estimate, providing complete visibility into stablecoin holdings.
        """
        return await self._get(
            "/api/v0/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BalanceGetAllStablecoinBalancesResponse,
        )

    async def get_eurc(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AggregatedBalance:
        """
        Retrieves the total EURC balance across all wallets for the specified app.

        This endpoint aggregates EURC balances from all associated wallets and provides:

        - Total EURC balance across all chains and wallets
        - Detailed breakdown by individual wallet and blockchain network
        - Contract addresses and wallet identifiers for each balance

        ## Use Cases

        - Dashboard balance display
        - European market operations
        - Euro-denominated financial reporting
        - Cross-currency balance tracking

        ## Response Format

        The response includes both the aggregated total and detailed breakdown, enabling
        comprehensive euro stablecoin balance management.
        """
        return await self._get(
            "/api/v0/balance/eurc",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AggregatedBalance,
        )

    async def get_usdc(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AggregatedBalance:
        """
        Retrieves the total USDC balance across all wallets for the specified app.

        This endpoint aggregates USDC balances from all associated wallets and provides:

        - Total USDC balance across all chains and wallets
        - Detailed breakdown by individual wallet and blockchain network
        - Contract addresses and wallet identifiers for each balance

        ## Use Cases

        - Dashboard balance display
        - Financial reporting and reconciliation
        - Real-time balance monitoring
        - Multi-chain balance aggregation

        ## Response Format

        The response includes both the aggregated total and detailed breakdown, allowing
        for comprehensive balance tracking and wallet-specific analysis.
        """
        return await self._get(
            "/api/v0/balance/usdc",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AggregatedBalance,
        )


class BalanceResourceWithRawResponse:
    def __init__(self, balance: BalanceResource) -> None:
        self._balance = balance

        self.get_all_stablecoin_balances = to_raw_response_wrapper(
            balance.get_all_stablecoin_balances,
        )
        self.get_eurc = to_raw_response_wrapper(
            balance.get_eurc,
        )
        self.get_usdc = to_raw_response_wrapper(
            balance.get_usdc,
        )


class AsyncBalanceResourceWithRawResponse:
    def __init__(self, balance: AsyncBalanceResource) -> None:
        self._balance = balance

        self.get_all_stablecoin_balances = async_to_raw_response_wrapper(
            balance.get_all_stablecoin_balances,
        )
        self.get_eurc = async_to_raw_response_wrapper(
            balance.get_eurc,
        )
        self.get_usdc = async_to_raw_response_wrapper(
            balance.get_usdc,
        )


class BalanceResourceWithStreamingResponse:
    def __init__(self, balance: BalanceResource) -> None:
        self._balance = balance

        self.get_all_stablecoin_balances = to_streamed_response_wrapper(
            balance.get_all_stablecoin_balances,
        )
        self.get_eurc = to_streamed_response_wrapper(
            balance.get_eurc,
        )
        self.get_usdc = to_streamed_response_wrapper(
            balance.get_usdc,
        )


class AsyncBalanceResourceWithStreamingResponse:
    def __init__(self, balance: AsyncBalanceResource) -> None:
        self._balance = balance

        self.get_all_stablecoin_balances = async_to_streamed_response_wrapper(
            balance.get_all_stablecoin_balances,
        )
        self.get_eurc = async_to_streamed_response_wrapper(
            balance.get_eurc,
        )
        self.get_usdc = async_to_streamed_response_wrapper(
            balance.get_usdc,
        )
