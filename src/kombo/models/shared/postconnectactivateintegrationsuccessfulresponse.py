"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from kombo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostConnectActivateIntegrationSuccessfulResponseData:
    end_user_email: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_user_email') }})
    end_user_organization_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_user_organization_name') }})
    end_user_origin_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_user_origin_id') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    tool: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tool') }})
    


class PostConnectActivateIntegrationSuccessfulResponseStatus(str, Enum):
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostConnectActivateIntegrationSuccessfulResponse:
    data: PostConnectActivateIntegrationSuccessfulResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    status: PostConnectActivateIntegrationSuccessfulResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

