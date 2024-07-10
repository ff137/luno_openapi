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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Self


class GetTickerResponse(BaseModel):
    """
    GetTickerResponse response for /api/ticker
    """  # noqa: E501

    ask: Optional[StrictStr] = Field(default=None, description="The lowest ask price")
    bid: Optional[StrictStr] = Field(default=None, description="The highest bid price")
    last_trade: Optional[StrictStr] = Field(
        default=None, description="Last trade price"
    )
    pair: Optional[StrictStr] = None
    rolling_24_hour_volume: Optional[StrictStr] = Field(
        default=None, description="24h rolling trade volume"
    )
    status: Optional[StrictStr] = Field(
        default=None,
        description="Market current status  <code>ACTIVE</code> when the market is trading normally  <code>POSTONLY</code> when the market has been suspended and only post-only orders will be accepted  <code>DISABLED</code> when the market is shutdown and no orders can be accepted  <code>UNKNOWN</code> the market status could not be determined. This is a temporary state.",
    )
    timestamp: Optional[int] = Field(
        default=None, description="Unix timestamp in milliseconds of the tick"
    )
    __properties: ClassVar[List[str]] = [
        "ask",
        "bid",
        "last_trade",
        "pair",
        "rolling_24_hour_volume",
        "status",
        "timestamp",
    ]

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["ACTIVE", "POSTONLY", "DISABLED", "UNKNOWN"]):
            raise ValueError(
                "must be one of enum values ('ACTIVE', 'POSTONLY', 'DISABLED', 'UNKNOWN')"
            )
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
        """Create an instance of GetTickerResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetTickerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "ask": obj.get("ask"),
                "bid": obj.get("bid"),
                "last_trade": obj.get("last_trade"),
                "pair": obj.get("pair"),
                "rolling_24_hour_volume": obj.get("rolling_24_hour_volume"),
                "status": obj.get("status"),
                "timestamp": obj.get("timestamp"),
            }
        )
        return _obj
