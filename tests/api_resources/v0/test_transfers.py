# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from devdraft import Devdraft, AsyncDevdraft

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_direct_bank(self, client: Devdraft) -> None:
        transfer = client.v0.transfers.create_direct_bank(
            amount=0,
            destination_currency="destinationCurrency",
            payment_rail="paymentRail",
            source_currency="sourceCurrency",
            wallet_id="walletId",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_direct_bank_with_all_params(self, client: Devdraft) -> None:
        transfer = client.v0.transfers.create_direct_bank(
            amount=0,
            destination_currency="destinationCurrency",
            payment_rail="paymentRail",
            source_currency="sourceCurrency",
            wallet_id="walletId",
            ach_reference="ach_reference",
            sepa_reference="sepa_reference",
            wire_message="wire_message",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_direct_bank(self, client: Devdraft) -> None:
        response = client.v0.transfers.with_raw_response.create_direct_bank(
            amount=0,
            destination_currency="destinationCurrency",
            payment_rail="paymentRail",
            source_currency="sourceCurrency",
            wallet_id="walletId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_direct_bank(self, client: Devdraft) -> None:
        with client.v0.transfers.with_streaming_response.create_direct_bank(
            amount=0,
            destination_currency="destinationCurrency",
            payment_rail="paymentRail",
            source_currency="sourceCurrency",
            wallet_id="walletId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert transfer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_direct_wallet(self, client: Devdraft) -> None:
        transfer = client.v0.transfers.create_direct_wallet(
            amount=0,
            network="network",
            stable_coin_currency="stableCoinCurrency",
            wallet_id="walletId",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_direct_wallet(self, client: Devdraft) -> None:
        response = client.v0.transfers.with_raw_response.create_direct_wallet(
            amount=0,
            network="network",
            stable_coin_currency="stableCoinCurrency",
            wallet_id="walletId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_direct_wallet(self, client: Devdraft) -> None:
        with client.v0.transfers.with_streaming_response.create_direct_wallet(
            amount=0,
            network="network",
            stable_coin_currency="stableCoinCurrency",
            wallet_id="walletId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert transfer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_external_bank_transfer(self, client: Devdraft) -> None:
        transfer = client.v0.transfers.create_external_bank_transfer(
            destination_currency="destinationCurrency",
            destination_payment_rail="ach",
            external_account_id="external_account_id",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_external_bank_transfer_with_all_params(self, client: Devdraft) -> None:
        transfer = client.v0.transfers.create_external_bank_transfer(
            destination_currency="destinationCurrency",
            destination_payment_rail="ach",
            external_account_id="external_account_id",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
            ach_reference="x",
            amount=0,
            sepa_reference="xxxxxx",
            spei_reference="x",
            swift_charges="swift_charges",
            swift_reference="x",
            wire_message="x",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_external_bank_transfer(self, client: Devdraft) -> None:
        response = client.v0.transfers.with_raw_response.create_external_bank_transfer(
            destination_currency="destinationCurrency",
            destination_payment_rail="ach",
            external_account_id="external_account_id",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_external_bank_transfer(self, client: Devdraft) -> None:
        with client.v0.transfers.with_streaming_response.create_external_bank_transfer(
            destination_currency="destinationCurrency",
            destination_payment_rail="ach",
            external_account_id="external_account_id",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert transfer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_external_stablecoin_transfer(self, client: Devdraft) -> None:
        transfer = client.v0.transfers.create_external_stablecoin_transfer(
            beneficiary_id="beneficiary_12345",
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_external_stablecoin_transfer_with_all_params(self, client: Devdraft) -> None:
        transfer = client.v0.transfers.create_external_stablecoin_transfer(
            beneficiary_id="beneficiary_12345",
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
            amount=0,
            blockchain_memo="blockchain_memo",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_external_stablecoin_transfer(self, client: Devdraft) -> None:
        response = client.v0.transfers.with_raw_response.create_external_stablecoin_transfer(
            beneficiary_id="beneficiary_12345",
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_external_stablecoin_transfer(self, client: Devdraft) -> None:
        with client.v0.transfers.with_streaming_response.create_external_stablecoin_transfer(
            beneficiary_id="beneficiary_12345",
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert transfer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_stablecoin_conversion(self, client: Devdraft) -> None:
        transfer = client.v0.transfers.create_stablecoin_conversion(
            amount=0,
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_network="sourceNetwork",
            wallet_id="walletId",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_stablecoin_conversion(self, client: Devdraft) -> None:
        response = client.v0.transfers.with_raw_response.create_stablecoin_conversion(
            amount=0,
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_network="sourceNetwork",
            wallet_id="walletId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = response.parse()
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_stablecoin_conversion(self, client: Devdraft) -> None:
        with client.v0.transfers.with_streaming_response.create_stablecoin_conversion(
            amount=0,
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_network="sourceNetwork",
            wallet_id="walletId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = response.parse()
            assert transfer is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTransfers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_direct_bank(self, async_client: AsyncDevdraft) -> None:
        transfer = await async_client.v0.transfers.create_direct_bank(
            amount=0,
            destination_currency="destinationCurrency",
            payment_rail="paymentRail",
            source_currency="sourceCurrency",
            wallet_id="walletId",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_direct_bank_with_all_params(self, async_client: AsyncDevdraft) -> None:
        transfer = await async_client.v0.transfers.create_direct_bank(
            amount=0,
            destination_currency="destinationCurrency",
            payment_rail="paymentRail",
            source_currency="sourceCurrency",
            wallet_id="walletId",
            ach_reference="ach_reference",
            sepa_reference="sepa_reference",
            wire_message="wire_message",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_direct_bank(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.transfers.with_raw_response.create_direct_bank(
            amount=0,
            destination_currency="destinationCurrency",
            payment_rail="paymentRail",
            source_currency="sourceCurrency",
            wallet_id="walletId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_direct_bank(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.transfers.with_streaming_response.create_direct_bank(
            amount=0,
            destination_currency="destinationCurrency",
            payment_rail="paymentRail",
            source_currency="sourceCurrency",
            wallet_id="walletId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert transfer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_direct_wallet(self, async_client: AsyncDevdraft) -> None:
        transfer = await async_client.v0.transfers.create_direct_wallet(
            amount=0,
            network="network",
            stable_coin_currency="stableCoinCurrency",
            wallet_id="walletId",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_direct_wallet(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.transfers.with_raw_response.create_direct_wallet(
            amount=0,
            network="network",
            stable_coin_currency="stableCoinCurrency",
            wallet_id="walletId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_direct_wallet(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.transfers.with_streaming_response.create_direct_wallet(
            amount=0,
            network="network",
            stable_coin_currency="stableCoinCurrency",
            wallet_id="walletId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert transfer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_external_bank_transfer(self, async_client: AsyncDevdraft) -> None:
        transfer = await async_client.v0.transfers.create_external_bank_transfer(
            destination_currency="destinationCurrency",
            destination_payment_rail="ach",
            external_account_id="external_account_id",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_external_bank_transfer_with_all_params(self, async_client: AsyncDevdraft) -> None:
        transfer = await async_client.v0.transfers.create_external_bank_transfer(
            destination_currency="destinationCurrency",
            destination_payment_rail="ach",
            external_account_id="external_account_id",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
            ach_reference="x",
            amount=0,
            sepa_reference="xxxxxx",
            spei_reference="x",
            swift_charges="swift_charges",
            swift_reference="x",
            wire_message="x",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_external_bank_transfer(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.transfers.with_raw_response.create_external_bank_transfer(
            destination_currency="destinationCurrency",
            destination_payment_rail="ach",
            external_account_id="external_account_id",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_external_bank_transfer(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.transfers.with_streaming_response.create_external_bank_transfer(
            destination_currency="destinationCurrency",
            destination_payment_rail="ach",
            external_account_id="external_account_id",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert transfer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_external_stablecoin_transfer(self, async_client: AsyncDevdraft) -> None:
        transfer = await async_client.v0.transfers.create_external_stablecoin_transfer(
            beneficiary_id="beneficiary_12345",
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_external_stablecoin_transfer_with_all_params(
        self, async_client: AsyncDevdraft
    ) -> None:
        transfer = await async_client.v0.transfers.create_external_stablecoin_transfer(
            beneficiary_id="beneficiary_12345",
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
            amount=0,
            blockchain_memo="blockchain_memo",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_external_stablecoin_transfer(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.transfers.with_raw_response.create_external_stablecoin_transfer(
            beneficiary_id="beneficiary_12345",
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_external_stablecoin_transfer(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.transfers.with_streaming_response.create_external_stablecoin_transfer(
            beneficiary_id="beneficiary_12345",
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_wallet_id="sourceWalletId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert transfer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_stablecoin_conversion(self, async_client: AsyncDevdraft) -> None:
        transfer = await async_client.v0.transfers.create_stablecoin_conversion(
            amount=0,
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_network="sourceNetwork",
            wallet_id="walletId",
        )
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_stablecoin_conversion(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.transfers.with_raw_response.create_stablecoin_conversion(
            amount=0,
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_network="sourceNetwork",
            wallet_id="walletId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer = await response.parse()
        assert transfer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_stablecoin_conversion(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.transfers.with_streaming_response.create_stablecoin_conversion(
            amount=0,
            destination_currency="destinationCurrency",
            source_currency="sourceCurrency",
            source_network="sourceNetwork",
            wallet_id="walletId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer = await response.parse()
            assert transfer is None

        assert cast(Any, response.is_closed) is True
