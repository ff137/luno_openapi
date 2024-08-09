# coding: utf-8

"""
    Luno API

    The Luno API provides developers with a wealth of financial information provided through the Luno platform.  Through this secure system developers can:  <ul>    <li>Create accounts for trading in cryptocurrencies</li>    <li>Access current and historic cryptocurrency market data</li>    <li>Submit trade orders and view order status</li>    <li>Buy and sell Bitcoin and Ethereum</li>    <li>Send and receive Bitcoin and Ethereum</li>    <li>Generate Bitcoin and Ethereum wallet addresses</li>  </ul>   The Luno API brings the world of Bitcoin and Ethereum to your doorstep. 

    The version of the OpenAPI document: 1.2.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from luno_openapi.models.get_move_response import GetMoveResponse


class TestGetMoveResponse(unittest.IsolatedAsyncioTestCase):
    """GetMoveResponse unit test stubs"""

    async def asyncSetUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMoveResponse:
        """Test GetMoveResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetMoveResponse`
        """
        model = GetMoveResponse()
        if include_optional:
            return GetMoveResponse(
                amount = '',
                client_move_id = 'move-1642.2008_10_31',
                created_at = '',
                credit_account_id = '8557520073699984185',
                debit_account_id = '2225762606892986213',
                id = '6213702911573325445',
                status = 'MOVING',
                updated_at = ''
            )
        else:
            return GetMoveResponse(
        )
        """

    def testGetMoveResponse(self):
        """Test GetMoveResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
