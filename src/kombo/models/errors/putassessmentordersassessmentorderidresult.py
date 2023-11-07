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
class PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponse503Error:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponse503Status(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponse503ResponseBody(Exception):
    r"""Returned when no sync has finished successfully yet"""
    error: PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponse503Error = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponse503Status = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponseError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponseStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponseResponseBody(Exception):
    r"""Returned when a requested resource is not found."""
    error: PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponseError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponseBody(Exception):
    r"""Returned when the passed integration is inactive."""
    error: PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutAssessmentOrdersAssessmentOrderIDResultError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PutAssessmentOrdersAssessmentOrderIDResultStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAssessmentOrdersAssessmentOrderIDResultResponseBody(Exception):
    r"""Returned when the authentication header was invalid or missing."""
    error: PutAssessmentOrdersAssessmentOrderIDResultError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PutAssessmentOrdersAssessmentOrderIDResultStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)
