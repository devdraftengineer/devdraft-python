# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v0 import product_list_params, product_create_params, product_update_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["ProductsResource", "AsyncProductsResource"]


class ProductsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return ProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#with_streaming_response
        """
        return ProductsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        name: str,
        price: float,
        currency: Literal["USD", "EUR", "GBP", "CAD", "AUD", "JPY"] | Omit = omit,
        images: SequenceNotStr[str] | Omit = omit,
        product_type: str | Omit = omit,
        quantity: float | Omit = omit,
        status: str | Omit = omit,
        stock_count: float | Omit = omit,
        type: str | Omit = omit,
        unit: str | Omit = omit,
        weight: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Creates a new product with optional image uploads.

        This endpoint allows you to create products with detailed information and
        multiple images.

        ## Use Cases

        - Add new products to your catalog
        - Create products with multiple images
        - Set up product pricing and descriptions

        ## Supported Image Formats

        - JPEG/JPG
        - PNG
        - WebP
        - Maximum 10 images per product
        - Maximum file size: 5MB per image

        ## Example Request (multipart/form-data)

        ```
        name: "Premium Widget"
        description: "High-quality widget for all your needs"
        price: "99.99"
        images: [file1.jpg, file2.jpg]  // Optional, up to 10 images
        ```

        ## Required Fields

        - `name`: Product name
        - `price`: Product price (decimal number)

        ## Optional Fields

        - `description`: Detailed product description
        - `images`: Product images (up to 10 files)

        Args:
          description: Detailed description of the product. Supports markdown formatting for rich text
              display.

          name: Product name as it will appear to customers. Should be clear and descriptive.

          price: Product price in the specified currency. Must be greater than 0.

          currency: Currency code for the price. Defaults to USD if not specified.

          images: Array of image URLs

          product_type: Product type

          quantity: Quantity available

          status: Product status

          stock_count: Stock count

          type: Product type

          unit: Unit of measurement

          weight: Weight of the product

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._post(
            "/api/v0/products",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "price": price,
                    "currency": currency,
                    "images": images,
                    "product_type": product_type,
                    "quantity": quantity,
                    "status": status,
                    "stock_count": stock_count,
                    "type": type,
                    "unit": unit,
                    "weight": weight,
                },
                product_create_params.ProductCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieves detailed information about a specific product.

        This endpoint allows you to fetch complete product details including all images.

        ## Use Cases

        - View product details
        - Display product information
        - Check product availability

        ## Example Response

        ```json
        {
          "id": "prod_123456",
          "name": "Premium Widget",
          "description": "High-quality widget for all your needs",
          "price": "99.99",
          "images": [
            "https://storage.example.com/images/file1.jpg",
            "https://storage.example.com/images/file2.jpg"
          ],
          "createdAt": "2024-03-20T10:00:00Z",
          "updatedAt": "2024-03-20T10:00:00Z"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/v0/products/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        id: str,
        *,
        currency: Literal["USD", "EUR", "GBP", "CAD", "AUD", "JPY"] | Omit = omit,
        description: str | Omit = omit,
        images: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        price: float | Omit = omit,
        product_type: str | Omit = omit,
        quantity: float | Omit = omit,
        status: str | Omit = omit,
        stock_count: float | Omit = omit,
        type: str | Omit = omit,
        unit: str | Omit = omit,
        weight: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Updates an existing product's information and optionally adds new images.

        This endpoint allows you to modify product details and manage product images.

        ## Use Cases

        - Update product information
        - Change product pricing
        - Modify product images
        - Update product description

        ## Example Request (multipart/form-data)

        ```
        name: "Updated Premium Widget"
        description: "Updated description"
        price: "129.99"
        images: [file1.jpg, file2.jpg]  // Optional, up to 10 images
        ```

        ## Notes

        - Only include fields that need to be updated
        - New images will replace existing images
        - Maximum 10 images per product
        - Images are automatically optimized

        Args:
          currency: Currency code for the price. Defaults to USD if not specified.

          description: Detailed description of the product. Supports markdown formatting for rich text
              display.

          images: Array of image URLs

          name: Product name as it will appear to customers. Should be clear and descriptive.

          price: Product price in the specified currency. Must be greater than 0.

          product_type: Product type

          quantity: Quantity available

          status: Product status

          stock_count: Stock count

          type: Product type

          unit: Unit of measurement

          weight: Weight of the product

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._put(
            f"/api/v0/products/{id}",
            body=maybe_transform(
                {
                    "currency": currency,
                    "description": description,
                    "images": images,
                    "name": name,
                    "price": price,
                    "product_type": product_type,
                    "quantity": quantity,
                    "status": status,
                    "stock_count": stock_count,
                    "type": type,
                    "unit": unit,
                    "weight": weight,
                },
                product_update_params.ProductUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        skip: float | Omit = omit,
        take: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieves a list of products with pagination.

        This endpoint allows you to fetch products with optional pagination.

        ## Use Cases

        - List all products
        - Browse product catalog
        - Implement product search

        ## Query Parameters

        - `skip`: Number of records to skip (default: 0)
        - `take`: Number of records to take (default: 10)

        ## Example Response

        ```json
        {
          "data": [
            {
              "id": "prod_123456",
              "name": "Premium Widget",
              "description": "High-quality widget for all your needs",
              "price": "99.99",
              "images": [
                "https://storage.example.com/images/file1.jpg",
                "https://storage.example.com/images/file2.jpg"
              ],
              "createdAt": "2024-03-20T10:00:00Z"
            }
          ],
          "total": 100,
          "skip": 0,
          "take": 10
        }
        ```

        Args:
          skip: Number of records to skip

          take: Number of records to take

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/v0/products",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "skip": skip,
                        "take": take,
                    },
                    product_list_params.ProductListParams,
                ),
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a product and its associated images.

        This endpoint allows you to remove a product and all its associated data.

        ## Use Cases

        - Remove discontinued products
        - Clean up product catalog
        - Delete test products

        ## Notes

        - This action cannot be undone
        - All product images will be deleted
        - Associated data will be removed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v0/products/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def upload_images(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Adds new images to an existing product.

        This endpoint allows you to upload additional images for a product that already
        exists.

        ## Use Cases

        - Add more product images
        - Update product gallery
        - Enhance product presentation

        ## Supported Image Formats

        - JPEG/JPG
        - PNG
        - WebP
        - Maximum 10 images per upload
        - Maximum file size: 5MB per image

        ## Example Request (multipart/form-data)

        ```
        images: [file1.jpg, file2.jpg]  // Up to 10 images
        ```

        ## Notes

        - Images are appended to existing product images
        - Total images per product cannot exceed 10
        - Images are automatically optimized and resized

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/api/v0/products/{id}/images",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncProductsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devdraft-python#with_streaming_response
        """
        return AsyncProductsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        name: str,
        price: float,
        currency: Literal["USD", "EUR", "GBP", "CAD", "AUD", "JPY"] | Omit = omit,
        images: SequenceNotStr[str] | Omit = omit,
        product_type: str | Omit = omit,
        quantity: float | Omit = omit,
        status: str | Omit = omit,
        stock_count: float | Omit = omit,
        type: str | Omit = omit,
        unit: str | Omit = omit,
        weight: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Creates a new product with optional image uploads.

        This endpoint allows you to create products with detailed information and
        multiple images.

        ## Use Cases

        - Add new products to your catalog
        - Create products with multiple images
        - Set up product pricing and descriptions

        ## Supported Image Formats

        - JPEG/JPG
        - PNG
        - WebP
        - Maximum 10 images per product
        - Maximum file size: 5MB per image

        ## Example Request (multipart/form-data)

        ```
        name: "Premium Widget"
        description: "High-quality widget for all your needs"
        price: "99.99"
        images: [file1.jpg, file2.jpg]  // Optional, up to 10 images
        ```

        ## Required Fields

        - `name`: Product name
        - `price`: Product price (decimal number)

        ## Optional Fields

        - `description`: Detailed product description
        - `images`: Product images (up to 10 files)

        Args:
          description: Detailed description of the product. Supports markdown formatting for rich text
              display.

          name: Product name as it will appear to customers. Should be clear and descriptive.

          price: Product price in the specified currency. Must be greater than 0.

          currency: Currency code for the price. Defaults to USD if not specified.

          images: Array of image URLs

          product_type: Product type

          quantity: Quantity available

          status: Product status

          stock_count: Stock count

          type: Product type

          unit: Unit of measurement

          weight: Weight of the product

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._post(
            "/api/v0/products",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "price": price,
                    "currency": currency,
                    "images": images,
                    "product_type": product_type,
                    "quantity": quantity,
                    "status": status,
                    "stock_count": stock_count,
                    "type": type,
                    "unit": unit,
                    "weight": weight,
                },
                product_create_params.ProductCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieves detailed information about a specific product.

        This endpoint allows you to fetch complete product details including all images.

        ## Use Cases

        - View product details
        - Display product information
        - Check product availability

        ## Example Response

        ```json
        {
          "id": "prod_123456",
          "name": "Premium Widget",
          "description": "High-quality widget for all your needs",
          "price": "99.99",
          "images": [
            "https://storage.example.com/images/file1.jpg",
            "https://storage.example.com/images/file2.jpg"
          ],
          "createdAt": "2024-03-20T10:00:00Z",
          "updatedAt": "2024-03-20T10:00:00Z"
        }
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/v0/products/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        id: str,
        *,
        currency: Literal["USD", "EUR", "GBP", "CAD", "AUD", "JPY"] | Omit = omit,
        description: str | Omit = omit,
        images: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        price: float | Omit = omit,
        product_type: str | Omit = omit,
        quantity: float | Omit = omit,
        status: str | Omit = omit,
        stock_count: float | Omit = omit,
        type: str | Omit = omit,
        unit: str | Omit = omit,
        weight: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Updates an existing product's information and optionally adds new images.

        This endpoint allows you to modify product details and manage product images.

        ## Use Cases

        - Update product information
        - Change product pricing
        - Modify product images
        - Update product description

        ## Example Request (multipart/form-data)

        ```
        name: "Updated Premium Widget"
        description: "Updated description"
        price: "129.99"
        images: [file1.jpg, file2.jpg]  // Optional, up to 10 images
        ```

        ## Notes

        - Only include fields that need to be updated
        - New images will replace existing images
        - Maximum 10 images per product
        - Images are automatically optimized

        Args:
          currency: Currency code for the price. Defaults to USD if not specified.

          description: Detailed description of the product. Supports markdown formatting for rich text
              display.

          images: Array of image URLs

          name: Product name as it will appear to customers. Should be clear and descriptive.

          price: Product price in the specified currency. Must be greater than 0.

          product_type: Product type

          quantity: Quantity available

          status: Product status

          stock_count: Stock count

          type: Product type

          unit: Unit of measurement

          weight: Weight of the product

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._put(
            f"/api/v0/products/{id}",
            body=await async_maybe_transform(
                {
                    "currency": currency,
                    "description": description,
                    "images": images,
                    "name": name,
                    "price": price,
                    "product_type": product_type,
                    "quantity": quantity,
                    "status": status,
                    "stock_count": stock_count,
                    "type": type,
                    "unit": unit,
                    "weight": weight,
                },
                product_update_params.ProductUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        skip: float | Omit = omit,
        take: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Retrieves a list of products with pagination.

        This endpoint allows you to fetch products with optional pagination.

        ## Use Cases

        - List all products
        - Browse product catalog
        - Implement product search

        ## Query Parameters

        - `skip`: Number of records to skip (default: 0)
        - `take`: Number of records to take (default: 10)

        ## Example Response

        ```json
        {
          "data": [
            {
              "id": "prod_123456",
              "name": "Premium Widget",
              "description": "High-quality widget for all your needs",
              "price": "99.99",
              "images": [
                "https://storage.example.com/images/file1.jpg",
                "https://storage.example.com/images/file2.jpg"
              ],
              "createdAt": "2024-03-20T10:00:00Z"
            }
          ],
          "total": 100,
          "skip": 0,
          "take": 10
        }
        ```

        Args:
          skip: Number of records to skip

          take: Number of records to take

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/v0/products",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "skip": skip,
                        "take": take,
                    },
                    product_list_params.ProductListParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a product and its associated images.

        This endpoint allows you to remove a product and all its associated data.

        ## Use Cases

        - Remove discontinued products
        - Clean up product catalog
        - Delete test products

        ## Notes

        - This action cannot be undone
        - All product images will be deleted
        - Associated data will be removed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v0/products/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def upload_images(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Adds new images to an existing product.

        This endpoint allows you to upload additional images for a product that already
        exists.

        ## Use Cases

        - Add more product images
        - Update product gallery
        - Enhance product presentation

        ## Supported Image Formats

        - JPEG/JPG
        - PNG
        - WebP
        - Maximum 10 images per upload
        - Maximum file size: 5MB per image

        ## Example Request (multipart/form-data)

        ```
        images: [file1.jpg, file2.jpg]  // Up to 10 images
        ```

        ## Notes

        - Images are appended to existing product images
        - Total images per product cannot exceed 10
        - Images are automatically optimized and resized

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/api/v0/products/{id}/images",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.create = to_raw_response_wrapper(
            products.create,
        )
        self.retrieve = to_raw_response_wrapper(
            products.retrieve,
        )
        self.update = to_raw_response_wrapper(
            products.update,
        )
        self.list = to_raw_response_wrapper(
            products.list,
        )
        self.delete = to_raw_response_wrapper(
            products.delete,
        )
        self.upload_images = to_raw_response_wrapper(
            products.upload_images,
        )


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.create = async_to_raw_response_wrapper(
            products.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            products.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            products.update,
        )
        self.list = async_to_raw_response_wrapper(
            products.list,
        )
        self.delete = async_to_raw_response_wrapper(
            products.delete,
        )
        self.upload_images = async_to_raw_response_wrapper(
            products.upload_images,
        )


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.create = to_streamed_response_wrapper(
            products.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            products.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            products.update,
        )
        self.list = to_streamed_response_wrapper(
            products.list,
        )
        self.delete = to_streamed_response_wrapper(
            products.delete,
        )
        self.upload_images = to_streamed_response_wrapper(
            products.upload_images,
        )


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.create = async_to_streamed_response_wrapper(
            products.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            products.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            products.update,
        )
        self.list = async_to_streamed_response_wrapper(
            products.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            products.delete,
        )
        self.upload_images = async_to_streamed_response_wrapper(
            products.upload_images,
        )
