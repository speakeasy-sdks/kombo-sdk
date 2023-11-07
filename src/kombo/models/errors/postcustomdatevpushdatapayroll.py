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
class PostCustomDatevPushDataPayrollCustomEndpointsResponse503Error:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostCustomDatevPushDataPayrollCustomEndpointsResponse503Status(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostCustomDatevPushDataPayrollCustomEndpointsResponse503ResponseBody(Exception):
    r"""Returned when no sync has finished successfully yet"""
    error: PostCustomDatevPushDataPayrollCustomEndpointsResponse503Error = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostCustomDatevPushDataPayrollCustomEndpointsResponse503Status = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostCustomDatevPushDataPayrollCustomEndpointsResponseError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostCustomDatevPushDataPayrollCustomEndpointsResponseStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostCustomDatevPushDataPayrollCustomEndpointsResponseResponseBody(Exception):
    r"""Returned when a requested resource is not found."""
    error: PostCustomDatevPushDataPayrollCustomEndpointsResponseError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostCustomDatevPushDataPayrollCustomEndpointsResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostCustomDatevPushDataPayrollCustomEndpointsError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostCustomDatevPushDataPayrollCustomEndpointsStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostCustomDatevPushDataPayrollCustomEndpointsResponseBody(Exception):
    r"""Returned when the passed integration is inactive."""
    error: PostCustomDatevPushDataPayrollCustomEndpointsError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostCustomDatevPushDataPayrollCustomEndpointsStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostCustomDatevPushDataPayrollError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostCustomDatevPushDataPayrollStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostCustomDatevPushDataPayrollResponseBody(Exception):
    r"""Returned when the authentication header was invalid or missing."""
    error: PostCustomDatevPushDataPayrollError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostCustomDatevPushDataPayrollStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)