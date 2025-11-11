# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from devdraft import Devdraft, AsyncDevdraft
from devdraft._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Devdraft) -> None:
        invoice = client.v0.invoices.create(
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
        )
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Devdraft) -> None:
        invoice = client.v0.invoices.create(
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
            address="address",
            logo="logo",
            phone_number="phone_number",
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            tax_id="taxId",
        )
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Devdraft) -> None:
        response = client.v0.invoices.with_raw_response.create(
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Devdraft) -> None:
        with client.v0.invoices.with_streaming_response.create(
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Devdraft) -> None:
        invoice = client.v0.invoices.retrieve(
            "id",
        )
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Devdraft) -> None:
        response = client.v0.invoices.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Devdraft) -> None:
        with client.v0.invoices.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v0.invoices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Devdraft) -> None:
        invoice = client.v0.invoices.update(
            id="id",
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
        )
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Devdraft) -> None:
        invoice = client.v0.invoices.update(
            id="id",
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
            address="address",
            logo="logo",
            phone_number="phone_number",
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            tax_id="taxId",
        )
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Devdraft) -> None:
        response = client.v0.invoices.with_raw_response.update(
            id="id",
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Devdraft) -> None:
        with client.v0.invoices.with_streaming_response.update(
            id="id",
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Devdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v0.invoices.with_raw_response.update(
                id="",
                currency="usdc",
                customer_id="customer_id",
                delivery="EMAIL",
                due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
                email="email",
                items=[
                    {
                        "product_id": "product_id",
                        "quantity": 0,
                    }
                ],
                name="name",
                partial_payment=True,
                payment_link=True,
                payment_methods=["ACH"],
                status="DRAFT",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Devdraft) -> None:
        invoice = client.v0.invoices.list()
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Devdraft) -> None:
        invoice = client.v0.invoices.list(
            skip=0,
            take=0,
        )
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Devdraft) -> None:
        response = client.v0.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Devdraft) -> None:
        with client.v0.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncDevdraft) -> None:
        invoice = await async_client.v0.invoices.create(
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
        )
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDevdraft) -> None:
        invoice = await async_client.v0.invoices.create(
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
            address="address",
            logo="logo",
            phone_number="phone_number",
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            tax_id="taxId",
        )
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.invoices.with_raw_response.create(
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.invoices.with_streaming_response.create(
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDevdraft) -> None:
        invoice = await async_client.v0.invoices.retrieve(
            "id",
        )
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.invoices.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.invoices.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v0.invoices.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncDevdraft) -> None:
        invoice = await async_client.v0.invoices.update(
            id="id",
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
        )
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDevdraft) -> None:
        invoice = await async_client.v0.invoices.update(
            id="id",
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
            address="address",
            logo="logo",
            phone_number="phone_number",
            send_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            tax_id="taxId",
        )
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.invoices.with_raw_response.update(
            id="id",
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.invoices.with_streaming_response.update(
            id="id",
            currency="usdc",
            customer_id="customer_id",
            delivery="EMAIL",
            due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            items=[
                {
                    "product_id": "product_id",
                    "quantity": 0,
                }
            ],
            name="name",
            partial_payment=True,
            payment_link=True,
            payment_methods=["ACH"],
            status="DRAFT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncDevdraft) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v0.invoices.with_raw_response.update(
                id="",
                currency="usdc",
                customer_id="customer_id",
                delivery="EMAIL",
                due_date=parse_datetime("2019-12-27T18:11:19.117Z"),
                email="email",
                items=[
                    {
                        "product_id": "product_id",
                        "quantity": 0,
                    }
                ],
                name="name",
                partial_payment=True,
                payment_link=True,
                payment_methods=["ACH"],
                status="DRAFT",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDevdraft) -> None:
        invoice = await async_client.v0.invoices.list()
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDevdraft) -> None:
        invoice = await async_client.v0.invoices.list(
            skip=0,
            take=0,
        )
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDevdraft) -> None:
        response = await async_client.v0.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert invoice is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDevdraft) -> None:
        async with async_client.v0.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert invoice is None

        assert cast(Any, response.is_closed) is True
