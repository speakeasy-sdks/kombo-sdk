"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from kombo import utils
from typing import Optional

class GetIntegrationsIntegrationIDSuccessfulResponseDataCategory(str, Enum):
    HRIS = 'HRIS'
    ATS = 'ATS'
    ASSESSMENT = 'ASSESSMENT'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsIntegrationIDSuccessfulResponseDataEndUser:
    creator_email: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creator_email') }})
    organization_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_name') }})
    origin_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('origin_id') }})
    r"""The ID you have passed initially to the connection flow to create this integration."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsIntegrationIDSuccessfulResponseDataScopeConfig:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    


class GetIntegrationsIntegrationIDSuccessfulResponseDataStatus(str, Enum):
    ACTIVE = 'ACTIVE'
    INVALID = 'INVALID'
    INACTIVE = 'INACTIVE'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsIntegrationIDSuccessfulResponseDataTool:
    icon_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('icon_url') }})
    r"""URL to a square SVG icon of the connected tool."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The ID of the connected tool in Kombo (e.g. `factorial`)."""
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    logo_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logo_url') }})
    r"""URL to an SVG logo of the connected tool. The logo usually contains the tool name."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsIntegrationIDSuccessfulResponseData:
    category: GetIntegrationsIntegrationIDSuccessfulResponseDataCategory = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""YYYY-MM-DDTHH:mm:ss.sssZ
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    end_user: GetIntegrationsIntegrationIDSuccessfulResponseDataEndUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_user') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    scope_config: GetIntegrationsIntegrationIDSuccessfulResponseDataScopeConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scope_config') }})
    status: GetIntegrationsIntegrationIDSuccessfulResponseDataStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    tool: GetIntegrationsIntegrationIDSuccessfulResponseDataTool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tool') }})
    


class GetIntegrationsIntegrationIDSuccessfulResponseStatus(str, Enum):
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsIntegrationIDSuccessfulResponse:
    data: GetIntegrationsIntegrationIDSuccessfulResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    status: GetIntegrationsIntegrationIDSuccessfulResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

