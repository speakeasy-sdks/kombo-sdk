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
class DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIResponse503Error:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIResponse503Status(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIResponse503ResponseBody(Exception):
    r"""Returned when no sync has finished successfully yet"""
    error: DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIResponse503Error = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIResponse503Status = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIResponseError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIResponseStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIResponseResponseBody(Exception):
    r"""Returned when a requested resource is not found."""
    error: DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIResponseError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIResponseBody(Exception):
    r"""Returned when the passed integration is inactive."""
    error: DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: DeleteHRISAbsencesAbsenceIDUnifiedHRISAPIStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteHrisAbsencesAbsenceIDError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class DeleteHrisAbsencesAbsenceIDStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteHrisAbsencesAbsenceIDResponseBody(Exception):
    r"""Returned when the authentication header was invalid or missing."""
    error: DeleteHrisAbsencesAbsenceIDError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: DeleteHrisAbsencesAbsenceIDStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))
