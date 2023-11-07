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
class DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIResponse503Error:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIResponse503Status(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIResponse503ResponseBody(Exception):
    r"""Returned when no sync has finished successfully yet"""
    error: DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIResponse503Error = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIResponse503Status = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIResponseError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIResponseStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIResponseResponseBody(Exception):
    r"""Returned when a requested resource is not found."""
    error: DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIResponseError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIResponseBody(Exception):
    r"""Returned when the passed integration is inactive."""
    error: DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: DeleteATSCandidatesCandidateIDTagsUnifiedATSAPIStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteAtsCandidatesCandidateIDTagsError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class DeleteAtsCandidatesCandidateIDTagsStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteAtsCandidatesCandidateIDTagsResponseBody(Exception):
    r"""Returned when the authentication header was invalid or missing."""
    error: DeleteAtsCandidatesCandidateIDTagsError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: DeleteAtsCandidatesCandidateIDTagsStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    r"""Raw HTTP response; suitable for custom response parsing"""
    

    def __str__(self) -> str:
        return utils.marshal_json(self)
