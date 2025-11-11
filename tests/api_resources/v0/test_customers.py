# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from devdraft import Devdraft, AsyncDevdraft

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Devdraft) -> None:
        customer = client.v0.customers.create(
            first_name="John",
            last_name="Doe",
            phone_number="+1-555-123-4567",
        )
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Devdraft) -> None:
        customer = client.v0.customers.create(
            first_name="John",
            last_name="Doe",
            phone_number="+1-555-123-4567",
            customer_type="Individual",
            email="john.doe@example.com",
            status="ACTIVE",
        )
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Devdraft) -> None:
        response = client.v0.customers.with_raw_response.create(
            first_name="John",
            last_name="Doe",
            phone_number="+1-555-123-4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Devdraft) -> None:
        with client.v0.customers.with_streaming_response.create(
            first_name="John",
            last_name="Doe",
            phone_number="+1-555-123-4567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Devdraft) -> None:
        customer = client.v0.customers.retrieve(
            "cust_123e4567-e89b-12d3-a456-426614174000",
        )
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Devdraft) -> None:
        response = client.v0.customers.with_raw_response.retrieve(
            "cust_123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Devdraft) -> None:
        with client.v0.customers.with_streaming_response.retrieve(
            "cust_123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v0.customers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Devdraft) -> None:
        customer = client.v0.customers.update(
            id="cust_123e4567-e89b-12d3-a456-426614174000",
        )
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Devdraft) -> None:
        customer = client.v0.customers.update(
            id="cust_123e4567-e89b-12d3-a456-426614174000",
            customer_type="Individual",
            email="john.doe@example.com",
            first_name="John",
            last_name="Doe",
            phone_number="+1-987-654-3210",
            status="ACTIVE",
        )
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Devdraft) -> None:
        response = client.v0.customers.with_raw_response.update(
            id="cust_123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Devdraft) -> None:
        with client.v0.customers.with_streaming_response.update(
            id="cust_123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v0.customers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Devdraft) -> None:
        customer = client.v0.customers.list()
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Devdraft) -> None:
        customer = client.v0.customers.list(
            email="john.doe@example.com",
            name="John",
            skip=0,
            status="ACTIVE",
            take=10,
        )
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Devdraft) -> None:
        response = client.v0.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Devdraft) -> None:
        with client.v0.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDevdraft) -> None:
        customer = await async_client.v0.customers.create(
            first_name="John",
            last_name="Doe",
            phone_number="+1-555-123-4567",
        )
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDevdraft) -> None:
        customer = await async_client.v0.customers.create(
            first_name="John",
            last_name="Doe",
            phone_number="+1-555-123-4567",
            customer_type="Individual",
            email="john.doe@example.com",
            status="ACTIVE",
        )
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.customers.with_raw_response.create(
            first_name="John",
            last_name="Doe",
            phone_number="+1-555-123-4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.customers.with_streaming_response.create(
            first_name="John",
            last_name="Doe",
            phone_number="+1-555-123-4567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDevdraft) -> None:
        customer = await async_client.v0.customers.retrieve(
            "cust_123e4567-e89b-12d3-a456-426614174000",
        )
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.customers.with_raw_response.retrieve(
            "cust_123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.customers.with_streaming_response.retrieve(
            "cust_123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v0.customers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncDevdraft) -> None:
        customer = await async_client.v0.customers.update(
            id="cust_123e4567-e89b-12d3-a456-426614174000",
        )
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDevdraft) -> None:
        customer = await async_client.v0.customers.update(
            id="cust_123e4567-e89b-12d3-a456-426614174000",
            customer_type="Individual",
            email="john.doe@example.com",
            first_name="John",
            last_name="Doe",
            phone_number="+1-987-654-3210",
            status="ACTIVE",
        )
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.customers.with_raw_response.update(
            id="cust_123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.customers.with_streaming_response.update(
            id="cust_123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v0.customers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevdraft) -> None:
        customer = await async_client.v0.customers.list()
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevdraft) -> None:
        customer = await async_client.v0.customers.list(
            email="john.doe@example.com",
            name="John",
            skip=0,
            status="ACTIVE",
            take=10,
        )
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert customer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert customer is None

        assert cast(Any, response.is_closed) is True
