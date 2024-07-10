import base64
from contextlib import AbstractAsyncContextManager
from typing import Optional

from luno_openapi.api import (
    AccountsApi,
    AddressApi,
    BeneficiariesApi,
    MarketApi,
    OrdersApi,
    ReceiveApi,
    SendApi,
    TransfersApi,
)
from luno_openapi.api_client import ApiClient
from luno_openapi.configuration import Configuration


class LunoClient(AbstractAsyncContextManager):

    def __init__(
        self,
        *,
        base_url: str = "https://api.luno.com",
        api_key_id: Optional[str] = None,
        api_key_secret: Optional[str] = None,
    ):
        # Configure a Luno instance
        self.configuration = Configuration(host=base_url)
        self.api_client = ApiClient(self.configuration)

        if not (api_key_id and api_key_secret):
            print(
                "api_key_id and api_key_secret are required for authenticated API calls"
            )
        else:
            api_key = f"{api_key_id}:{api_key_secret}"
            api_key_bytes = base64.b64encode(api_key.encode("utf-8"))
            encoded_key = api_key_bytes.decode("utf-8")
            self.api_client.default_headers["Authorization"] = f"Basic {encoded_key}"

        # Initialize the API modules
        self.accounts_api = AccountsApi(self.api_client)
        self.address_api = AddressApi(self.api_client)
        self.beneficiaries_api = BeneficiariesApi(self.api_client)
        self.market_api = MarketApi(self.api_client)
        self.orders_api = OrdersApi(self.api_client)
        self.receive_api = ReceiveApi(self.api_client)
        self.send_api = SendApi(self.api_client)
        self.transfers_api = TransfersApi(self.api_client)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()

    async def close(self):
        await self.api_client.close()
