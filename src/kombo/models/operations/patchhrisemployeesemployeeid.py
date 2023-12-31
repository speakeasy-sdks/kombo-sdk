"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import patchhrisemployeesemployeeiderrorresponse as shared_patchhrisemployeesemployeeiderrorresponse
from ..shared import patchhrisemployeesemployeeidrequestbody as shared_patchhrisemployeesemployeeidrequestbody
from ..shared import patchhrisemployeesemployeeidsuccessfulresponse as shared_patchhrisemployeesemployeeidsuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from kombo import utils
from typing import Optional



@dataclasses.dataclass
class PatchHrisEmployeesEmployeeIDRequest:
    employee_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'employee_id', 'style': 'simple', 'explode': False }})
    r"""ID of the employee that should be updated. You can use their Kombo `id` or their ID in the remote system by prefixing it with `remote:` (e.g., `remote:12312`)"""
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    patch_hris_employees_employee_id_request_body: Optional[shared_patchhrisemployeesemployeeidrequestbody.PatchHrisEmployeesEmployeeIDRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""PATCH /hris/employees/:employee_id request body"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PatchHrisEmployeesEmployeeID503ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PatchHrisEmployeesEmployeeID503ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PatchHrisEmployeesEmployeeID503ApplicationJSON:
    r"""Returned when no sync has finished successfully yet"""
    error: PatchHrisEmployeesEmployeeID503ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PatchHrisEmployeesEmployeeID503ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PatchHrisEmployeesEmployeeID404ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PatchHrisEmployeesEmployeeID404ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PatchHrisEmployeesEmployeeID404ApplicationJSON:
    r"""Returned when a requested resource is not found."""
    error: PatchHrisEmployeesEmployeeID404ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PatchHrisEmployeesEmployeeID404ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PatchHrisEmployeesEmployeeID403ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PatchHrisEmployeesEmployeeID403ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PatchHrisEmployeesEmployeeID403ApplicationJSON:
    r"""Returned when the passed integration is inactive."""
    error: PatchHrisEmployeesEmployeeID403ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PatchHrisEmployeesEmployeeID403ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PatchHrisEmployeesEmployeeID401ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PatchHrisEmployeesEmployeeID401ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PatchHrisEmployeesEmployeeID401ApplicationJSON:
    r"""Returned when the authentication header was invalid or missing."""
    error: PatchHrisEmployeesEmployeeID401ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PatchHrisEmployeesEmployeeID401ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    




@dataclasses.dataclass
class PatchHrisEmployeesEmployeeIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    patch_hris_employees_employee_id_401_application_json_object: Optional[PatchHrisEmployeesEmployeeID401ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the authentication header was invalid or missing."""
    patch_hris_employees_employee_id_403_application_json_object: Optional[PatchHrisEmployeesEmployeeID403ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the passed integration is inactive."""
    patch_hris_employees_employee_id_404_application_json_object: Optional[PatchHrisEmployeesEmployeeID404ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when a requested resource is not found."""
    patch_hris_employees_employee_id_503_application_json_object: Optional[PatchHrisEmployeesEmployeeID503ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when no sync has finished successfully yet"""
    patch_hris_employees_employee_id_error_response: Optional[shared_patchhrisemployeesemployeeiderrorresponse.PatchHrisEmployeesEmployeeIDErrorResponse] = dataclasses.field(default=None)
    r"""PATCH /hris/employees/:employee_id Error response"""
    patch_hris_employees_employee_id_successful_response: Optional[shared_patchhrisemployeesemployeeidsuccessfulresponse.PatchHrisEmployeesEmployeeIDSuccessfulResponse] = dataclasses.field(default=None)
    r"""PATCH /hris/employees/:employee_id Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

