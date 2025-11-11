# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .taxes import (
    TaxesResource,
    AsyncTaxesResource,
    TaxesResourceWithRawResponse,
    AsyncTaxesResourceWithRawResponse,
    TaxesResourceWithStreamingResponse,
    AsyncTaxesResourceWithStreamingResponse,
)
from .health import (
    HealthResource,
    AsyncHealthResource,
    HealthResourceWithRawResponse,
    AsyncHealthResourceWithRawResponse,
    HealthResourceWithStreamingResponse,
    AsyncHealthResourceWithStreamingResponse,
)
from .balance import (
    BalanceResource,
    AsyncBalanceResource,
    BalanceResourceWithRawResponse,
    AsyncBalanceResourceWithRawResponse,
    BalanceResourceWithStreamingResponse,
    AsyncBalanceResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .invoices import (
    InvoicesResource,
    AsyncInvoicesResource,
    InvoicesResourceWithRawResponse,
    AsyncInvoicesResourceWithRawResponse,
    InvoicesResourceWithStreamingResponse,
    AsyncInvoicesResourceWithStreamingResponse,
)
from .products import (
    ProductsResource,
    AsyncProductsResource,
    ProductsResourceWithRawResponse,
    AsyncProductsResourceWithRawResponse,
    ProductsResourceWithStreamingResponse,
    AsyncProductsResourceWithStreamingResponse,
)
from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .transfers import (
    TransfersResource,
    AsyncTransfersResource,
    TransfersResourceWithRawResponse,
    AsyncTransfersResourceWithRawResponse,
    TransfersResourceWithStreamingResponse,
    AsyncTransfersResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .test_payment import (
    TestPaymentResource,
    AsyncTestPaymentResource,
    TestPaymentResourceWithRawResponse,
    AsyncTestPaymentResourceWithRawResponse,
    TestPaymentResourceWithStreamingResponse,
    AsyncTestPaymentResourceWithStreamingResponse,
)
from .exchange_rate import (
    ExchangeRateResource,
    AsyncExchangeRateResource,
    ExchangeRateResourceWithRawResponse,
    AsyncExchangeRateResourceWithRawResponse,
    ExchangeRateResourceWithStreamingResponse,
    AsyncExchangeRateResourceWithStreamingResponse,
)
from .payment_links import (
    PaymentLinksResource,
    AsyncPaymentLinksResource,
    PaymentLinksResourceWithRawResponse,
    AsyncPaymentLinksResourceWithRawResponse,
    PaymentLinksResourceWithStreamingResponse,
    AsyncPaymentLinksResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .payment_intents import (
    PaymentIntentsResource,
    AsyncPaymentIntentsResource,
    PaymentIntentsResourceWithRawResponse,
    AsyncPaymentIntentsResourceWithRawResponse,
    PaymentIntentsResourceWithStreamingResponse,
    AsyncPaymentIntentsResourceWithStreamingResponse,
)
from .customers.customers import (
    CustomersResource,
    AsyncCustomersResource,
    CustomersResourceWithRawResponse,
    AsyncCustomersResourceWithRawResponse,
    CustomersResourceWithStreamingResponse,
    AsyncCustomersResourceWithStreamingResponse,
)

__all__ = ["V0Resource", "AsyncV0Resource"]


class V0Resource(SyncAPIResource):
    @cached_property
    def health(self) -> HealthResource:
        return HealthResource(self._client)

    @cached_property
    def test_payment(self) -> TestPaymentResource:
        return TestPaymentResource(self._client)

    @cached_property
    def customers(self) -> CustomersResource:
        return CustomersResource(self._client)

    @cached_property
    def payment_links(self) -> PaymentLinksResource:
        return PaymentLinksResource(self._client)

    @cached_property
    def payment_intents(self) -> PaymentIntentsResource:
        return PaymentIntentsResource(self._client)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        return WebhooksResource(self._client)

    @cached_property
    def transfers(self) -> TransfersResource:
        return TransfersResource(self._client)

    @cached_property
    def balance(self) -> BalanceResource:
        return BalanceResource(self._client)

    @cached_property
    def exchange_rate(self) -> ExchangeRateResource:
        return ExchangeRateResource(self._client)

    @cached_property
    def products(self) -> ProductsResource:
        return ProductsResource(self._client)

    @cached_property
    def invoices(self) -> InvoicesResource:
        return InvoicesResource(self._client)

    @cached_property
    def taxes(self) -> TaxesResource:
        return TaxesResource(self._client)

    @cached_property
    def with_raw_response(self) -> V0ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return V0ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V0ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#with_streaming_response
        """
        return V0ResourceWithStreamingResponse(self)

    def get_wallets(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get wallets for an app"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/v0/wallets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncV0Resource(AsyncAPIResource):
    @cached_property
    def health(self) -> AsyncHealthResource:
        return AsyncHealthResource(self._client)

    @cached_property
    def test_payment(self) -> AsyncTestPaymentResource:
        return AsyncTestPaymentResource(self._client)

    @cached_property
    def customers(self) -> AsyncCustomersResource:
        return AsyncCustomersResource(self._client)

    @cached_property
    def payment_links(self) -> AsyncPaymentLinksResource:
        return AsyncPaymentLinksResource(self._client)

    @cached_property
    def payment_intents(self) -> AsyncPaymentIntentsResource:
        return AsyncPaymentIntentsResource(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        return AsyncWebhooksResource(self._client)

    @cached_property
    def transfers(self) -> AsyncTransfersResource:
        return AsyncTransfersResource(self._client)

    @cached_property
    def balance(self) -> AsyncBalanceResource:
        return AsyncBalanceResource(self._client)

    @cached_property
    def exchange_rate(self) -> AsyncExchangeRateResource:
        return AsyncExchangeRateResource(self._client)

    @cached_property
    def products(self) -> AsyncProductsResource:
        return AsyncProductsResource(self._client)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        return AsyncInvoicesResource(self._client)

    @cached_property
    def taxes(self) -> AsyncTaxesResource:
        return AsyncTaxesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV0ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV0ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV0ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#with_streaming_response
        """
        return AsyncV0ResourceWithStreamingResponse(self)

    async def get_wallets(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Get wallets for an app"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/v0/wallets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class V0ResourceWithRawResponse:
    def __init__(self, v0: V0Resource) -> None:
        self._v0 = v0

        self.get_wallets = to_raw_response_wrapper(
            v0.get_wallets,
        )

    @cached_property
    def health(self) -> HealthResourceWithRawResponse:
        return HealthResourceWithRawResponse(self._v0.health)

    @cached_property
    def test_payment(self) -> TestPaymentResourceWithRawResponse:
        return TestPaymentResourceWithRawResponse(self._v0.test_payment)

    @cached_property
    def customers(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self._v0.customers)

    @cached_property
    def payment_links(self) -> PaymentLinksResourceWithRawResponse:
        return PaymentLinksResourceWithRawResponse(self._v0.payment_links)

    @cached_property
    def payment_intents(self) -> PaymentIntentsResourceWithRawResponse:
        return PaymentIntentsResourceWithRawResponse(self._v0.payment_intents)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self._v0.webhooks)

    @cached_property
    def transfers(self) -> TransfersResourceWithRawResponse:
        return TransfersResourceWithRawResponse(self._v0.transfers)

    @cached_property
    def balance(self) -> BalanceResourceWithRawResponse:
        return BalanceResourceWithRawResponse(self._v0.balance)

    @cached_property
    def exchange_rate(self) -> ExchangeRateResourceWithRawResponse:
        return ExchangeRateResourceWithRawResponse(self._v0.exchange_rate)

    @cached_property
    def products(self) -> ProductsResourceWithRawResponse:
        return ProductsResourceWithRawResponse(self._v0.products)

    @cached_property
    def invoices(self) -> InvoicesResourceWithRawResponse:
        return InvoicesResourceWithRawResponse(self._v0.invoices)

    @cached_property
    def taxes(self) -> TaxesResourceWithRawResponse:
        return TaxesResourceWithRawResponse(self._v0.taxes)


class AsyncV0ResourceWithRawResponse:
    def __init__(self, v0: AsyncV0Resource) -> None:
        self._v0 = v0

        self.get_wallets = async_to_raw_response_wrapper(
            v0.get_wallets,
        )

    @cached_property
    def health(self) -> AsyncHealthResourceWithRawResponse:
        return AsyncHealthResourceWithRawResponse(self._v0.health)

    @cached_property
    def test_payment(self) -> AsyncTestPaymentResourceWithRawResponse:
        return AsyncTestPaymentResourceWithRawResponse(self._v0.test_payment)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self._v0.customers)

    @cached_property
    def payment_links(self) -> AsyncPaymentLinksResourceWithRawResponse:
        return AsyncPaymentLinksResourceWithRawResponse(self._v0.payment_links)

    @cached_property
    def payment_intents(self) -> AsyncPaymentIntentsResourceWithRawResponse:
        return AsyncPaymentIntentsResourceWithRawResponse(self._v0.payment_intents)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self._v0.webhooks)

    @cached_property
    def transfers(self) -> AsyncTransfersResourceWithRawResponse:
        return AsyncTransfersResourceWithRawResponse(self._v0.transfers)

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithRawResponse:
        return AsyncBalanceResourceWithRawResponse(self._v0.balance)

    @cached_property
    def exchange_rate(self) -> AsyncExchangeRateResourceWithRawResponse:
        return AsyncExchangeRateResourceWithRawResponse(self._v0.exchange_rate)

    @cached_property
    def products(self) -> AsyncProductsResourceWithRawResponse:
        return AsyncProductsResourceWithRawResponse(self._v0.products)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithRawResponse:
        return AsyncInvoicesResourceWithRawResponse(self._v0.invoices)

    @cached_property
    def taxes(self) -> AsyncTaxesResourceWithRawResponse:
        return AsyncTaxesResourceWithRawResponse(self._v0.taxes)


class V0ResourceWithStreamingResponse:
    def __init__(self, v0: V0Resource) -> None:
        self._v0 = v0

        self.get_wallets = to_streamed_response_wrapper(
            v0.get_wallets,
        )

    @cached_property
    def health(self) -> HealthResourceWithStreamingResponse:
        return HealthResourceWithStreamingResponse(self._v0.health)

    @cached_property
    def test_payment(self) -> TestPaymentResourceWithStreamingResponse:
        return TestPaymentResourceWithStreamingResponse(self._v0.test_payment)

    @cached_property
    def customers(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self._v0.customers)

    @cached_property
    def payment_links(self) -> PaymentLinksResourceWithStreamingResponse:
        return PaymentLinksResourceWithStreamingResponse(self._v0.payment_links)

    @cached_property
    def payment_intents(self) -> PaymentIntentsResourceWithStreamingResponse:
        return PaymentIntentsResourceWithStreamingResponse(self._v0.payment_intents)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self._v0.webhooks)

    @cached_property
    def transfers(self) -> TransfersResourceWithStreamingResponse:
        return TransfersResourceWithStreamingResponse(self._v0.transfers)

    @cached_property
    def balance(self) -> BalanceResourceWithStreamingResponse:
        return BalanceResourceWithStreamingResponse(self._v0.balance)

    @cached_property
    def exchange_rate(self) -> ExchangeRateResourceWithStreamingResponse:
        return ExchangeRateResourceWithStreamingResponse(self._v0.exchange_rate)

    @cached_property
    def products(self) -> ProductsResourceWithStreamingResponse:
        return ProductsResourceWithStreamingResponse(self._v0.products)

    @cached_property
    def invoices(self) -> InvoicesResourceWithStreamingResponse:
        return InvoicesResourceWithStreamingResponse(self._v0.invoices)

    @cached_property
    def taxes(self) -> TaxesResourceWithStreamingResponse:
        return TaxesResourceWithStreamingResponse(self._v0.taxes)


class AsyncV0ResourceWithStreamingResponse:
    def __init__(self, v0: AsyncV0Resource) -> None:
        self._v0 = v0

        self.get_wallets = async_to_streamed_response_wrapper(
            v0.get_wallets,
        )

    @cached_property
    def health(self) -> AsyncHealthResourceWithStreamingResponse:
        return AsyncHealthResourceWithStreamingResponse(self._v0.health)

    @cached_property
    def test_payment(self) -> AsyncTestPaymentResourceWithStreamingResponse:
        return AsyncTestPaymentResourceWithStreamingResponse(self._v0.test_payment)

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self._v0.customers)

    @cached_property
    def payment_links(self) -> AsyncPaymentLinksResourceWithStreamingResponse:
        return AsyncPaymentLinksResourceWithStreamingResponse(self._v0.payment_links)

    @cached_property
    def payment_intents(self) -> AsyncPaymentIntentsResourceWithStreamingResponse:
        return AsyncPaymentIntentsResourceWithStreamingResponse(self._v0.payment_intents)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self._v0.webhooks)

    @cached_property
    def transfers(self) -> AsyncTransfersResourceWithStreamingResponse:
        return AsyncTransfersResourceWithStreamingResponse(self._v0.transfers)

    @cached_property
    def balance(self) -> AsyncBalanceResourceWithStreamingResponse:
        return AsyncBalanceResourceWithStreamingResponse(self._v0.balance)

    @cached_property
    def exchange_rate(self) -> AsyncExchangeRateResourceWithStreamingResponse:
        return AsyncExchangeRateResourceWithStreamingResponse(self._v0.exchange_rate)

    @cached_property
    def products(self) -> AsyncProductsResourceWithStreamingResponse:
        return AsyncProductsResourceWithStreamingResponse(self._v0.products)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithStreamingResponse:
        return AsyncInvoicesResourceWithStreamingResponse(self._v0.invoices)

    @cached_property
    def taxes(self) -> AsyncTaxesResourceWithStreamingResponse:
        return AsyncTaxesResourceWithStreamingResponse(self._v0.taxes)
