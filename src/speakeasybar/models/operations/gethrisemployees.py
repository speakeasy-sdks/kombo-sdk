"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import gethrisemployeeserrorresponse as shared_gethrisemployeeserrorresponse
from ..shared import gethrisemployeesparameteremploymentstatus as shared_gethrisemployeesparameteremploymentstatus
from ..shared import gethrisemployeesparameterincludedeleted as shared_gethrisemployeesparameterincludedeleted
from ..shared import gethrisemployeessuccessfulresponse as shared_gethrisemployeessuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from speakeasybar import utils
from typing import Optional



@dataclasses.dataclass
class GetHrisEmployeesRequest:
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""An optional cursor string used for pagination. This can be retrieved from the `next` property of the previous page response."""
    employment_status: Optional[shared_gethrisemployeesparameteremploymentstatus.GetHrisEmployeesParameterEmploymentStatus] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'employment_status', 'style': 'form', 'explode': True }})
    r"""**(⚠️ Deprecated)** Filter by the `employment_status` field."""
    employment_statuses: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'employment_statuses', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of `ACTIVE`, `PENDING`, `INACTIVE`, `LEAVE`
    * `ACTIVE`: the employee is **actively employed** 
    * `PENDING`: the employee is **not actively employed yet** (but they signed their contract or are part of an onboarding process) 
    * `INACTIVE`: a full-time employee is no longer employed, or, for a contract worker when their contract runs out 
    * `LEAVE`: the employee is still employed but **currently on leave** (note that not all HR systems support this status — use our absences API for detailed information)
    """
    group_ids: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'group_ids', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of group IDs. We will only return employees that are members of _any_ of the groups."""
    ids: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ids', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of IDs such as `222k7eCGyUdgt2JWZDNnkDs3,B5DVmypWENfU6eMe6gYDyJG3`."""
    include_deleted: Optional[shared_gethrisemployeesparameterincludedeleted.GetHrisEmployeesParameterIncludeDeleted] = dataclasses.field(default=shared_gethrisemployeesparameterincludedeleted.GetHrisEmployeesParameterIncludeDeleted.FALSE, metadata={'query_param': { 'field_name': 'include_deleted', 'style': 'form', 'explode': True }})
    r"""By default, deleted entries are not returned. Use the `include_deleted` query param to include deleted entries too."""
    legal_entity_ids: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'legal_entity_ids', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of legal entity IDs. We will only return employees that are members of _any_ of the legal entities."""
    page_size: Optional[int] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    r"""The number of results to return per page."""
    personal_emails: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'personal_emails', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of personal emails. We will only return employees who have _any_ of the personal emails."""
    remote_ids: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'remote_ids', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of remote IDs."""
    updated_after: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updated_after', 'style': 'form', 'explode': True }})
    r"""Filter the entries based on the modification date. If you want to track entry deletion, also set the `include_deleted=true` query parameter, because otherwise, deleted entries will be hidden."""
    work_emails: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'work_emails', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of work emails. We will only return employees who have _any_ of the work emails."""
    work_location_ids: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'work_location_ids', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of work location IDs. We will only return employees who are at _any_ of the work locations."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisEmployees503ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetHrisEmployees503ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisEmployees503ApplicationJSON:
    r"""Returned when no sync has finished successfully yet"""
    error: GetHrisEmployees503ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetHrisEmployees503ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisEmployees404ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetHrisEmployees404ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisEmployees404ApplicationJSON:
    r"""Returned when a requested resource is not found."""
    error: GetHrisEmployees404ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetHrisEmployees404ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisEmployees403ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetHrisEmployees403ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisEmployees403ApplicationJSON:
    r"""Returned when the passed integration is inactive."""
    error: GetHrisEmployees403ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetHrisEmployees403ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisEmployees401ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetHrisEmployees401ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisEmployees401ApplicationJSON:
    r"""Returned when the authentication header was invalid or missing."""
    error: GetHrisEmployees401ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetHrisEmployees401ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    




@dataclasses.dataclass
class GetHrisEmployeesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_hris_employees_401_application_json_object: Optional[GetHrisEmployees401ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the authentication header was invalid or missing."""
    get_hris_employees_403_application_json_object: Optional[GetHrisEmployees403ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the passed integration is inactive."""
    get_hris_employees_404_application_json_object: Optional[GetHrisEmployees404ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when a requested resource is not found."""
    get_hris_employees_503_application_json_object: Optional[GetHrisEmployees503ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when no sync has finished successfully yet"""
    get_hris_employees_error_response: Optional[shared_gethrisemployeeserrorresponse.GetHrisEmployeesErrorResponse] = dataclasses.field(default=None)
    r"""GET /hris/employees Error response"""
    get_hris_employees_successful_response: Optional[shared_gethrisemployeessuccessfulresponse.GetHrisEmployeesSuccessfulResponse] = dataclasses.field(default=None)
    r"""GET /hris/employees Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

