# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from devdraft import Devdraft, AsyncDevdraft

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentIntents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_bank(self, client: Devdraft) -> None:
        payment_intent = client.v0.payment_intents.create_bank(
            destination_currency="usdc",
            destination_network="ethereum",
            source_currency="usd",
            source_payment_rail="ach_push",
        )
        assert payment_intent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_bank_with_all_params(self, client: Devdraft) -> None:
        payment_intent = client.v0.payment_intents.create_bank(
            destination_currency="usdc",
            destination_network="ethereum",
            source_currency="usd",
            source_payment_rail="ach_push",
            ach_reference="INV12345",
            amount="1000.00",
            customer_address="123 Main St, New York, NY 10001",
            customer_country="United States",
            customer_country_iso="US",
            customer_email="john.doe@example.com",
            customer_first_name="John",
            customer_last_name="Doe",
            customer_province="New York",
            customer_province_iso="NY",
            destination_address="0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1",
            phone_number="+1-555-123-4567",
            sepa_reference="REF-123456789",
            wire_message="Payment for invoice #12345",
        )
        assert payment_intent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_bank(self, client: Devdraft) -> None:
        response = client.v0.payment_intents.with_raw_response.create_bank(
            destination_currency="usdc",
            destination_network="ethereum",
            source_currency="usd",
            source_payment_rail="ach_push",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_intent = response.parse()
        assert payment_intent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_bank(self, client: Devdraft) -> None:
        with client.v0.payment_intents.with_streaming_response.create_bank(
            destination_currency="usdc",
            destination_network="ethereum",
            source_currency="usd",
            source_payment_rail="ach_push",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_intent = response.parse()
            assert payment_intent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_stable(self, client: Devdraft) -> None:
        payment_intent = client.v0.payment_intents.create_stable(
            destination_network="polygon",
            source_currency="usdc",
            source_network="ethereum",
        )
        assert payment_intent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_stable_with_all_params(self, client: Devdraft) -> None:
        payment_intent = client.v0.payment_intents.create_stable(
            destination_network="polygon",
            source_currency="usdc",
            source_network="ethereum",
            amount="100.00",
            customer_address="123 Main St, New York, NY 10001",
            customer_country="United States",
            customer_country_iso="US",
            customer_email="john.doe@example.com",
            customer_first_name="John",
            customer_last_name="Doe",
            customer_province="New York",
            customer_province_iso="NY",
            destination_address="0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1",
            destination_currency="eurc",
            phone_number="+1-555-123-4567",
        )
        assert payment_intent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_stable(self, client: Devdraft) -> None:
        response = client.v0.payment_intents.with_raw_response.create_stable(
            destination_network="polygon",
            source_currency="usdc",
            source_network="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_intent = response.parse()
        assert payment_intent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_stable(self, client: Devdraft) -> None:
        with client.v0.payment_intents.with_streaming_response.create_stable(
            destination_network="polygon",
            source_currency="usdc",
            source_network="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_intent = response.parse()
            assert payment_intent is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPaymentIntents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_bank(self, async_client: AsyncDevdraft) -> None:
        payment_intent = await async_client.v0.payment_intents.create_bank(
            destination_currency="usdc",
            destination_network="ethereum",
            source_currency="usd",
            source_payment_rail="ach_push",
        )
        assert payment_intent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_bank_with_all_params(self, async_client: AsyncDevdraft) -> None:
        payment_intent = await async_client.v0.payment_intents.create_bank(
            destination_currency="usdc",
            destination_network="ethereum",
            source_currency="usd",
            source_payment_rail="ach_push",
            ach_reference="INV12345",
            amount="1000.00",
            customer_address="123 Main St, New York, NY 10001",
            customer_country="United States",
            customer_country_iso="US",
            customer_email="john.doe@example.com",
            customer_first_name="John",
            customer_last_name="Doe",
            customer_province="New York",
            customer_province_iso="NY",
            destination_address="0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1",
            phone_number="+1-555-123-4567",
            sepa_reference="REF-123456789",
            wire_message="Payment for invoice #12345",
        )
        assert payment_intent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_bank(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.payment_intents.with_raw_response.create_bank(
            destination_currency="usdc",
            destination_network="ethereum",
            source_currency="usd",
            source_payment_rail="ach_push",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_intent = await response.parse()
        assert payment_intent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_bank(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.payment_intents.with_streaming_response.create_bank(
            destination_currency="usdc",
            destination_network="ethereum",
            source_currency="usd",
            source_payment_rail="ach_push",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_intent = await response.parse()
            assert payment_intent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_stable(self, async_client: AsyncDevdraft) -> None:
        payment_intent = await async_client.v0.payment_intents.create_stable(
            destination_network="polygon",
            source_currency="usdc",
            source_network="ethereum",
        )
        assert payment_intent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_stable_with_all_params(self, async_client: AsyncDevdraft) -> None:
        payment_intent = await async_client.v0.payment_intents.create_stable(
            destination_network="polygon",
            source_currency="usdc",
            source_network="ethereum",
            amount="100.00",
            customer_address="123 Main St, New York, NY 10001",
            customer_country="United States",
            customer_country_iso="US",
            customer_email="john.doe@example.com",
            customer_first_name="John",
            customer_last_name="Doe",
            customer_province="New York",
            customer_province_iso="NY",
            destination_address="0x742d35Cc6634C0532925a3b8D4C9db96c4b4d8e1",
            destination_currency="eurc",
            phone_number="+1-555-123-4567",
        )
        assert payment_intent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_stable(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.payment_intents.with_raw_response.create_stable(
            destination_network="polygon",
            source_currency="usdc",
            source_network="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_intent = await response.parse()
        assert payment_intent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_stable(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.payment_intents.with_streaming_response.create_stable(
            destination_network="polygon",
            source_currency="usdc",
            source_network="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_intent = await response.parse()
            assert payment_intent is None

        assert cast(Any, response.is_closed) is True
