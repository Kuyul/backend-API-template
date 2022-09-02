from typing import ClassVar, Type, Optional
from dataclasses import field
from marshmallow import Schema as MSchema
from marshmallow_dataclass import dataclass as dataclass_with_schema


@dataclass_with_schema
class GetUserInfoRequest:
    user_id: str


@dataclass_with_schema
class UserInfo:
    user_id: str
    email: str
    first_name: str
    last_name: str
    prof_pic_url: str
