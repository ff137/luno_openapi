# coding: utf-8

"""
    Luno API

    The Luno API provides developers with a wealth of financial information provided through the Luno platform.  Through this secure system developers can:  <ul>    <li>Create accounts for trading in cryptocurrencies</li>    <li>Access current and historic cryptocurrency market data</li>    <li>Submit trade orders and view order status</li>    <li>Buy and sell Bitcoin and Ethereum</li>    <li>Send and receive Bitcoin and Ethereum</li>    <li>Generate Bitcoin and Ethereum wallet addresses</li>  </ul>   The Luno API brings the world of Bitcoin and Ethereum to your doorstep. 

    The version of the OpenAPI document: 1.2.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    field_validator,
)
from typing_extensions import Self


class Beneficiary(BaseModel):
    """
    Beneficiary
    """ # noqa: E501
    bank_account_branch: Optional[StrictStr] = Field(default=None, description="Bank branch code")
    bank_account_number: Optional[StrictStr] = Field(default=None, description="Beneficiary bank account number")
    bank_account_type: Optional[StrictStr] = Field(default=None, description="Bank account type")
    bank_country: Optional[StrictStr] = Field(default=None, description="Bank country of origin")
    bank_name: Optional[StrictStr] = Field(default=None, description="Bank SWIFT code")
    bank_recipient: Optional[StrictStr] = Field(default=None, description="The owner of the recipient account")
    created_at: Optional[StrictInt] = Field(default=None, description="Time of beneficiary creation")
    id: Optional[StrictStr] = Field(default=None, description="Unique id referencing beneficiary")
    supports_fast_withdrawals: Optional[StrictBool] = Field(default=None, description="If the bank account supports fast withdrawals")
    __properties: ClassVar[List[str]] = ["bank_account_branch", "bank_account_number", "bank_account_type", "bank_country", "bank_name", "bank_recipient", "created_at", "id", "supports_fast_withdrawals"]

    @field_validator('bank_account_type')
    def bank_account_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Current/Cheque', 'Savings', 'Transmission']):
            raise ValueError("must be one of enum values ('Current/Cheque', 'Savings', 'Transmission')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Beneficiary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Beneficiary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bank_account_branch": obj.get("bank_account_branch"),
            "bank_account_number": obj.get("bank_account_number"),
            "bank_account_type": obj.get("bank_account_type"),
            "bank_country": obj.get("bank_country"),
            "bank_name": obj.get("bank_name"),
            "bank_recipient": obj.get("bank_recipient"),
            "created_at": obj.get("created_at"),
            "id": obj.get("id"),
            "supports_fast_withdrawals": obj.get("supports_fast_withdrawals")
        })
        return _obj


