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
class GetHRISLocationsUnifiedHRISAPIResponse503Error:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetHRISLocationsUnifiedHRISAPIResponse503Status(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHRISLocationsUnifiedHRISAPIResponse503ResponseBody(Exception):
    r"""Returned when no sync has finished successfully yet"""
    error: GetHRISLocationsUnifiedHRISAPIResponse503Error = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetHRISLocationsUnifiedHRISAPIResponse503Status = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetHRISLocationsUnifiedHRISAPIResponseError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetHRISLocationsUnifiedHRISAPIResponseStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHRISLocationsUnifiedHRISAPIResponseResponseBody(Exception):
    r"""Returned when a requested resource is not found."""
    error: GetHRISLocationsUnifiedHRISAPIResponseError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetHRISLocationsUnifiedHRISAPIResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetHRISLocationsUnifiedHRISAPIError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetHRISLocationsUnifiedHRISAPIStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHRISLocationsUnifiedHRISAPIResponseBody(Exception):
    r"""Returned when the passed integration is inactive."""
    error: GetHRISLocationsUnifiedHRISAPIError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetHRISLocationsUnifiedHRISAPIStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetHrisLocationsError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetHrisLocationsStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisLocationsResponseBody(Exception):
    r"""Returned when the authentication header was invalid or missing."""
    error: GetHrisLocationsError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetHrisLocationsStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)