"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from speakeasybar import utils



@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotesSuccessfulResponseData:
    pass

class PostAtsApplicationsApplicationIDNotesSuccessfulResponseStatus(str, Enum):
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotesSuccessfulResponse:
    data: PostAtsApplicationsApplicationIDNotesSuccessfulResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    status: PostAtsApplicationsApplicationIDNotesSuccessfulResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

