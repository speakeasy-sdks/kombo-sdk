"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from kombo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponse503Error:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponse503Status(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponse503ResponseBody(Exception):
    r"""Returned when no sync has finished successfully yet"""
    error: PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponse503Error = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponse503Status = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponseError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponseStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponseResponseBody(Exception):
    r"""Returned when a requested resource is not found."""
    error: PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponseError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponseBody(Exception):
    r"""Returned when the passed integration is inactive."""
    error: PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutCustomDatevEmployeesEmployeeIDPreparePayrollError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PutCustomDatevEmployeesEmployeeIDPreparePayrollStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutCustomDatevEmployeesEmployeeIDPreparePayrollResponseBody(Exception):
    r"""Returned when the authentication header was invalid or missing."""
    error: PutCustomDatevEmployeesEmployeeIDPreparePayrollError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PutCustomDatevEmployeesEmployeeIDPreparePayrollStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)