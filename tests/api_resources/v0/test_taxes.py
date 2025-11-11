# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from devdraft import Devdraft, AsyncDevdraft
from tests.utils import assert_matches_type
from devdraft.types.v0 import TaxCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTaxes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Devdraft) -> None:
        tax = client.v0.taxes.create(
            name="Sales Tax",
            percentage=8.5,
        )
        assert_matches_type(TaxCreateResponse, tax, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Devdraft) -> None:
        tax = client.v0.taxes.create(
            name="Sales Tax",
            percentage=8.5,
            active=True,
            app_ids=["app_123e4567-e89b-12d3-a456-426614174000"],
            description="Standard sales tax for retail transactions",
        )
        assert_matches_type(TaxCreateResponse, tax, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Devdraft) -> None:
        response = client.v0.taxes.with_raw_response.create(
            name="Sales Tax",
            percentage=8.5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = response.parse()
        assert_matches_type(TaxCreateResponse, tax, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Devdraft) -> None:
        with client.v0.taxes.with_streaming_response.create(
            name="Sales Tax",
            percentage=8.5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = response.parse()
            assert_matches_type(TaxCreateResponse, tax, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Devdraft) -> None:
        tax = client.v0.taxes.retrieve(
            "tax_123e4567-e89b-12d3-a456-426614174000",
        )
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Devdraft) -> None:
        response = client.v0.taxes.with_raw_response.retrieve(
            "tax_123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = response.parse()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Devdraft) -> None:
        with client.v0.taxes.with_streaming_response.retrieve(
            "tax_123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = response.parse()
            assert tax is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v0.taxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Devdraft) -> None:
        tax = client.v0.taxes.update(
            id="tax_123e4567-e89b-12d3-a456-426614174000",
        )
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Devdraft) -> None:
        tax = client.v0.taxes.update(
            id="tax_123e4567-e89b-12d3-a456-426614174000",
            active=False,
            app_ids=["app_123e4567-e89b-12d3-a456-426614174000"],
            description="Updated description for retail sales tax",
            name="Updated Sales Tax",
            percentage=10.5,
        )
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Devdraft) -> None:
        response = client.v0.taxes.with_raw_response.update(
            id="tax_123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = response.parse()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Devdraft) -> None:
        with client.v0.taxes.with_streaming_response.update(
            id="tax_123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = response.parse()
            assert tax is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v0.taxes.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Devdraft) -> None:
        tax = client.v0.taxes.list()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Devdraft) -> None:
        tax = client.v0.taxes.list(
            active=True,
            name="Sales",
            skip=0,
            take=10,
        )
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Devdraft) -> None:
        response = client.v0.taxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = response.parse()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Devdraft) -> None:
        with client.v0.taxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = response.parse()
            assert tax is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Devdraft) -> None:
        tax = client.v0.taxes.delete(
            "tax_123e4567-e89b-12d3-a456-426614174000",
        )
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Devdraft) -> None:
        response = client.v0.taxes.with_raw_response.delete(
            "tax_123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = response.parse()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Devdraft) -> None:
        with client.v0.taxes.with_streaming_response.delete(
            "tax_123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = response.parse()
            assert tax is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v0.taxes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: Devdraft) -> None:
        tax = client.v0.taxes.delete_all()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: Devdraft) -> None:
        response = client.v0.taxes.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = response.parse()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: Devdraft) -> None:
        with client.v0.taxes.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = response.parse()
            assert tax is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_all(self, client: Devdraft) -> None:
        tax = client.v0.taxes.update_all()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_all(self, client: Devdraft) -> None:
        response = client.v0.taxes.with_raw_response.update_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = response.parse()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_all(self, client: Devdraft) -> None:
        with client.v0.taxes.with_streaming_response.update_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = response.parse()
            assert tax is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTaxes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDevdraft) -> None:
        tax = await async_client.v0.taxes.create(
            name="Sales Tax",
            percentage=8.5,
        )
        assert_matches_type(TaxCreateResponse, tax, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDevdraft) -> None:
        tax = await async_client.v0.taxes.create(
            name="Sales Tax",
            percentage=8.5,
            active=True,
            app_ids=["app_123e4567-e89b-12d3-a456-426614174000"],
            description="Standard sales tax for retail transactions",
        )
        assert_matches_type(TaxCreateResponse, tax, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.taxes.with_raw_response.create(
            name="Sales Tax",
            percentage=8.5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = await response.parse()
        assert_matches_type(TaxCreateResponse, tax, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.taxes.with_streaming_response.create(
            name="Sales Tax",
            percentage=8.5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = await response.parse()
            assert_matches_type(TaxCreateResponse, tax, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDevdraft) -> None:
        tax = await async_client.v0.taxes.retrieve(
            "tax_123e4567-e89b-12d3-a456-426614174000",
        )
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.taxes.with_raw_response.retrieve(
            "tax_123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = await response.parse()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.taxes.with_streaming_response.retrieve(
            "tax_123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = await response.parse()
            assert tax is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v0.taxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncDevdraft) -> None:
        tax = await async_client.v0.taxes.update(
            id="tax_123e4567-e89b-12d3-a456-426614174000",
        )
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDevdraft) -> None:
        tax = await async_client.v0.taxes.update(
            id="tax_123e4567-e89b-12d3-a456-426614174000",
            active=False,
            app_ids=["app_123e4567-e89b-12d3-a456-426614174000"],
            description="Updated description for retail sales tax",
            name="Updated Sales Tax",
            percentage=10.5,
        )
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.taxes.with_raw_response.update(
            id="tax_123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = await response.parse()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.taxes.with_streaming_response.update(
            id="tax_123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = await response.parse()
            assert tax is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v0.taxes.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevdraft) -> None:
        tax = await async_client.v0.taxes.list()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevdraft) -> None:
        tax = await async_client.v0.taxes.list(
            active=True,
            name="Sales",
            skip=0,
            take=10,
        )
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.taxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = await response.parse()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.taxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = await response.parse()
            assert tax is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncDevdraft) -> None:
        tax = await async_client.v0.taxes.delete(
            "tax_123e4567-e89b-12d3-a456-426614174000",
        )
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.taxes.with_raw_response.delete(
            "tax_123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = await response.parse()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.taxes.with_streaming_response.delete(
            "tax_123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = await response.parse()
            assert tax is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v0.taxes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncDevdraft) -> None:
        tax = await async_client.v0.taxes.delete_all()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.taxes.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = await response.parse()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.taxes.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = await response.parse()
            assert tax is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_all(self, async_client: AsyncDevdraft) -> None:
        tax = await async_client.v0.taxes.update_all()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_all(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.taxes.with_raw_response.update_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tax = await response.parse()
        assert tax is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_all(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.taxes.with_streaming_response.update_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tax = await response.parse()
            assert tax is None

        assert cast(Any, response.is_closed) is True
