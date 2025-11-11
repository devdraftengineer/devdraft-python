# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v0 import test_payment_process_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v0.payment_response import PaymentResponse
from ...types.v0.test_payment_refund_response import TestPaymentRefundResponse

__all__ = ["TestPaymentResource", "AsyncTestPaymentResource"]


class TestPaymentResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def with_raw_response(self) -> TestPaymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TestPaymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestPaymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#with_streaming_response
        """
        return TestPaymentResourceWithStreamingResponse(self)

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
    ) -> PaymentResponse:
        """
        Get payment details by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v0/test-payment/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentResponse,
        )

    def process(
        self,
        *,
        amount: float,
        currency: str,
        description: str,
        customer_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentResponse:
        """Creates a new payment.

        Requires an idempotency key to prevent duplicate payments
        on retry.

        ## Idempotency Key Best Practices

        1. **Generate unique keys**: Use UUIDs or similar unique identifiers, prefixed
           with a descriptive operation name
        2. **Store keys client-side**: Save the key with the original request so you can
           retry with the same key
        3. **Key format**: Between 6-64 alphanumeric characters
        4. **Expiration**: Keys expire after 24 hours by default
        5. **Use case**: Perfect for ensuring payment operations are never processed
           twice, even during network failures

        ## Example Request (curl)

        ```bash
        curl -X POST \\
          https://api.example.com/rest-api/v0/test-payment \\
          -H 'Content-Type: application/json' \\
          -H 'Client-Key: your-api-key' \\
          -H 'Client-Secret: your-api-secret' \\
          -H 'Idempotency-Key: payment_123456_unique_key' \\
          -d '{
            "amount": 100.00,
            "currency": "USD",
            "description": "Test payment for order #12345",
            "customerId": "cus_12345"
          }'
        ```

        ## Example Response (First Request)

        ```json
        {
          "id": "pay_abc123xyz456",
          "amount": 100.0,
          "currency": "USD",
          "status": "succeeded",
          "timestamp": "2023-07-01T12:00:00.000Z"
        }
        ```

        ## Example Response (Duplicate Request)

        The exact same response will be returned for any duplicate request with the same
        idempotency key, without creating a new payment.

        ## Retry Scenario Example

        Network failure during payment submission:

        1. Client creates payment request with idempotency key:
           "payment_123456_unique_key"
        2. Request begins processing, but network connection fails before response
           received
        3. Client retries the exact same request with the same idempotency key
        4. Server detects duplicate idempotency key and returns the result of the first
           request
        5. No duplicate payment is created

        If you retry with same key but different parameters (e.g., different amount),
        you'll receive a 409 Conflict error.

        Args:
          amount: The amount to charge

          currency: The currency code

          description: Description of the payment

          customer_id: Customer reference ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v0/test-payment",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "description": description,
                    "customer_id": customer_id,
                },
                test_payment_process_params.TestPaymentProcessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentResponse,
        )

    def refund(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestPaymentRefundResponse:
        """Refunds an existing payment.

        Requires an idempotency key to prevent duplicate
        refunds on retry.

        ## Idempotency Key Benefits for Refunds

        Refunds are critical financial operations where duplicates can cause serious
        issues. Using idempotency keys ensures:

        1. **Prevent duplicate refunds**: Even if a request times out or fails, retrying
           with the same key won't issue multiple refunds
        2. **Safe retries**: Network failures or timeouts won't risk creating multiple
           refunds
        3. **Consistent response**: Always get the same response for the same operation

        ## Example Request (curl)

        ```bash
        curl -X POST \\
          https://api.example.com/rest-api/v0/test-payment/pay_abc123xyz456/refund \\
          -H 'Content-Type: application/json' \\
          -H 'Client-Key: your-api-key' \\
          -H 'Client-Secret: your-api-secret' \\
          -H 'Idempotency-Key: refund_123456_unique_key'
        ```

        ## Example Response (First Request)

        ```json
        {
          "id": "ref_xyz789",
          "paymentId": "pay_abc123xyz456",
          "amount": 100.0,
          "status": "succeeded",
          "timestamp": "2023-07-01T14:30:00.000Z"
        }
        ```

        ## Example Response (Duplicate Request)

        The exact same response will be returned for any duplicate request with the same
        idempotency key, without creating a new refund.

        ## Idempotency Key Guidelines

        - Use a unique key for each distinct refund operation
        - Store keys client-side to ensure you can retry with the same key if needed
        - Keys expire after 24 hours by default

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v0/test-payment/{id}/refund",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestPaymentRefundResponse,
        )


class AsyncTestPaymentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTestPaymentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTestPaymentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestPaymentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/devdraftengineer/devdraft-python-sdk#with_streaming_response
        """
        return AsyncTestPaymentResourceWithStreamingResponse(self)

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
    ) -> PaymentResponse:
        """
        Get payment details by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v0/test-payment/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentResponse,
        )

    async def process(
        self,
        *,
        amount: float,
        currency: str,
        description: str,
        customer_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentResponse:
        """Creates a new payment.

        Requires an idempotency key to prevent duplicate payments
        on retry.

        ## Idempotency Key Best Practices

        1. **Generate unique keys**: Use UUIDs or similar unique identifiers, prefixed
           with a descriptive operation name
        2. **Store keys client-side**: Save the key with the original request so you can
           retry with the same key
        3. **Key format**: Between 6-64 alphanumeric characters
        4. **Expiration**: Keys expire after 24 hours by default
        5. **Use case**: Perfect for ensuring payment operations are never processed
           twice, even during network failures

        ## Example Request (curl)

        ```bash
        curl -X POST \\
          https://api.example.com/rest-api/v0/test-payment \\
          -H 'Content-Type: application/json' \\
          -H 'Client-Key: your-api-key' \\
          -H 'Client-Secret: your-api-secret' \\
          -H 'Idempotency-Key: payment_123456_unique_key' \\
          -d '{
            "amount": 100.00,
            "currency": "USD",
            "description": "Test payment for order #12345",
            "customerId": "cus_12345"
          }'
        ```

        ## Example Response (First Request)

        ```json
        {
          "id": "pay_abc123xyz456",
          "amount": 100.0,
          "currency": "USD",
          "status": "succeeded",
          "timestamp": "2023-07-01T12:00:00.000Z"
        }
        ```

        ## Example Response (Duplicate Request)

        The exact same response will be returned for any duplicate request with the same
        idempotency key, without creating a new payment.

        ## Retry Scenario Example

        Network failure during payment submission:

        1. Client creates payment request with idempotency key:
           "payment_123456_unique_key"
        2. Request begins processing, but network connection fails before response
           received
        3. Client retries the exact same request with the same idempotency key
        4. Server detects duplicate idempotency key and returns the result of the first
           request
        5. No duplicate payment is created

        If you retry with same key but different parameters (e.g., different amount),
        you'll receive a 409 Conflict error.

        Args:
          amount: The amount to charge

          currency: The currency code

          description: Description of the payment

          customer_id: Customer reference ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v0/test-payment",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "description": description,
                    "customer_id": customer_id,
                },
                test_payment_process_params.TestPaymentProcessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentResponse,
        )

    async def refund(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestPaymentRefundResponse:
        """Refunds an existing payment.

        Requires an idempotency key to prevent duplicate
        refunds on retry.

        ## Idempotency Key Benefits for Refunds

        Refunds are critical financial operations where duplicates can cause serious
        issues. Using idempotency keys ensures:

        1. **Prevent duplicate refunds**: Even if a request times out or fails, retrying
           with the same key won't issue multiple refunds
        2. **Safe retries**: Network failures or timeouts won't risk creating multiple
           refunds
        3. **Consistent response**: Always get the same response for the same operation

        ## Example Request (curl)

        ```bash
        curl -X POST \\
          https://api.example.com/rest-api/v0/test-payment/pay_abc123xyz456/refund \\
          -H 'Content-Type: application/json' \\
          -H 'Client-Key: your-api-key' \\
          -H 'Client-Secret: your-api-secret' \\
          -H 'Idempotency-Key: refund_123456_unique_key'
        ```

        ## Example Response (First Request)

        ```json
        {
          "id": "ref_xyz789",
          "paymentId": "pay_abc123xyz456",
          "amount": 100.0,
          "status": "succeeded",
          "timestamp": "2023-07-01T14:30:00.000Z"
        }
        ```

        ## Example Response (Duplicate Request)

        The exact same response will be returned for any duplicate request with the same
        idempotency key, without creating a new refund.

        ## Idempotency Key Guidelines

        - Use a unique key for each distinct refund operation
        - Store keys client-side to ensure you can retry with the same key if needed
        - Keys expire after 24 hours by default

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v0/test-payment/{id}/refund",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestPaymentRefundResponse,
        )


class TestPaymentResourceWithRawResponse:
    __test__ = False

    def __init__(self, test_payment: TestPaymentResource) -> None:
        self._test_payment = test_payment

        self.retrieve = to_raw_response_wrapper(
            test_payment.retrieve,
        )
        self.process = to_raw_response_wrapper(
            test_payment.process,
        )
        self.refund = to_raw_response_wrapper(
            test_payment.refund,
        )


class AsyncTestPaymentResourceWithRawResponse:
    def __init__(self, test_payment: AsyncTestPaymentResource) -> None:
        self._test_payment = test_payment

        self.retrieve = async_to_raw_response_wrapper(
            test_payment.retrieve,
        )
        self.process = async_to_raw_response_wrapper(
            test_payment.process,
        )
        self.refund = async_to_raw_response_wrapper(
            test_payment.refund,
        )


class TestPaymentResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, test_payment: TestPaymentResource) -> None:
        self._test_payment = test_payment

        self.retrieve = to_streamed_response_wrapper(
            test_payment.retrieve,
        )
        self.process = to_streamed_response_wrapper(
            test_payment.process,
        )
        self.refund = to_streamed_response_wrapper(
            test_payment.refund,
        )


class AsyncTestPaymentResourceWithStreamingResponse:
    def __init__(self, test_payment: AsyncTestPaymentResource) -> None:
        self._test_payment = test_payment

        self.retrieve = async_to_streamed_response_wrapper(
            test_payment.retrieve,
        )
        self.process = async_to_streamed_response_wrapper(
            test_payment.process,
        )
        self.refund = async_to_streamed_response_wrapper(
            test_payment.refund,
        )
