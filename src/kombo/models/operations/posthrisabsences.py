"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from ...models.shared import posthrisabsencessuccessfulresponse as shared_posthrisabsencessuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from kombo import utils
from typing import Optional

class PostHrisAbsencesStatus(str, Enum):
    r"""Specify if the absence should be created in the requested or approved state. Please note that some tools might approve absences automatically if they were created for an absence type that does not require approval. There are more edge cases that might cause an absence to be approved automatically."""
    REQUESTED = 'REQUESTED'
    APPROVED = 'APPROVED'

class Unit(str, Enum):
    r"""Specifying this also requires specifying `amount`."""
    HOURS = 'HOURS'
    DAYS = 'DAYS'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostHrisAbsencesRequestBody:
    r"""POST /hris/absences request body"""
    absence_type_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('absence_type_id') }})
    r"""The ID of the absence type in Kombo (not its `remote_id`)."""
    employee_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employee_id') }})
    r"""The ID of the employee in Kombo or their ID in the remote system by prefixing it with `remote:` (e.g., `remote:12312`)"""
    employee_note: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employee_note') }})
    r"""A note describing the reason for this absence."""
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    r"""Specifying this also requires specifying `unit`. This is supported by very few tools."""
    end_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""When the absence ends. This is a plain date (i.e., `yyyy-MM-dd`), all time information is discarded.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    end_half_day: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_half_day'), 'exclude': lambda f: f is None }})
    r"""`true` if the absence should end in the middle of the day."""
    end_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_time'), 'exclude': lambda f: f is None }})
    r"""When the absence ends. Follows the format `HH:mm` or `HH:mm:ss` (e.g., `14:45:15`). If `end_time` is specified, `start_time` has to be specified as well."""
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""When the absence starts. This is a plain date (i.e., `yyyy-MM-dd`), all time information is discarded.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    start_half_day: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_half_day'), 'exclude': lambda f: f is None }})
    r"""`true` if the absence should start in the middle of the day."""
    start_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_time'), 'exclude': lambda f: f is None }})
    r"""When the absence begins. Follows the format `HH:mm` or `HH:mm:ss` (e.g., `14:45:15`). If `start_time` is specified, `end_time` has to be specified as well."""
    status: Optional[PostHrisAbsencesStatus] = dataclasses.field(default=PostHrisAbsencesStatus.REQUESTED, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Specify if the absence should be created in the requested or approved state. Please note that some tools might approve absences automatically if they were created for an absence type that does not require approval. There are more edge cases that might cause an absence to be approved automatically."""
    unit: Optional[Unit] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit'), 'exclude': lambda f: f is None }})
    r"""Specifying this also requires specifying `amount`."""
    



@dataclasses.dataclass
class PostHrisAbsencesRequest:
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    request_body: Optional[PostHrisAbsencesRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""POST /hris/absences request body"""
    



@dataclasses.dataclass
class PostHrisAbsencesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    post_hris_absences_successful_response: Optional[shared_posthrisabsencessuccessfulresponse.PostHrisAbsencesSuccessfulResponse] = dataclasses.field(default=None)
    r"""POST /hris/absences Successful response"""
    

