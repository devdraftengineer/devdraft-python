# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from devdraft import Devdraft, AsyncDevdraft
from devdraft._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Devdraft) -> None:
        payment_link = client.v0.payment_links.create(
            allow_mobile_payment=True,
            allow_quantity_adjustment=True,
            collect_address=True,
            collect_tax=True,
            currency="usdc",
            link_type="PRODUCT",
            title="Premium Subscription",
            url="https://checkout.example.com/pay/123",
        )
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Devdraft) -> None:
        payment_link = client.v0.payment_links.create(
            allow_mobile_payment=True,
            allow_quantity_adjustment=True,
            collect_address=True,
            collect_tax=True,
            currency="usdc",
            link_type="PRODUCT",
            title="Premium Subscription",
            url="https://checkout.example.com/pay/123",
            amount=29.99,
            cover_image="https://example.com/images/premium-subscription.jpg",
            customer_id="123e4567-e89b-12d3-a456-426614174002",
            custom_fields={
                "customField1": "value1",
                "customField2": "value2",
            },
            description="Get access to all premium features with our monthly subscription plan.",
            expiration_date=parse_datetime("2024-12-31T23:59:59Z"),
            is_for_all_product=False,
            limit_payments=True,
            max_payments=100,
            payment_for_id="sub_123456789",
            payment_link_products=[
                {
                    "product_id": "123e4567-e89b-12d3-a456-426614174003",
                    "quantity": 1,
                },
                {
                    "product_id": "123e4567-e89b-12d3-a456-426614174004",
                    "quantity": 2,
                },
            ],
            tax_id="123e4567-e89b-12d3-a456-426614174005",
        )
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Devdraft) -> None:
        response = client.v0.payment_links.with_raw_response.create(
            allow_mobile_payment=True,
            allow_quantity_adjustment=True,
            collect_address=True,
            collect_tax=True,
            currency="usdc",
            link_type="PRODUCT",
            title="Premium Subscription",
            url="https://checkout.example.com/pay/123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = response.parse()
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Devdraft) -> None:
        with client.v0.payment_links.with_streaming_response.create(
            allow_mobile_payment=True,
            allow_quantity_adjustment=True,
            collect_address=True,
            collect_tax=True,
            currency="usdc",
            link_type="PRODUCT",
            title="Premium Subscription",
            url="https://checkout.example.com/pay/123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = response.parse()
            assert payment_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Devdraft) -> None:
        payment_link = client.v0.payment_links.retrieve(
            "id",
        )
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Devdraft) -> None:
        response = client.v0.payment_links.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = response.parse()
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Devdraft) -> None:
        with client.v0.payment_links.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = response.parse()
            assert payment_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v0.payment_links.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Devdraft) -> None:
        payment_link = client.v0.payment_links.update(
            "id",
        )
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Devdraft) -> None:
        response = client.v0.payment_links.with_raw_response.update(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = response.parse()
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Devdraft) -> None:
        with client.v0.payment_links.with_streaming_response.update(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = response.parse()
            assert payment_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v0.payment_links.with_raw_response.update(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Devdraft) -> None:
        payment_link = client.v0.payment_links.list()
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Devdraft) -> None:
        payment_link = client.v0.payment_links.list(
            skip="skip",
            take="take",
        )
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Devdraft) -> None:
        response = client.v0.payment_links.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = response.parse()
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Devdraft) -> None:
        with client.v0.payment_links.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = response.parse()
            assert payment_link is None

        assert cast(Any, response.is_closed) is True


class TestAsyncPaymentLinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDevdraft) -> None:
        payment_link = await async_client.v0.payment_links.create(
            allow_mobile_payment=True,
            allow_quantity_adjustment=True,
            collect_address=True,
            collect_tax=True,
            currency="usdc",
            link_type="PRODUCT",
            title="Premium Subscription",
            url="https://checkout.example.com/pay/123",
        )
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDevdraft) -> None:
        payment_link = await async_client.v0.payment_links.create(
            allow_mobile_payment=True,
            allow_quantity_adjustment=True,
            collect_address=True,
            collect_tax=True,
            currency="usdc",
            link_type="PRODUCT",
            title="Premium Subscription",
            url="https://checkout.example.com/pay/123",
            amount=29.99,
            cover_image="https://example.com/images/premium-subscription.jpg",
            customer_id="123e4567-e89b-12d3-a456-426614174002",
            custom_fields={
                "customField1": "value1",
                "customField2": "value2",
            },
            description="Get access to all premium features with our monthly subscription plan.",
            expiration_date=parse_datetime("2024-12-31T23:59:59Z"),
            is_for_all_product=False,
            limit_payments=True,
            max_payments=100,
            payment_for_id="sub_123456789",
            payment_link_products=[
                {
                    "product_id": "123e4567-e89b-12d3-a456-426614174003",
                    "quantity": 1,
                },
                {
                    "product_id": "123e4567-e89b-12d3-a456-426614174004",
                    "quantity": 2,
                },
            ],
            tax_id="123e4567-e89b-12d3-a456-426614174005",
        )
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.payment_links.with_raw_response.create(
            allow_mobile_payment=True,
            allow_quantity_adjustment=True,
            collect_address=True,
            collect_tax=True,
            currency="usdc",
            link_type="PRODUCT",
            title="Premium Subscription",
            url="https://checkout.example.com/pay/123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = await response.parse()
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.payment_links.with_streaming_response.create(
            allow_mobile_payment=True,
            allow_quantity_adjustment=True,
            collect_address=True,
            collect_tax=True,
            currency="usdc",
            link_type="PRODUCT",
            title="Premium Subscription",
            url="https://checkout.example.com/pay/123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = await response.parse()
            assert payment_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDevdraft) -> None:
        payment_link = await async_client.v0.payment_links.retrieve(
            "id",
        )
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.payment_links.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = await response.parse()
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.payment_links.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = await response.parse()
            assert payment_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v0.payment_links.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncDevdraft) -> None:
        payment_link = await async_client.v0.payment_links.update(
            "id",
        )
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.payment_links.with_raw_response.update(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = await response.parse()
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.payment_links.with_streaming_response.update(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = await response.parse()
            assert payment_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v0.payment_links.with_raw_response.update(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevdraft) -> None:
        payment_link = await async_client.v0.payment_links.list()
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevdraft) -> None:
        payment_link = await async_client.v0.payment_links.list(
            skip="skip",
            take="take",
        )
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.payment_links.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = await response.parse()
        assert payment_link is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.payment_links.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = await response.parse()
            assert payment_link is None

        assert cast(Any, response.is_closed) is True
