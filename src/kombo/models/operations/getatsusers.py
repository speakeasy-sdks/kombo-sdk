"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getatsuserserrorresponse as shared_getatsuserserrorresponse
from ..shared import getatsusersparameterincludedeleted as shared_getatsusersparameterincludedeleted
from ..shared import getatsuserssuccessfulresponse as shared_getatsuserssuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from kombo import utils
from typing import Optional



@dataclasses.dataclass
class GetAtsUsersRequest:
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""An optional cursor string used for pagination. This can be retrieved from the `next` property of the previous page response."""
    ids: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ids', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of IDs such as `222k7eCGyUdgt2JWZDNnkDs3,B5DVmypWENfU6eMe6gYDyJG3`."""
    include_deleted: Optional[shared_getatsusersparameterincludedeleted.GetAtsUsersParameterIncludeDeleted] = dataclasses.field(default=shared_getatsusersparameterincludedeleted.GetAtsUsersParameterIncludeDeleted.FALSE, metadata={'query_param': { 'field_name': 'include_deleted', 'style': 'form', 'explode': True }})
    r"""By default, deleted entries are not returned. Use the `include_deleted` query param to include deleted entries too."""
    page_size: Optional[int] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    r"""The number of results to return per page."""
    remote_ids: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'remote_ids', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of remote IDs."""
    updated_after: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updated_after', 'style': 'form', 'explode': True }})
    r"""Filter the entries based on the modification date. If you want to track entry deletion, also set the `include_deleted=true` query parameter, because otherwise, deleted entries will be hidden."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsUsers503ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetAtsUsers503ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsUsers503ApplicationJSON:
    r"""Returned when no sync has finished successfully yet"""
    error: GetAtsUsers503ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetAtsUsers503ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsUsers404ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetAtsUsers404ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsUsers404ApplicationJSON:
    r"""Returned when a requested resource is not found."""
    error: GetAtsUsers404ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetAtsUsers404ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsUsers403ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetAtsUsers403ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsUsers403ApplicationJSON:
    r"""Returned when the passed integration is inactive."""
    error: GetAtsUsers403ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetAtsUsers403ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsUsers401ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetAtsUsers401ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsUsers401ApplicationJSON:
    r"""Returned when the authentication header was invalid or missing."""
    error: GetAtsUsers401ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetAtsUsers401ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    




@dataclasses.dataclass
class GetAtsUsersResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_ats_users_401_application_json_object: Optional[GetAtsUsers401ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the authentication header was invalid or missing."""
    get_ats_users_403_application_json_object: Optional[GetAtsUsers403ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the passed integration is inactive."""
    get_ats_users_404_application_json_object: Optional[GetAtsUsers404ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when a requested resource is not found."""
    get_ats_users_503_application_json_object: Optional[GetAtsUsers503ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when no sync has finished successfully yet"""
    get_ats_users_error_response: Optional[shared_getatsuserserrorresponse.GetAtsUsersErrorResponse] = dataclasses.field(default=None)
    r"""GET /ats/users Error response"""
    get_ats_users_successful_response: Optional[shared_getatsuserssuccessfulresponse.GetAtsUsersSuccessfulResponse] = dataclasses.field(default=None)
    r"""GET /ats/users Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
