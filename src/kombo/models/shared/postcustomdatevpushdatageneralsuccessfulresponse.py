"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from kombo import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostCustomDatevPushDataGeneralSuccessfulResponseDataFiles:
    content: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostCustomDatevPushDataGeneralSuccessfulResponseData:
    files: List[PostCustomDatevPushDataGeneralSuccessfulResponseDataFiles] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('files') }})
    


class PostCustomDatevPushDataGeneralSuccessfulResponseStatus(str, Enum):
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostCustomDatevPushDataGeneralSuccessfulResponse:
    data: PostCustomDatevPushDataGeneralSuccessfulResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    status: PostCustomDatevPushDataGeneralSuccessfulResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

