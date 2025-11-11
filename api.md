# V0

Methods:

- <code title="get /api/v0/wallets">client.v0.<a href="./src/devdraft/resources/v0/v0.py">get_wallets</a>() -> None</code>

## Health

Types:

```python
from devdraft.types.v0 import HealthCheckResponse, HealthCheckPublicResponse
```

Methods:

- <code title="get /api/v0/health">client.v0.health.<a href="./src/devdraft/resources/v0/health.py">check</a>() -> <a href="./src/devdraft/types/v0/health_check_response.py">HealthCheckResponse</a></code>
- <code title="get /api/v0/health/public">client.v0.health.<a href="./src/devdraft/resources/v0/health.py">check_public</a>() -> <a href="./src/devdraft/types/v0/health_check_public_response.py">HealthCheckPublicResponse</a></code>

## TestPayment

Types:

```python
from devdraft.types.v0 import PaymentResponse, TestPaymentRefundResponse
```

Methods:

- <code title="get /api/v0/test-payment/{id}">client.v0.test_payment.<a href="./src/devdraft/resources/v0/test_payment.py">retrieve</a>(id) -> <a href="./src/devdraft/types/v0/payment_response.py">PaymentResponse</a></code>
- <code title="post /api/v0/test-payment">client.v0.test_payment.<a href="./src/devdraft/resources/v0/test_payment.py">process</a>(\*\*<a href="src/devdraft/types/v0/test_payment_process_params.py">params</a>) -> <a href="./src/devdraft/types/v0/payment_response.py">PaymentResponse</a></code>
- <code title="post /api/v0/test-payment/{id}/refund">client.v0.test_payment.<a href="./src/devdraft/resources/v0/test_payment.py">refund</a>(id) -> <a href="./src/devdraft/types/v0/test_payment_refund_response.py">TestPaymentRefundResponse</a></code>

## Customers

Types:

```python
from devdraft.types.v0 import CustomerStatus, CustomerType
```

Methods:

- <code title="post /api/v0/customers">client.v0.customers.<a href="./src/devdraft/resources/v0/customers/customers.py">create</a>(\*\*<a href="src/devdraft/types/v0/customer_create_params.py">params</a>) -> None</code>
- <code title="get /api/v0/customers/{id}">client.v0.customers.<a href="./src/devdraft/resources/v0/customers/customers.py">retrieve</a>(id) -> None</code>
- <code title="patch /api/v0/customers/{id}">client.v0.customers.<a href="./src/devdraft/resources/v0/customers/customers.py">update</a>(id, \*\*<a href="src/devdraft/types/v0/customer_update_params.py">params</a>) -> None</code>
- <code title="get /api/v0/customers">client.v0.customers.<a href="./src/devdraft/resources/v0/customers/customers.py">list</a>(\*\*<a href="src/devdraft/types/v0/customer_list_params.py">params</a>) -> None</code>

### LiquidationAddresses

Types:

```python
from devdraft.types.v0.customers import LiquidationAddressResponse, LiquidationAddressListResponse
```

Methods:

- <code title="post /api/v0/customers/{customerId}/liquidation_addresses">client.v0.customers.liquidation_addresses.<a href="./src/devdraft/resources/v0/customers/liquidation_addresses.py">create</a>(customer_id, \*\*<a href="src/devdraft/types/v0/customers/liquidation_address_create_params.py">params</a>) -> <a href="./src/devdraft/types/v0/customers/liquidation_address_response.py">LiquidationAddressResponse</a></code>
- <code title="get /api/v0/customers/{customerId}/liquidation_addresses/{liquidationAddressId}">client.v0.customers.liquidation_addresses.<a href="./src/devdraft/resources/v0/customers/liquidation_addresses.py">retrieve</a>(liquidation_address_id, \*, customer_id) -> <a href="./src/devdraft/types/v0/customers/liquidation_address_response.py">LiquidationAddressResponse</a></code>
- <code title="get /api/v0/customers/{customerId}/liquidation_addresses">client.v0.customers.liquidation_addresses.<a href="./src/devdraft/resources/v0/customers/liquidation_addresses.py">list</a>(customer_id) -> <a href="./src/devdraft/types/v0/customers/liquidation_address_list_response.py">LiquidationAddressListResponse</a></code>

## PaymentLinks

Methods:

- <code title="post /api/v0/payment-links">client.v0.payment_links.<a href="./src/devdraft/resources/v0/payment_links.py">create</a>(\*\*<a href="src/devdraft/types/v0/payment_link_create_params.py">params</a>) -> None</code>
- <code title="get /api/v0/payment-links/{id}">client.v0.payment_links.<a href="./src/devdraft/resources/v0/payment_links.py">retrieve</a>(id) -> None</code>
- <code title="put /api/v0/payment-links/{id}">client.v0.payment_links.<a href="./src/devdraft/resources/v0/payment_links.py">update</a>(id) -> None</code>
- <code title="get /api/v0/payment-links">client.v0.payment_links.<a href="./src/devdraft/resources/v0/payment_links.py">list</a>(\*\*<a href="src/devdraft/types/v0/payment_link_list_params.py">params</a>) -> None</code>

## PaymentIntents

Types:

```python
from devdraft.types.v0 import BridgePaymentRail, StableCoinCurrency
```

Methods:

- <code title="post /api/v0/payment-intents/bank">client.v0.payment_intents.<a href="./src/devdraft/resources/v0/payment_intents.py">create_bank</a>(\*\*<a href="src/devdraft/types/v0/payment_intent_create_bank_params.py">params</a>) -> None</code>
- <code title="post /api/v0/payment-intents/stablecoin">client.v0.payment_intents.<a href="./src/devdraft/resources/v0/payment_intents.py">create_stable</a>(\*\*<a href="src/devdraft/types/v0/payment_intent_create_stable_params.py">params</a>) -> None</code>

## Webhooks

Types:

```python
from devdraft.types.v0 import WebhookResponse, WebhookListResponse
```

Methods:

- <code title="post /api/v0/webhooks">client.v0.webhooks.<a href="./src/devdraft/resources/v0/webhooks.py">create</a>(\*\*<a href="src/devdraft/types/v0/webhook_create_params.py">params</a>) -> <a href="./src/devdraft/types/v0/webhook_response.py">WebhookResponse</a></code>
- <code title="get /api/v0/webhooks/{id}">client.v0.webhooks.<a href="./src/devdraft/resources/v0/webhooks.py">retrieve</a>(id) -> <a href="./src/devdraft/types/v0/webhook_response.py">WebhookResponse</a></code>
- <code title="patch /api/v0/webhooks/{id}">client.v0.webhooks.<a href="./src/devdraft/resources/v0/webhooks.py">update</a>(id, \*\*<a href="src/devdraft/types/v0/webhook_update_params.py">params</a>) -> <a href="./src/devdraft/types/v0/webhook_response.py">WebhookResponse</a></code>
- <code title="get /api/v0/webhooks">client.v0.webhooks.<a href="./src/devdraft/resources/v0/webhooks.py">list</a>(\*\*<a href="src/devdraft/types/v0/webhook_list_params.py">params</a>) -> <a href="./src/devdraft/types/v0/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /api/v0/webhooks/{id}">client.v0.webhooks.<a href="./src/devdraft/resources/v0/webhooks.py">delete</a>(id) -> <a href="./src/devdraft/types/v0/webhook_response.py">WebhookResponse</a></code>

## Transfers

Methods:

- <code title="post /api/v0/transfers/direct-bank">client.v0.transfers.<a href="./src/devdraft/resources/v0/transfers.py">create_direct_bank</a>(\*\*<a href="src/devdraft/types/v0/transfer_create_direct_bank_params.py">params</a>) -> None</code>
- <code title="post /api/v0/transfers/direct-wallet">client.v0.transfers.<a href="./src/devdraft/resources/v0/transfers.py">create_direct_wallet</a>(\*\*<a href="src/devdraft/types/v0/transfer_create_direct_wallet_params.py">params</a>) -> None</code>
- <code title="post /api/v0/transfers/external-bank-transfer">client.v0.transfers.<a href="./src/devdraft/resources/v0/transfers.py">create_external_bank_transfer</a>(\*\*<a href="src/devdraft/types/v0/transfer_create_external_bank_transfer_params.py">params</a>) -> None</code>
- <code title="post /api/v0/transfers/external-stablecoin-transfer">client.v0.transfers.<a href="./src/devdraft/resources/v0/transfers.py">create_external_stablecoin_transfer</a>(\*\*<a href="src/devdraft/types/v0/transfer_create_external_stablecoin_transfer_params.py">params</a>) -> None</code>
- <code title="post /api/v0/transfers/stablecoin-conversion">client.v0.transfers.<a href="./src/devdraft/resources/v0/transfers.py">create_stablecoin_conversion</a>(\*\*<a href="src/devdraft/types/v0/transfer_create_stablecoin_conversion_params.py">params</a>) -> None</code>

## Balance

Types:

```python
from devdraft.types.v0 import AggregatedBalance, BalanceGetAllStablecoinBalancesResponse
```

Methods:

- <code title="get /api/v0/balance">client.v0.balance.<a href="./src/devdraft/resources/v0/balance.py">get_all_stablecoin_balances</a>() -> <a href="./src/devdraft/types/v0/balance_get_all_stablecoin_balances_response.py">BalanceGetAllStablecoinBalancesResponse</a></code>
- <code title="get /api/v0/balance/eurc">client.v0.balance.<a href="./src/devdraft/resources/v0/balance.py">get_eurc</a>() -> <a href="./src/devdraft/types/v0/aggregated_balance.py">AggregatedBalance</a></code>
- <code title="get /api/v0/balance/usdc">client.v0.balance.<a href="./src/devdraft/resources/v0/balance.py">get_usdc</a>() -> <a href="./src/devdraft/types/v0/aggregated_balance.py">AggregatedBalance</a></code>

## ExchangeRate

Types:

```python
from devdraft.types.v0 import ExchangeRateResponse
```

Methods:

- <code title="get /api/v0/exchange-rate/eur-to-usd">client.v0.exchange_rate.<a href="./src/devdraft/resources/v0/exchange_rate.py">get_eur_to_usd</a>() -> <a href="./src/devdraft/types/v0/exchange_rate_response.py">ExchangeRateResponse</a></code>
- <code title="get /api/v0/exchange-rate">client.v0.exchange_rate.<a href="./src/devdraft/resources/v0/exchange_rate.py">get_exchange_rate</a>(\*\*<a href="src/devdraft/types/v0/exchange_rate_get_exchange_rate_params.py">params</a>) -> <a href="./src/devdraft/types/v0/exchange_rate_response.py">ExchangeRateResponse</a></code>
- <code title="get /api/v0/exchange-rate/usd-to-eur">client.v0.exchange_rate.<a href="./src/devdraft/resources/v0/exchange_rate.py">get_usd_to_eur</a>() -> <a href="./src/devdraft/types/v0/exchange_rate_response.py">ExchangeRateResponse</a></code>

## Products

Methods:

- <code title="post /api/v0/products">client.v0.products.<a href="./src/devdraft/resources/v0/products.py">create</a>(\*\*<a href="src/devdraft/types/v0/product_create_params.py">params</a>) -> None</code>
- <code title="get /api/v0/products/{id}">client.v0.products.<a href="./src/devdraft/resources/v0/products.py">retrieve</a>(id) -> None</code>
- <code title="put /api/v0/products/{id}">client.v0.products.<a href="./src/devdraft/resources/v0/products.py">update</a>(id, \*\*<a href="src/devdraft/types/v0/product_update_params.py">params</a>) -> None</code>
- <code title="get /api/v0/products">client.v0.products.<a href="./src/devdraft/resources/v0/products.py">list</a>(\*\*<a href="src/devdraft/types/v0/product_list_params.py">params</a>) -> None</code>
- <code title="delete /api/v0/products/{id}">client.v0.products.<a href="./src/devdraft/resources/v0/products.py">delete</a>(id) -> None</code>
- <code title="post /api/v0/products/{id}/images">client.v0.products.<a href="./src/devdraft/resources/v0/products.py">upload_images</a>(id) -> None</code>

## Invoices

Types:

```python
from devdraft.types.v0 import CreateInvoice
```

Methods:

- <code title="post /api/v0/invoices">client.v0.invoices.<a href="./src/devdraft/resources/v0/invoices.py">create</a>(\*\*<a href="src/devdraft/types/v0/invoice_create_params.py">params</a>) -> None</code>
- <code title="get /api/v0/invoices/{id}">client.v0.invoices.<a href="./src/devdraft/resources/v0/invoices.py">retrieve</a>(id) -> None</code>
- <code title="put /api/v0/invoices/{id}">client.v0.invoices.<a href="./src/devdraft/resources/v0/invoices.py">update</a>(id, \*\*<a href="src/devdraft/types/v0/invoice_update_params.py">params</a>) -> None</code>
- <code title="get /api/v0/invoices">client.v0.invoices.<a href="./src/devdraft/resources/v0/invoices.py">list</a>(\*\*<a href="src/devdraft/types/v0/invoice_list_params.py">params</a>) -> None</code>

## Taxes

Types:

```python
from devdraft.types.v0 import TaxCreateResponse
```

Methods:

- <code title="post /api/v0/taxes">client.v0.taxes.<a href="./src/devdraft/resources/v0/taxes.py">create</a>(\*\*<a href="src/devdraft/types/v0/tax_create_params.py">params</a>) -> <a href="./src/devdraft/types/v0/tax_create_response.py">TaxCreateResponse</a></code>
- <code title="get /api/v0/taxes/{id}">client.v0.taxes.<a href="./src/devdraft/resources/v0/taxes.py">retrieve</a>(id) -> None</code>
- <code title="put /api/v0/taxes/{id}">client.v0.taxes.<a href="./src/devdraft/resources/v0/taxes.py">update</a>(id, \*\*<a href="src/devdraft/types/v0/tax_update_params.py">params</a>) -> None</code>
- <code title="get /api/v0/taxes">client.v0.taxes.<a href="./src/devdraft/resources/v0/taxes.py">list</a>(\*\*<a href="src/devdraft/types/v0/tax_list_params.py">params</a>) -> None</code>
- <code title="delete /api/v0/taxes/{id}">client.v0.taxes.<a href="./src/devdraft/resources/v0/taxes.py">delete</a>(id) -> None</code>
- <code title="delete /api/v0/taxes">client.v0.taxes.<a href="./src/devdraft/resources/v0/taxes.py">delete_all</a>() -> None</code>
- <code title="put /api/v0/taxes">client.v0.taxes.<a href="./src/devdraft/resources/v0/taxes.py">update_all</a>() -> None</code>
