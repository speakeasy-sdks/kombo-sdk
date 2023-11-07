"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from kombo import utils
from typing import Any, Dict, List, Optional, Union

class GetHrisAbsencesSuccessfulResponse1(str, Enum):
    r"""One of 5 standardized values (`REQUESTED`, `APPROVED`, `DECLINED`, `CANCELLED`, or `DELETED`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    REQUESTED = 'REQUESTED'
    APPROVED = 'APPROVED'
    DECLINED = 'DECLINED'
    CANCELLED = 'CANCELLED'
    DELETED = 'DELETED'


@dataclasses.dataclass
class GetHrisAbsencesSuccessfulResponseSchemasStatus:
    pass

class GetHrisAbsencesSuccessfulResponseSchemasUnit(str, Enum):
    HOURS = 'HOURS'
    DAYS = 'DAYS'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetHrisAbsencesSuccessfulResponseType:
    changed_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changed_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""YYYY-MM-DDTHH:mm:ss.sssZ
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    exact_times_supported: Optional[bool] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exact_times_supported') }})
    r"""`true` if the system supports exact times (absences with a `start_time` and an `end_time`) for this absence, `false` if not."""
    half_days_supported: Optional[bool] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('half_days_supported') }})
    r"""Whether the integration supports half-day absences (represented through `start_half_day` and `end_half_day`) for this absence type."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    remote_data: Optional[Dict[str, Any]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_data') }})
    remote_deleted_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_deleted_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""YYYY-MM-DDTHH:mm:ss.sssZ
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    remote_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_id') }})
    unit: Optional[GetHrisAbsencesSuccessfulResponseSchemasUnit] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit') }})
    


class GetHrisAbsencesSuccessfulResponseUnit(str, Enum):
    r"""The unit of time for this absence. Can be `HOURS` or `DAYS`."""
    HOURS = 'HOURS'
    DAYS = 'DAYS'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetHrisAbsencesSuccessfulResponseResults:
    amount: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The amount of time this absence takes."""
    approver_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approver_id') }})
    r"""**(⚠️ Deprecated)** The ID of the employee who is responsible for approving this absence."""
    changed_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changed_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The timestamp when this object was last changed. This value is tracked by Kombo based on changes in the data.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    employee_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employee_id') }})
    employee_note: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employee_note') }})
    r"""A note the employee has added to this absence."""
    end_date: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date') }})
    r"""The date this absence ends in the `yyyy-MM-dd` format."""
    end_half_day: Optional[bool] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_half_day') }})
    r"""`true` if the absence ends in the middle of the day, `false` if not, and `null` if the system doesn't support half-day absences."""
    end_time: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_time') }})
    r"""The time at which this absence ends. Follows the format `HH:mm:ss` (e.g., `14:45:15`)."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The globally unique ID of this object generated by Kombo. We recommend using this as a stable primary key for syncing."""
    remote_data: Optional[Dict[str, Any]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_data') }})
    remote_deleted_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_deleted_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date and time the object was deleted in the remote system. Objects are automatically marked as deleted when Kombo can't retrieve them from the remote system anymore. Kombo will also anonymize entries 14 days after they disappear.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    remote_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_id') }})
    r"""The raw ID of the object in the remote system. We don't recommend using this as a primary key on your side as it might sometimes be compromised of multiple identifiers if a system doesn't provide a clear primary key."""
    start_date: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""The date this absence starts in the `yyyy-MM-dd` format."""
    start_half_day: Optional[bool] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_half_day') }})
    r"""`true` if the absence starts in the middle of the day, `false` if not, and `null` if the system doesn't support half-day absences."""
    start_time: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_time') }})
    r"""The time at which this absence starts. Follows the format `HH:mm:ss` (e.g., `14:45:15`)."""
    status: Optional[Union[GetHrisAbsencesSuccessfulResponse1, str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""One of 5 standardized values (`REQUESTED`, `APPROVED`, `DECLINED`, `CANCELLED`, or `DELETED`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    type: Optional[GetHrisAbsencesSuccessfulResponseType] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    type_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type_id') }})
    r"""The Kombo absence type ID of this absence."""
    unit: Optional[GetHrisAbsencesSuccessfulResponseUnit] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit') }})
    r"""The unit of time for this absence. Can be `HOURS` or `DAYS`."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetHrisAbsencesSuccessfulResponseData:
    next: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next') }})
    r"""Cursor string that can be passed to the `cursor` query parameter to get the next page. If this is `null`, then there are no more pages."""
    results: List[GetHrisAbsencesSuccessfulResponseResults] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results') }})
    


class GetHrisAbsencesSuccessfulResponseStatus(str, Enum):
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetHrisAbsencesSuccessfulResponse:
    data: GetHrisAbsencesSuccessfulResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    status: GetHrisAbsencesSuccessfulResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

