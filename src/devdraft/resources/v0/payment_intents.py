# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v0 import (
    BridgePaymentRail,
    StableCoinCurrency,
    payment_intent_create_bank_params,
    payment_intent_create_stable_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v0.bridge_payment_rail import BridgePaymentRail
from ...types.v0.stable_coin_currency import StableCoinCurrency

__all__ = ["PaymentIntentsResource", "AsyncPaymentIntentsResource"]


class PaymentIntentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentIntentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PaymentIntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentIntentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#with_streaming_response
        """
        return PaymentIntentsResourceWithStreamingResponse(self)

    def create_bank(
        self,
        *,
        destination_currency: StableCoinCurrency,
        destination_network: BridgePaymentRail,
        source_currency: Literal["usd", "eur", "mxn"],
        source_payment_rail: BridgePaymentRail,
        ach_reference: str | Omit = omit,
        amount: str | Omit = omit,
        customer_address: str | Omit = omit,
        customer_country: str | Omit = omit,
        customer_country_iso: str | Omit = omit,
        customer_email: str | Omit = omit,
        customer_first_name: str | Omit = omit,
        customer_last_name: str | Omit = omit,
        customer_province: str | Omit = omit,
        customer_province_iso: str | Omit = omit,
        destination_address: str | Omit = omit,
        phone_number: str | Omit = omit,
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
        Creates a new bank payment intent for fiat-to-stablecoin transfers.

        This endpoint allows you to create payment intents for bank transfers (ACH,
        Wire, SEPA) that convert to stablecoins. Perfect for onboarding users from
        traditional banking to crypto.

        ## Supported Payment Rails

        - **ACH_PUSH**: US bank transfers (same-day or standard)
        - **WIRE**: International wire transfers
        - **SEPA**: European bank transfers

        ## Use Cases

        - USD bank account to USDC conversion
        - EUR bank account to EURC conversion
        - MXN bank account to stablecoin conversion
        - Flexible amount payment intents for variable pricing

        ## Supported Source Currencies

        - **USD**: US Dollar
        - **EUR**: Euro
        - **MXN**: Mexican Peso

        ## Example: USD Bank to USDC

        ```json
        {
          "sourcePaymentRail": "ach_push",
          "sourceCurrency": "usd",
          "destinationCurrency": "usdc",
          "destinationNetwork": "ethereum",
          "destinationAddress": "0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1",
          "amount": "1000.00",
          "customer_first_name": "John",
          "customer_last_name": "Doe",
          "customer_email": "john.doe@example.com",
          "ach_reference": "INV12345"
        }
        ```

        ## Reference Fields

        Use appropriate reference fields based on the payment rail:

        - `ach_reference`: For ACH transfers (max 10 chars, alphanumeric + spaces)
        - `wire_message`: For wire transfers (max 256 chars)
        - `sepa_reference`: For SEPA transfers (6-140 chars, specific character set)

        ## Idempotency

        Include an `idempotency-key` header with a unique UUID v4 to prevent duplicate
        payments. Subsequent requests with the same key will return the original
        response.

        Args:
          destination_currency: The stablecoin currency to convert FROM. This is the currency the customer will
              pay with.

          destination_network: The blockchain network where the source currency resides. Determines gas fees
              and transaction speed.

          source_currency: The fiat currency to convert FROM. Must match the currency of the source payment
              rail.

          source_payment_rail: The blockchain network where the source currency resides. Determines gas fees
              and transaction speed.

          ach_reference: ACH reference (for ACH transfers)

          amount: Payment amount (optional for flexible amount)

          customer_address: Customer address

          customer_country: Customer country

          customer_country_iso: Customer country ISO code

          customer_email: Customer email address

          customer_first_name: Customer first name

          customer_last_name: Customer last name

          customer_province: Customer province/state

          customer_province_iso: Customer province/state ISO code

          destination_address: Destination wallet address. Supports Ethereum (0x...) and Solana address
              formats.

          phone_number: Customer phone number

          sepa_reference: SEPA reference (for SEPA transfers)

          wire_message: Wire transfer message (for WIRE transfers)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v0/payment-intents/bank",
            body=maybe_transform(
                {
                    "destination_currency": destination_currency,
                    "destination_network": destination_network,
                    "source_currency": source_currency,
                    "source_payment_rail": source_payment_rail,
                    "ach_reference": ach_reference,
                    "amount": amount,
                    "customer_address": customer_address,
                    "customer_country": customer_country,
                    "customer_country_iso": customer_country_iso,
                    "customer_email": customer_email,
                    "customer_first_name": customer_first_name,
                    "customer_last_name": customer_last_name,
                    "customer_province": customer_province,
                    "customer_province_iso": customer_province_iso,
                    "destination_address": destination_address,
                    "phone_number": phone_number,
                    "sepa_reference": sepa_reference,
                    "wire_message": wire_message,
                },
                payment_intent_create_bank_params.PaymentIntentCreateBankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_stable(
        self,
        *,
        destination_network: BridgePaymentRail,
        source_currency: StableCoinCurrency,
        source_network: BridgePaymentRail,
        amount: str | Omit = omit,
        customer_address: str | Omit = omit,
        customer_country: str | Omit = omit,
        customer_country_iso: str | Omit = omit,
        customer_email: str | Omit = omit,
        customer_first_name: str | Omit = omit,
        customer_last_name: str | Omit = omit,
        customer_province: str | Omit = omit,
        customer_province_iso: str | Omit = omit,
        destination_address: str | Omit = omit,
        destination_currency: StableCoinCurrency | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Creates a new stable payment intent for stablecoin-to-stablecoin transfers.

        This endpoint allows you to create payment intents for transfers between
        different stablecoins and networks. Perfect for cross-chain stablecoin swaps and
        conversions.

        ## Use Cases

        - USDC to EURC conversions
        - Cross-chain stablecoin transfers (e.g., Ethereum USDC to Polygon USDC)
        - Flexible amount payment intents for dynamic pricing

        ## Example: USDC to EURC Conversion

        ```json
        {
          "sourceCurrency": "usdc",
          "sourceNetwork": "ethereum",
          "destinationCurrency": "eurc",
          "destinationNetwork": "polygon",
          "destinationAddress": "0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1",
          "amount": "100.00",
          "customer_first_name": "John",
          "customer_last_name": "Doe",
          "customer_email": "john.doe@example.com"
        }
        ```

        ## Flexible Amount Payments

        Omit the `amount` field to create a flexible payment intent where users can
        specify the amount during payment.

        ## Idempotency

        Include an `idempotency-key` header with a unique UUID v4 to prevent duplicate
        payments. Subsequent requests with the same key will return the original
        response.

        Args:
          destination_network: The blockchain network where the source currency resides. Determines gas fees
              and transaction speed.

          source_currency: The stablecoin currency to convert FROM. This is the currency the customer will
              pay with.

          source_network: The blockchain network where the source currency resides. Determines gas fees
              and transaction speed.

          amount: Payment amount in the source currency. Omit for flexible amount payments where
              users specify the amount during checkout.

          customer_address: Customer's full address. Required for compliance in certain jurisdictions and
              high-value transactions.

          customer_country: Customer's country of residence. Used for compliance and tax reporting.

          customer_country_iso: Customer's country ISO 3166-1 alpha-2 code. Used for automated compliance
              checks.

          customer_email: Customer's email address. Used for transaction notifications and receipts.
              Highly recommended for all transactions.

          customer_first_name: Customer's first name. Used for transaction records and compliance. Required for
              amounts over $1000.

          customer_last_name: Customer's last name. Used for transaction records and compliance. Required for
              amounts over $1000.

          customer_province: Customer's state or province. Required for US and Canadian customers.

          customer_province_iso: Customer's state or province ISO code. Used for automated tax calculations.

          destination_address: The wallet address where converted funds will be sent. Supports Ethereum (0x...)
              and Solana address formats.

          destination_currency: The stablecoin currency to convert FROM. This is the currency the customer will
              pay with.

          phone_number: Customer's phone number with country code. Used for SMS notifications and
              verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v0/payment-intents/stablecoin",
            body=maybe_transform(
                {
                    "destination_network": destination_network,
                    "source_currency": source_currency,
                    "source_network": source_network,
                    "amount": amount,
                    "customer_address": customer_address,
                    "customer_country": customer_country,
                    "customer_country_iso": customer_country_iso,
                    "customer_email": customer_email,
                    "customer_first_name": customer_first_name,
                    "customer_last_name": customer_last_name,
                    "customer_province": customer_province,
                    "customer_province_iso": customer_province_iso,
                    "destination_address": destination_address,
                    "destination_currency": destination_currency,
                    "phone_number": phone_number,
                },
                payment_intent_create_stable_params.PaymentIntentCreateStableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPaymentIntentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentIntentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentIntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentIntentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#with_streaming_response
        """
        return AsyncPaymentIntentsResourceWithStreamingResponse(self)

    async def create_bank(
        self,
        *,
        destination_currency: StableCoinCurrency,
        destination_network: BridgePaymentRail,
        source_currency: Literal["usd", "eur", "mxn"],
        source_payment_rail: BridgePaymentRail,
        ach_reference: str | Omit = omit,
        amount: str | Omit = omit,
        customer_address: str | Omit = omit,
        customer_country: str | Omit = omit,
        customer_country_iso: str | Omit = omit,
        customer_email: str | Omit = omit,
        customer_first_name: str | Omit = omit,
        customer_last_name: str | Omit = omit,
        customer_province: str | Omit = omit,
        customer_province_iso: str | Omit = omit,
        destination_address: str | Omit = omit,
        phone_number: str | Omit = omit,
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
        Creates a new bank payment intent for fiat-to-stablecoin transfers.

        This endpoint allows you to create payment intents for bank transfers (ACH,
        Wire, SEPA) that convert to stablecoins. Perfect for onboarding users from
        traditional banking to crypto.

        ## Supported Payment Rails

        - **ACH_PUSH**: US bank transfers (same-day or standard)
        - **WIRE**: International wire transfers
        - **SEPA**: European bank transfers

        ## Use Cases

        - USD bank account to USDC conversion
        - EUR bank account to EURC conversion
        - MXN bank account to stablecoin conversion
        - Flexible amount payment intents for variable pricing

        ## Supported Source Currencies

        - **USD**: US Dollar
        - **EUR**: Euro
        - **MXN**: Mexican Peso

        ## Example: USD Bank to USDC

        ```json
        {
          "sourcePaymentRail": "ach_push",
          "sourceCurrency": "usd",
          "destinationCurrency": "usdc",
          "destinationNetwork": "ethereum",
          "destinationAddress": "0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1",
          "amount": "1000.00",
          "customer_first_name": "John",
          "customer_last_name": "Doe",
          "customer_email": "john.doe@example.com",
          "ach_reference": "INV12345"
        }
        ```

        ## Reference Fields

        Use appropriate reference fields based on the payment rail:

        - `ach_reference`: For ACH transfers (max 10 chars, alphanumeric + spaces)
        - `wire_message`: For wire transfers (max 256 chars)
        - `sepa_reference`: For SEPA transfers (6-140 chars, specific character set)

        ## Idempotency

        Include an `idempotency-key` header with a unique UUID v4 to prevent duplicate
        payments. Subsequent requests with the same key will return the original
        response.

        Args:
          destination_currency: The stablecoin currency to convert FROM. This is the currency the customer will
              pay with.

          destination_network: The blockchain network where the source currency resides. Determines gas fees
              and transaction speed.

          source_currency: The fiat currency to convert FROM. Must match the currency of the source payment
              rail.

          source_payment_rail: The blockchain network where the source currency resides. Determines gas fees
              and transaction speed.

          ach_reference: ACH reference (for ACH transfers)

          amount: Payment amount (optional for flexible amount)

          customer_address: Customer address

          customer_country: Customer country

          customer_country_iso: Customer country ISO code

          customer_email: Customer email address

          customer_first_name: Customer first name

          customer_last_name: Customer last name

          customer_province: Customer province/state

          customer_province_iso: Customer province/state ISO code

          destination_address: Destination wallet address. Supports Ethereum (0x...) and Solana address
              formats.

          phone_number: Customer phone number

          sepa_reference: SEPA reference (for SEPA transfers)

          wire_message: Wire transfer message (for WIRE transfers)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v0/payment-intents/bank",
            body=await async_maybe_transform(
                {
                    "destination_currency": destination_currency,
                    "destination_network": destination_network,
                    "source_currency": source_currency,
                    "source_payment_rail": source_payment_rail,
                    "ach_reference": ach_reference,
                    "amount": amount,
                    "customer_address": customer_address,
                    "customer_country": customer_country,
                    "customer_country_iso": customer_country_iso,
                    "customer_email": customer_email,
                    "customer_first_name": customer_first_name,
                    "customer_last_name": customer_last_name,
                    "customer_province": customer_province,
                    "customer_province_iso": customer_province_iso,
                    "destination_address": destination_address,
                    "phone_number": phone_number,
                    "sepa_reference": sepa_reference,
                    "wire_message": wire_message,
                },
                payment_intent_create_bank_params.PaymentIntentCreateBankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_stable(
        self,
        *,
        destination_network: BridgePaymentRail,
        source_currency: StableCoinCurrency,
        source_network: BridgePaymentRail,
        amount: str | Omit = omit,
        customer_address: str | Omit = omit,
        customer_country: str | Omit = omit,
        customer_country_iso: str | Omit = omit,
        customer_email: str | Omit = omit,
        customer_first_name: str | Omit = omit,
        customer_last_name: str | Omit = omit,
        customer_province: str | Omit = omit,
        customer_province_iso: str | Omit = omit,
        destination_address: str | Omit = omit,
        destination_currency: StableCoinCurrency | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Creates a new stable payment intent for stablecoin-to-stablecoin transfers.

        This endpoint allows you to create payment intents for transfers between
        different stablecoins and networks. Perfect for cross-chain stablecoin swaps and
        conversions.

        ## Use Cases

        - USDC to EURC conversions
        - Cross-chain stablecoin transfers (e.g., Ethereum USDC to Polygon USDC)
        - Flexible amount payment intents for dynamic pricing

        ## Example: USDC to EURC Conversion

        ```json
        {
          "sourceCurrency": "usdc",
          "sourceNetwork": "ethereum",
          "destinationCurrency": "eurc",
          "destinationNetwork": "polygon",
          "destinationAddress": "0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1",
          "amount": "100.00",
          "customer_first_name": "John",
          "customer_last_name": "Doe",
          "customer_email": "john.doe@example.com"
        }
        ```

        ## Flexible Amount Payments

        Omit the `amount` field to create a flexible payment intent where users can
        specify the amount during payment.

        ## Idempotency

        Include an `idempotency-key` header with a unique UUID v4 to prevent duplicate
        payments. Subsequent requests with the same key will return the original
        response.

        Args:
          destination_network: The blockchain network where the source currency resides. Determines gas fees
              and transaction speed.

          source_currency: The stablecoin currency to convert FROM. This is the currency the customer will
              pay with.

          source_network: The blockchain network where the source currency resides. Determines gas fees
              and transaction speed.

          amount: Payment amount in the source currency. Omit for flexible amount payments where
              users specify the amount during checkout.

          customer_address: Customer's full address. Required for compliance in certain jurisdictions and
              high-value transactions.

          customer_country: Customer's country of residence. Used for compliance and tax reporting.

          customer_country_iso: Customer's country ISO 3166-1 alpha-2 code. Used for automated compliance
              checks.

          customer_email: Customer's email address. Used for transaction notifications and receipts.
              Highly recommended for all transactions.

          customer_first_name: Customer's first name. Used for transaction records and compliance. Required for
              amounts over $1000.

          customer_last_name: Customer's last name. Used for transaction records and compliance. Required for
              amounts over $1000.

          customer_province: Customer's state or province. Required for US and Canadian customers.

          customer_province_iso: Customer's state or province ISO code. Used for automated tax calculations.

          destination_address: The wallet address where converted funds will be sent. Supports Ethereum (0x...)
              and Solana address formats.

          destination_currency: The stablecoin currency to convert FROM. This is the currency the customer will
              pay with.

          phone_number: Customer's phone number with country code. Used for SMS notifications and
              verification.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v0/payment-intents/stablecoin",
            body=await async_maybe_transform(
                {
                    "destination_network": destination_network,
                    "source_currency": source_currency,
                    "source_network": source_network,
                    "amount": amount,
                    "customer_address": customer_address,
                    "customer_country": customer_country,
                    "customer_country_iso": customer_country_iso,
                    "customer_email": customer_email,
                    "customer_first_name": customer_first_name,
                    "customer_last_name": customer_last_name,
                    "customer_province": customer_province,
                    "customer_province_iso": customer_province_iso,
                    "destination_address": destination_address,
                    "destination_currency": destination_currency,
                    "phone_number": phone_number,
                },
                payment_intent_create_stable_params.PaymentIntentCreateStableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PaymentIntentsResourceWithRawResponse:
    def __init__(self, payment_intents: PaymentIntentsResource) -> None:
        self._payment_intents = payment_intents

        self.create_bank = to_raw_response_wrapper(
            payment_intents.create_bank,
        )
        self.create_stable = to_raw_response_wrapper(
            payment_intents.create_stable,
        )


class AsyncPaymentIntentsResourceWithRawResponse:
    def __init__(self, payment_intents: AsyncPaymentIntentsResource) -> None:
        self._payment_intents = payment_intents

        self.create_bank = async_to_raw_response_wrapper(
            payment_intents.create_bank,
        )
        self.create_stable = async_to_raw_response_wrapper(
            payment_intents.create_stable,
        )


class PaymentIntentsResourceWithStreamingResponse:
    def __init__(self, payment_intents: PaymentIntentsResource) -> None:
        self._payment_intents = payment_intents

        self.create_bank = to_streamed_response_wrapper(
            payment_intents.create_bank,
        )
        self.create_stable = to_streamed_response_wrapper(
            payment_intents.create_stable,
        )


class AsyncPaymentIntentsResourceWithStreamingResponse:
    def __init__(self, payment_intents: AsyncPaymentIntentsResource) -> None:
        self._payment_intents = payment_intents

        self.create_bank = async_to_streamed_response_wrapper(
            payment_intents.create_bank,
        )
        self.create_stable = async_to_streamed_response_wrapper(
            payment_intents.create_stable,
        )
