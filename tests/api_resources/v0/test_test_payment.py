# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from devdraft import Devdraft, AsyncDevdraft
from tests.utils import assert_matches_type
from devdraft.types.v0 import PaymentResponse, TestPaymentRefundResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestPayment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Devdraft) -> None:
        test_payment = client.v0.test_payment.retrieve(
            "id",
        )
        assert_matches_type(PaymentResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Devdraft) -> None:
        response = client.v0.test_payment.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_payment = response.parse()
        assert_matches_type(PaymentResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Devdraft) -> None:
        with client.v0.test_payment.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_payment = response.parse()
            assert_matches_type(PaymentResponse, test_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v0.test_payment.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_process(self, client: Devdraft) -> None:
        test_payment = client.v0.test_payment.process(
            amount=100.5,
            currency="USD",
            description="Test payment for API",
        )
        assert_matches_type(PaymentResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_process_with_all_params(self, client: Devdraft) -> None:
        test_payment = client.v0.test_payment.process(
            amount=100.5,
            currency="USD",
            description="Test payment for API",
            customer_id="cus_12345",
        )
        assert_matches_type(PaymentResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_process(self, client: Devdraft) -> None:
        response = client.v0.test_payment.with_raw_response.process(
            amount=100.5,
            currency="USD",
            description="Test payment for API",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_payment = response.parse()
        assert_matches_type(PaymentResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_process(self, client: Devdraft) -> None:
        with client.v0.test_payment.with_streaming_response.process(
            amount=100.5,
            currency="USD",
            description="Test payment for API",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_payment = response.parse()
            assert_matches_type(PaymentResponse, test_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_refund(self, client: Devdraft) -> None:
        test_payment = client.v0.test_payment.refund(
            "id",
        )
        assert_matches_type(TestPaymentRefundResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_refund(self, client: Devdraft) -> None:
        response = client.v0.test_payment.with_raw_response.refund(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_payment = response.parse()
        assert_matches_type(TestPaymentRefundResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_refund(self, client: Devdraft) -> None:
        with client.v0.test_payment.with_streaming_response.refund(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_payment = response.parse()
            assert_matches_type(TestPaymentRefundResponse, test_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_refund(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v0.test_payment.with_raw_response.refund(
                "",
            )


class TestAsyncTestPayment:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDevdraft) -> None:
        test_payment = await async_client.v0.test_payment.retrieve(
            "id",
        )
        assert_matches_type(PaymentResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.test_payment.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_payment = await response.parse()
        assert_matches_type(PaymentResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.test_payment.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_payment = await response.parse()
            assert_matches_type(PaymentResponse, test_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v0.test_payment.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_process(self, async_client: AsyncDevdraft) -> None:
        test_payment = await async_client.v0.test_payment.process(
            amount=100.5,
            currency="USD",
            description="Test payment for API",
        )
        assert_matches_type(PaymentResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_process_with_all_params(self, async_client: AsyncDevdraft) -> None:
        test_payment = await async_client.v0.test_payment.process(
            amount=100.5,
            currency="USD",
            description="Test payment for API",
            customer_id="cus_12345",
        )
        assert_matches_type(PaymentResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_process(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.test_payment.with_raw_response.process(
            amount=100.5,
            currency="USD",
            description="Test payment for API",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_payment = await response.parse()
        assert_matches_type(PaymentResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_process(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.test_payment.with_streaming_response.process(
            amount=100.5,
            currency="USD",
            description="Test payment for API",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_payment = await response.parse()
            assert_matches_type(PaymentResponse, test_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_refund(self, async_client: AsyncDevdraft) -> None:
        test_payment = await async_client.v0.test_payment.refund(
            "id",
        )
        assert_matches_type(TestPaymentRefundResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_refund(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.test_payment.with_raw_response.refund(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test_payment = await response.parse()
        assert_matches_type(TestPaymentRefundResponse, test_payment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_refund(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.test_payment.with_streaming_response.refund(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test_payment = await response.parse()
            assert_matches_type(TestPaymentRefundResponse, test_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_refund(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v0.test_payment.with_raw_response.refund(
                "",
            )
