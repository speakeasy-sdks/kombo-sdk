"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from kombo import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAssessmentPackagesErrorResponseError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PutAssessmentPackagesErrorResponseStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAssessmentPackagesErrorResponse:
    error: PutAssessmentPackagesErrorResponseError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PutAssessmentPackagesErrorResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

