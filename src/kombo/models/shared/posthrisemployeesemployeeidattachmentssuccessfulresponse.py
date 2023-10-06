"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from kombo import utils



@dataclasses.dataclass
class PostHrisEmployeesEmployeeIDAttachmentsSuccessfulResponseData:
    pass

class PostHrisEmployeesEmployeeIDAttachmentsSuccessfulResponseStatus(str, Enum):
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostHrisEmployeesEmployeeIDAttachmentsSuccessfulResponse:
    data: PostHrisEmployeesEmployeeIDAttachmentsSuccessfulResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    status: PostHrisEmployeesEmployeeIDAttachmentsSuccessfulResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    
