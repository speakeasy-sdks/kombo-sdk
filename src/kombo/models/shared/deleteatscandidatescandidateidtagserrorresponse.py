"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from kombo import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteAtsCandidatesCandidateIDTagsErrorResponseError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class DeleteAtsCandidatesCandidateIDTagsErrorResponseStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteAtsCandidatesCandidateIDTagsErrorResponse:
    error: DeleteAtsCandidatesCandidateIDTagsErrorResponseError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: DeleteAtsCandidatesCandidateIDTagsErrorResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

