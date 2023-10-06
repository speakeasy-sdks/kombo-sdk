"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from speakeasybar import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisAbsenceTypesErrorResponseError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class GetHrisAbsenceTypesErrorResponseStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisAbsenceTypesErrorResponse:
    error: GetHrisAbsenceTypesErrorResponseError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: GetHrisAbsenceTypesErrorResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

