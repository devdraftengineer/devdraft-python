# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from devdraft import Devdraft, AsyncDevdraft
from tests.utils import assert_matches_type
from devdraft.types.v0.customers import (
    LiquidationAddressResponse,
    LiquidationAddressListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLiquidationAddresses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Devdraft) -> None:
        liquidation_address = client.v0.customers.liquidation_addresses.create(
            customer_id="cust_123",
            address="0x4d0280da2f2fDA5103914bCc5aad114743152A9c",
            chain="ethereum",
            currency="usdc",
        )
        assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Devdraft) -> None:
        liquidation_address = client.v0.customers.liquidation_addresses.create(
            customer_id="cust_123",
            address="0x4d0280da2f2fDA5103914bCc5aad114743152A9c",
            chain="ethereum",
            currency="usdc",
            bridge_wallet_id="bw_123",
            custom_developer_fee_percent="2.5",
            destination_ach_reference="ACH123",
            destination_address="0x1234567890abcdef1234567890abcdef12345678",
            destination_blockchain_memo="liquidation-memo-123",
            destination_currency="eur",
            destination_payment_rail="sepa",
            destination_sepa_reference="SEPA-REF-123456",
            destination_wire_message="Liquidation payment for customer",
            external_account_id="ext_123",
            prefunded_account_id="pf_acc_123",
            return_address="0xabcdefabcdefabcdefabcdefabcdefabcdef",
        )
        assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Devdraft) -> None:
        response = client.v0.customers.liquidation_addresses.with_raw_response.create(
            customer_id="cust_123",
            address="0x4d0280da2f2fDA5103914bCc5aad114743152A9c",
            chain="ethereum",
            currency="usdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        liquidation_address = response.parse()
        assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Devdraft) -> None:
        with client.v0.customers.liquidation_addresses.with_streaming_response.create(
            customer_id="cust_123",
            address="0x4d0280da2f2fDA5103914bCc5aad114743152A9c",
            chain="ethereum",
            currency="usdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            liquidation_address = response.parse()
            assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v0.customers.liquidation_addresses.with_raw_response.create(
                customer_id="",
                address="0x4d0280da2f2fDA5103914bCc5aad114743152A9c",
                chain="ethereum",
                currency="usdc",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Devdraft) -> None:
        liquidation_address = client.v0.customers.liquidation_addresses.retrieve(
            liquidation_address_id="la_generated_id_123",
            customer_id="cust_123",
        )
        assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Devdraft) -> None:
        response = client.v0.customers.liquidation_addresses.with_raw_response.retrieve(
            liquidation_address_id="la_generated_id_123",
            customer_id="cust_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        liquidation_address = response.parse()
        assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Devdraft) -> None:
        with client.v0.customers.liquidation_addresses.with_streaming_response.retrieve(
            liquidation_address_id="la_generated_id_123",
            customer_id="cust_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            liquidation_address = response.parse()
            assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v0.customers.liquidation_addresses.with_raw_response.retrieve(
                liquidation_address_id="la_generated_id_123",
                customer_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `liquidation_address_id` but received ''"
        ):
            client.v0.customers.liquidation_addresses.with_raw_response.retrieve(
                liquidation_address_id="",
                customer_id="cust_123",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Devdraft) -> None:
        liquidation_address = client.v0.customers.liquidation_addresses.list(
            "cust_123",
        )
        assert_matches_type(LiquidationAddressListResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Devdraft) -> None:
        response = client.v0.customers.liquidation_addresses.with_raw_response.list(
            "cust_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        liquidation_address = response.parse()
        assert_matches_type(LiquidationAddressListResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Devdraft) -> None:
        with client.v0.customers.liquidation_addresses.with_streaming_response.list(
            "cust_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            liquidation_address = response.parse()
            assert_matches_type(LiquidationAddressListResponse, liquidation_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.v0.customers.liquidation_addresses.with_raw_response.list(
                "",
            )


class TestAsyncLiquidationAddresses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDevdraft) -> None:
        liquidation_address = await async_client.v0.customers.liquidation_addresses.create(
            customer_id="cust_123",
            address="0x4d0280da2f2fDA5103914bCc5aad114743152A9c",
            chain="ethereum",
            currency="usdc",
        )
        assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDevdraft) -> None:
        liquidation_address = await async_client.v0.customers.liquidation_addresses.create(
            customer_id="cust_123",
            address="0x4d0280da2f2fDA5103914bCc5aad114743152A9c",
            chain="ethereum",
            currency="usdc",
            bridge_wallet_id="bw_123",
            custom_developer_fee_percent="2.5",
            destination_ach_reference="ACH123",
            destination_address="0x1234567890abcdef1234567890abcdef12345678",
            destination_blockchain_memo="liquidation-memo-123",
            destination_currency="eur",
            destination_payment_rail="sepa",
            destination_sepa_reference="SEPA-REF-123456",
            destination_wire_message="Liquidation payment for customer",
            external_account_id="ext_123",
            prefunded_account_id="pf_acc_123",
            return_address="0xabcdefabcdefabcdefabcdefabcdefabcdef",
        )
        assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.customers.liquidation_addresses.with_raw_response.create(
            customer_id="cust_123",
            address="0x4d0280da2f2fDA5103914bCc5aad114743152A9c",
            chain="ethereum",
            currency="usdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        liquidation_address = await response.parse()
        assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.customers.liquidation_addresses.with_streaming_response.create(
            customer_id="cust_123",
            address="0x4d0280da2f2fDA5103914bCc5aad114743152A9c",
            chain="ethereum",
            currency="usdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            liquidation_address = await response.parse()
            assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v0.customers.liquidation_addresses.with_raw_response.create(
                customer_id="",
                address="0x4d0280da2f2fDA5103914bCc5aad114743152A9c",
                chain="ethereum",
                currency="usdc",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDevdraft) -> None:
        liquidation_address = await async_client.v0.customers.liquidation_addresses.retrieve(
            liquidation_address_id="la_generated_id_123",
            customer_id="cust_123",
        )
        assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.customers.liquidation_addresses.with_raw_response.retrieve(
            liquidation_address_id="la_generated_id_123",
            customer_id="cust_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        liquidation_address = await response.parse()
        assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.customers.liquidation_addresses.with_streaming_response.retrieve(
            liquidation_address_id="la_generated_id_123",
            customer_id="cust_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            liquidation_address = await response.parse()
            assert_matches_type(LiquidationAddressResponse, liquidation_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v0.customers.liquidation_addresses.with_raw_response.retrieve(
                liquidation_address_id="la_generated_id_123",
                customer_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `liquidation_address_id` but received ''"
        ):
            await async_client.v0.customers.liquidation_addresses.with_raw_response.retrieve(
                liquidation_address_id="",
                customer_id="cust_123",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevdraft) -> None:
        liquidation_address = await async_client.v0.customers.liquidation_addresses.list(
            "cust_123",
        )
        assert_matches_type(LiquidationAddressListResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.customers.liquidation_addresses.with_raw_response.list(
            "cust_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        liquidation_address = await response.parse()
        assert_matches_type(LiquidationAddressListResponse, liquidation_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.customers.liquidation_addresses.with_streaming_response.list(
            "cust_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            liquidation_address = await response.parse()
            assert_matches_type(LiquidationAddressListResponse, liquidation_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.v0.customers.liquidation_addresses.with_raw_response.list(
                "",
            )
