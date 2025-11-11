# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v0 import exchange_rate_get_exchange_rate_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v0.exchange_rate_response import ExchangeRateResponse

__all__ = ["ExchangeRateResource", "AsyncExchangeRateResource"]


class ExchangeRateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExchangeRateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ExchangeRateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExchangeRateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#with_streaming_response
        """
        return ExchangeRateResourceWithStreamingResponse(self)

    def get_eur_to_usd(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeRateResponse:
        """
        Retrieves the current exchange rate for converting EUR to USD (EURC to USDC).

        This endpoint provides real-time exchange rate information for stablecoin
        conversions:

        - Mid-market rate for reference pricing
        - Buy rate for actual conversion calculations
        - Sell rate for reverse conversion scenarios

        ## Use Cases

        - Display current exchange rates in dashboards
        - Calculate conversion amounts for EURC to USDC transfers
        - Financial reporting and analytics
        - Real-time pricing for multi-currency operations

        ## Rate Information

        - **Mid-market rate**: The theoretical middle rate between buy and sell
        - **Buy rate**: Rate used when converting FROM EUR TO USD (what you get)
        - **Sell rate**: Rate used when converting FROM USD TO EUR (what you pay)

        The rates are updated in real-time and reflect current market conditions.
        """
        return self._get(
            "/api/v0/exchange-rate/eur-to-usd",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeRateResponse,
        )

    def get_exchange_rate(
        self,
        *,
        from_: str,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeRateResponse:
        """
        Retrieves the current exchange rate between two specified currencies.

        This flexible endpoint allows you to get exchange rates for any supported
        currency pair:

        - Supports USD and EUR currency codes
        - Provides comprehensive rate information
        - Real-time market data

        ## Supported Currency Pairs

        - USD to EUR (USDC to EURC)
        - EUR to USD (EURC to USDC)

        ## Query Parameters

        - **from**: Source currency code (usd, eur)
        - **to**: Target currency code (usd, eur)

        ## Use Cases

        - Flexible exchange rate queries
        - Multi-currency application support
        - Dynamic currency conversion calculations
        - Financial analytics and reporting

        ## Rate Information

        All rates are provided with full market context including mid-market, buy, and
        sell rates.

        Args:
          from_: Source currency code (e.g., usd)

          to: Target currency code (e.g., eur)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v0/exchange-rate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    exchange_rate_get_exchange_rate_params.ExchangeRateGetExchangeRateParams,
                ),
            ),
            cast_to=ExchangeRateResponse,
        )

    def get_usd_to_eur(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeRateResponse:
        """
        Retrieves the current exchange rate for converting USD to EUR (USDC to EURC).

        This endpoint provides real-time exchange rate information for stablecoin
        conversions:

        - Mid-market rate for reference pricing
        - Buy rate for actual conversion calculations
        - Sell rate for reverse conversion scenarios

        ## Use Cases

        - Display current exchange rates in dashboards
        - Calculate conversion amounts for USDC to EURC transfers
        - Financial reporting and analytics
        - Real-time pricing for multi-currency operations

        ## Rate Information

        - **Mid-market rate**: The theoretical middle rate between buy and sell
        - **Buy rate**: Rate used when converting FROM USD TO EUR (what you get)
        - **Sell rate**: Rate used when converting FROM EUR TO USD (what you pay)

        The rates are updated in real-time and reflect current market conditions.
        """
        return self._get(
            "/api/v0/exchange-rate/usd-to-eur",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeRateResponse,
        )


class AsyncExchangeRateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExchangeRateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncExchangeRateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExchangeRateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#with_streaming_response
        """
        return AsyncExchangeRateResourceWithStreamingResponse(self)

    async def get_eur_to_usd(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeRateResponse:
        """
        Retrieves the current exchange rate for converting EUR to USD (EURC to USDC).

        This endpoint provides real-time exchange rate information for stablecoin
        conversions:

        - Mid-market rate for reference pricing
        - Buy rate for actual conversion calculations
        - Sell rate for reverse conversion scenarios

        ## Use Cases

        - Display current exchange rates in dashboards
        - Calculate conversion amounts for EURC to USDC transfers
        - Financial reporting and analytics
        - Real-time pricing for multi-currency operations

        ## Rate Information

        - **Mid-market rate**: The theoretical middle rate between buy and sell
        - **Buy rate**: Rate used when converting FROM EUR TO USD (what you get)
        - **Sell rate**: Rate used when converting FROM USD TO EUR (what you pay)

        The rates are updated in real-time and reflect current market conditions.
        """
        return await self._get(
            "/api/v0/exchange-rate/eur-to-usd",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeRateResponse,
        )

    async def get_exchange_rate(
        self,
        *,
        from_: str,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeRateResponse:
        """
        Retrieves the current exchange rate between two specified currencies.

        This flexible endpoint allows you to get exchange rates for any supported
        currency pair:

        - Supports USD and EUR currency codes
        - Provides comprehensive rate information
        - Real-time market data

        ## Supported Currency Pairs

        - USD to EUR (USDC to EURC)
        - EUR to USD (EURC to USDC)

        ## Query Parameters

        - **from**: Source currency code (usd, eur)
        - **to**: Target currency code (usd, eur)

        ## Use Cases

        - Flexible exchange rate queries
        - Multi-currency application support
        - Dynamic currency conversion calculations
        - Financial analytics and reporting

        ## Rate Information

        All rates are provided with full market context including mid-market, buy, and
        sell rates.

        Args:
          from_: Source currency code (e.g., usd)

          to: Target currency code (e.g., eur)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v0/exchange-rate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    exchange_rate_get_exchange_rate_params.ExchangeRateGetExchangeRateParams,
                ),
            ),
            cast_to=ExchangeRateResponse,
        )

    async def get_usd_to_eur(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeRateResponse:
        """
        Retrieves the current exchange rate for converting USD to EUR (USDC to EURC).

        This endpoint provides real-time exchange rate information for stablecoin
        conversions:

        - Mid-market rate for reference pricing
        - Buy rate for actual conversion calculations
        - Sell rate for reverse conversion scenarios

        ## Use Cases

        - Display current exchange rates in dashboards
        - Calculate conversion amounts for USDC to EURC transfers
        - Financial reporting and analytics
        - Real-time pricing for multi-currency operations

        ## Rate Information

        - **Mid-market rate**: The theoretical middle rate between buy and sell
        - **Buy rate**: Rate used when converting FROM USD TO EUR (what you get)
        - **Sell rate**: Rate used when converting FROM EUR TO USD (what you pay)

        The rates are updated in real-time and reflect current market conditions.
        """
        return await self._get(
            "/api/v0/exchange-rate/usd-to-eur",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeRateResponse,
        )


class ExchangeRateResourceWithRawResponse:
    def __init__(self, exchange_rate: ExchangeRateResource) -> None:
        self._exchange_rate = exchange_rate

        self.get_eur_to_usd = to_raw_response_wrapper(
            exchange_rate.get_eur_to_usd,
        )
        self.get_exchange_rate = to_raw_response_wrapper(
            exchange_rate.get_exchange_rate,
        )
        self.get_usd_to_eur = to_raw_response_wrapper(
            exchange_rate.get_usd_to_eur,
        )


class AsyncExchangeRateResourceWithRawResponse:
    def __init__(self, exchange_rate: AsyncExchangeRateResource) -> None:
        self._exchange_rate = exchange_rate

        self.get_eur_to_usd = async_to_raw_response_wrapper(
            exchange_rate.get_eur_to_usd,
        )
        self.get_exchange_rate = async_to_raw_response_wrapper(
            exchange_rate.get_exchange_rate,
        )
        self.get_usd_to_eur = async_to_raw_response_wrapper(
            exchange_rate.get_usd_to_eur,
        )


class ExchangeRateResourceWithStreamingResponse:
    def __init__(self, exchange_rate: ExchangeRateResource) -> None:
        self._exchange_rate = exchange_rate

        self.get_eur_to_usd = to_streamed_response_wrapper(
            exchange_rate.get_eur_to_usd,
        )
        self.get_exchange_rate = to_streamed_response_wrapper(
            exchange_rate.get_exchange_rate,
        )
        self.get_usd_to_eur = to_streamed_response_wrapper(
            exchange_rate.get_usd_to_eur,
        )


class AsyncExchangeRateResourceWithStreamingResponse:
    def __init__(self, exchange_rate: AsyncExchangeRateResource) -> None:
        self._exchange_rate = exchange_rate

        self.get_eur_to_usd = async_to_streamed_response_wrapper(
            exchange_rate.get_eur_to_usd,
        )
        self.get_exchange_rate = async_to_streamed_response_wrapper(
            exchange_rate.get_exchange_rate,
        )
        self.get_usd_to_eur = async_to_streamed_response_wrapper(
            exchange_rate.get_usd_to_eur,
        )
