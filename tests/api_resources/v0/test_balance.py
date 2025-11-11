# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from devdraft import Devdraft, AsyncDevdraft
from tests.utils import assert_matches_type
from devdraft.types.v0 import AggregatedBalance, BalanceGetAllStablecoinBalancesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBalance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_all_stablecoin_balances(self, client: Devdraft) -> None:
        balance = client.v0.balance.get_all_stablecoin_balances()
        assert_matches_type(BalanceGetAllStablecoinBalancesResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_all_stablecoin_balances(self, client: Devdraft) -> None:
        response = client.v0.balance.with_raw_response.get_all_stablecoin_balances()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(BalanceGetAllStablecoinBalancesResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_all_stablecoin_balances(self, client: Devdraft) -> None:
        with client.v0.balance.with_streaming_response.get_all_stablecoin_balances() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(BalanceGetAllStablecoinBalancesResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_eurc(self, client: Devdraft) -> None:
        balance = client.v0.balance.get_eurc()
        assert_matches_type(AggregatedBalance, balance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_eurc(self, client: Devdraft) -> None:
        response = client.v0.balance.with_raw_response.get_eurc()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(AggregatedBalance, balance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_eurc(self, client: Devdraft) -> None:
        with client.v0.balance.with_streaming_response.get_eurc() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(AggregatedBalance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_usdc(self, client: Devdraft) -> None:
        balance = client.v0.balance.get_usdc()
        assert_matches_type(AggregatedBalance, balance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_usdc(self, client: Devdraft) -> None:
        response = client.v0.balance.with_raw_response.get_usdc()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(AggregatedBalance, balance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_usdc(self, client: Devdraft) -> None:
        with client.v0.balance.with_streaming_response.get_usdc() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(AggregatedBalance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBalance:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_all_stablecoin_balances(self, async_client: AsyncDevdraft) -> None:
        balance = await async_client.v0.balance.get_all_stablecoin_balances()
        assert_matches_type(BalanceGetAllStablecoinBalancesResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_all_stablecoin_balances(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.balance.with_raw_response.get_all_stablecoin_balances()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(BalanceGetAllStablecoinBalancesResponse, balance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_all_stablecoin_balances(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.balance.with_streaming_response.get_all_stablecoin_balances() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(BalanceGetAllStablecoinBalancesResponse, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_eurc(self, async_client: AsyncDevdraft) -> None:
        balance = await async_client.v0.balance.get_eurc()
        assert_matches_type(AggregatedBalance, balance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_eurc(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.balance.with_raw_response.get_eurc()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(AggregatedBalance, balance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_eurc(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.balance.with_streaming_response.get_eurc() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(AggregatedBalance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_usdc(self, async_client: AsyncDevdraft) -> None:
        balance = await async_client.v0.balance.get_usdc()
        assert_matches_type(AggregatedBalance, balance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_usdc(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.balance.with_raw_response.get_usdc()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(AggregatedBalance, balance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_usdc(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.balance.with_streaming_response.get_usdc() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(AggregatedBalance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True
