"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from speakeasybar import utils

class GetCustomDatevDataPushesSuccessfulResponseDataDataPushesType(str, Enum):
    r"""Type of the executed data push."""
    GENERAL = 'GENERAL'
    PAYROLL = 'PAYROLL'

class GetCustomDatevDataPushesSuccessfulResponseDataDataPushesUploadJobsState(str, Enum):
    r"""If we were not able to send the file to DATEV, we will set the state \\"FAILED\\". The other values are synced from DATEV for the respective import jobs."""
    FAILED = 'FAILED'
    UPLOADED = 'UPLOADED'
    IMPORTED = 'IMPORTED'
    CORRUPTED = 'CORRUPTED'
    DELETED = 'DELETED'
    AUTO_DELETED = 'AUTO_DELETED'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetCustomDatevDataPushesSuccessfulResponseDataDataPushesUploadJobs:
    file: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file') }})
    r"""Actual content of the file."""
    file_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    state: GetCustomDatevDataPushesSuccessfulResponseDataDataPushesUploadJobsState = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    r"""If we were not able to send the file to DATEV, we will set the state \\"FAILED\\". The other values are synced from DATEV for the respective import jobs."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetCustomDatevDataPushesSuccessfulResponseDataDataPushes:
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Date when the push-data endpoint was called.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    type: GetCustomDatevDataPushesSuccessfulResponseDataDataPushesType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Type of the executed data push."""
    upload_jobs: list[GetCustomDatevDataPushesSuccessfulResponseDataDataPushesUploadJobs] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upload_jobs') }})
    r"""List of all the submitted files. This can include multiple files if data was edited for multiple months."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetCustomDatevDataPushesSuccessfulResponseData:
    data_pushes: list[GetCustomDatevDataPushesSuccessfulResponseDataDataPushes] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_pushes') }})
    


class GetCustomDatevDataPushesSuccessfulResponseStatus(str, Enum):
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetCustomDatevDataPushesSuccessfulResponse:
    data: GetCustomDatevDataPushesSuccessfulResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    status: GetCustomDatevDataPushesSuccessfulResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

