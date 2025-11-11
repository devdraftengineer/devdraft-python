# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from devdraft import Devdraft, AsyncDevdraft
from tests.utils import assert_matches_type
from devdraft.types.v0 import ExchangeRateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExchangeRate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_eur_to_usd(self, client: Devdraft) -> None:
        exchange_rate = client.v0.exchange_rate.get_eur_to_usd()
        assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_eur_to_usd(self, client: Devdraft) -> None:
        response = client.v0.exchange_rate.with_raw_response.get_eur_to_usd()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_eur_to_usd(self, client: Devdraft) -> None:
        with client.v0.exchange_rate.with_streaming_response.get_eur_to_usd() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_exchange_rate(self, client: Devdraft) -> None:
        exchange_rate = client.v0.exchange_rate.get_exchange_rate(
            from_="usd",
            to="eur",
        )
        assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_exchange_rate(self, client: Devdraft) -> None:
        response = client.v0.exchange_rate.with_raw_response.get_exchange_rate(
            from_="usd",
            to="eur",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_exchange_rate(self, client: Devdraft) -> None:
        with client.v0.exchange_rate.with_streaming_response.get_exchange_rate(
            from_="usd",
            to="eur",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_usd_to_eur(self, client: Devdraft) -> None:
        exchange_rate = client.v0.exchange_rate.get_usd_to_eur()
        assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_usd_to_eur(self, client: Devdraft) -> None:
        response = client.v0.exchange_rate.with_raw_response.get_usd_to_eur()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = response.parse()
        assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_usd_to_eur(self, client: Devdraft) -> None:
        with client.v0.exchange_rate.with_streaming_response.get_usd_to_eur() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = response.parse()
            assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExchangeRate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_eur_to_usd(self, async_client: AsyncDevdraft) -> None:
        exchange_rate = await async_client.v0.exchange_rate.get_eur_to_usd()
        assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_eur_to_usd(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.exchange_rate.with_raw_response.get_eur_to_usd()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_eur_to_usd(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.exchange_rate.with_streaming_response.get_eur_to_usd() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_exchange_rate(self, async_client: AsyncDevdraft) -> None:
        exchange_rate = await async_client.v0.exchange_rate.get_exchange_rate(
            from_="usd",
            to="eur",
        )
        assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_exchange_rate(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.exchange_rate.with_raw_response.get_exchange_rate(
            from_="usd",
            to="eur",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_exchange_rate(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.exchange_rate.with_streaming_response.get_exchange_rate(
            from_="usd",
            to="eur",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_usd_to_eur(self, async_client: AsyncDevdraft) -> None:
        exchange_rate = await async_client.v0.exchange_rate.get_usd_to_eur()
        assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_usd_to_eur(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.exchange_rate.with_raw_response.get_usd_to_eur()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange_rate = await response.parse()
        assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_usd_to_eur(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.exchange_rate.with_streaming_response.get_usd_to_eur() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange_rate = await response.parse()
            assert_matches_type(ExchangeRateResponse, exchange_rate, path=["response"])

        assert cast(Any, response.is_closed) is True
