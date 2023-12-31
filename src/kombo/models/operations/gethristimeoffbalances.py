"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import gethristimeoffbalanceserrorresponse as shared_gethristimeoffbalanceserrorresponse
from ..shared import gethristimeoffbalancesparameterincludedeleted as shared_gethristimeoffbalancesparameterincludedeleted
from ..shared import gethristimeoffbalancessuccessfulresponse as shared_gethristimeoffbalancessuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from kombo import utils
from typing import Optional



@dataclasses.dataclass
class GetHrisTimeOffBalancesRequest:
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""An optional cursor string used for pagination. This can be retrieved from the `next` property of the previous page response."""
    employee_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'employee_id', 'style': 'form', 'explode': True }})
    r"""Filter by a specific employee using their ID."""
    ids: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ids', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of IDs such as `222k7eCGyUdgt2JWZDNnkDs3,B5DVmypWENfU6eMe6gYDyJG3`."""
    include_deleted: Optional[shared_gethristimeoffbalancesparameterincludedeleted.GetHrisTimeOffBalancesParameterIncludeDeleted] = dataclasses.field(default=shared_gethristimeoffbalancesparameterincludedeleted.GetHrisTimeOffBalancesParameterIncludeDeleted.FALSE, metadata={'query_param': { 'field_name': 'include_deleted', 'style': 'form', 'explode': True }})
    r"""By default, deleted entries are not returned. Use the `include_deleted` query param to include deleted entries too."""
    page_size: Optional[int] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    r"""The number of results to return per page."""
    remote_ids: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'remote_ids', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of remote IDs."""
    updated_after: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updated_after', 'style': 'form', 'explode': True }})
    r"""Filter the entries based on the modification date. If you want to track entry deletion, also set the `include_deleted=true` query parameter, because otherwise, deleted entries will be hidden."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisTimeOffBalances503ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetHrisTimeOffBalances503ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisTimeOffBalances503ApplicationJSON:
    r"""Returned when no sync has finished successfully yet"""
    error: GetHrisTimeOffBalances503ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetHrisTimeOffBalances503ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisTimeOffBalances404ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetHrisTimeOffBalances404ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisTimeOffBalances404ApplicationJSON:
    r"""Returned when a requested resource is not found."""
    error: GetHrisTimeOffBalances404ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetHrisTimeOffBalances404ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisTimeOffBalances403ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetHrisTimeOffBalances403ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisTimeOffBalances403ApplicationJSON:
    r"""Returned when the passed integration is inactive."""
    error: GetHrisTimeOffBalances403ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetHrisTimeOffBalances403ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisTimeOffBalances401ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetHrisTimeOffBalances401ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisTimeOffBalances401ApplicationJSON:
    r"""Returned when the authentication header was invalid or missing."""
    error: GetHrisTimeOffBalances401ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetHrisTimeOffBalances401ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    




@dataclasses.dataclass
class GetHrisTimeOffBalancesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_hris_time_off_balances_401_application_json_object: Optional[GetHrisTimeOffBalances401ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the authentication header was invalid or missing."""
    get_hris_time_off_balances_403_application_json_object: Optional[GetHrisTimeOffBalances403ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the passed integration is inactive."""
    get_hris_time_off_balances_404_application_json_object: Optional[GetHrisTimeOffBalances404ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when a requested resource is not found."""
    get_hris_time_off_balances_503_application_json_object: Optional[GetHrisTimeOffBalances503ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when no sync has finished successfully yet"""
    get_hris_time_off_balances_error_response: Optional[shared_gethristimeoffbalanceserrorresponse.GetHrisTimeOffBalancesErrorResponse] = dataclasses.field(default=None)
    r"""GET /hris/time-off-balances Error response"""
    get_hris_time_off_balances_successful_response: Optional[shared_gethristimeoffbalancessuccessfulresponse.GetHrisTimeOffBalancesSuccessfulResponse] = dataclasses.field(default=None)
    r"""GET /hris/time-off-balances Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

