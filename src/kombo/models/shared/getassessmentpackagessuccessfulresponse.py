"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from kombo import utils
from typing import List, Optional

class Type(str, Enum):
    BEHAVIORAL = 'BEHAVIORAL'
    VIDEO_INTERVIEW = 'VIDEO_INTERVIEW'
    SKILLS_TEST = 'SKILLS_TEST'
    BACKGROUND_CHECK = 'BACKGROUND_CHECK'
    REFERENCE_CHECK = 'REFERENCE_CHECK'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Packages:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""Description about the package. Some ATSs will display this in their UI."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""A unique identifier for the assessment package."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the assessment package."""
    type: Optional[Type] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    updated_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""YYYY-MM-DDTHH:mm:ss.sssZ
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAssessmentPackagesSuccessfulResponseData:
    packages: List[Packages] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('packages') }})
    


class GetAssessmentPackagesSuccessfulResponseStatus(str, Enum):
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAssessmentPackagesSuccessfulResponse:
    data: GetAssessmentPackagesSuccessfulResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    status: GetAssessmentPackagesSuccessfulResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

