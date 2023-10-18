"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from kombo import utils
from typing import Any, Dict, List, Optional, Union

class GetHrisEmploymentsSuccessfulResponseDataResultsEmploymentType1(str, Enum):
    r"""One of 8 standardized values (`FULL_TIME`, `PART_TIME`, `CONTRACT`, `INTERNSHIP`, `FREELANCE`, `WORKING_STUDENT`, `APPRENTICESHIP`, or `TRAINING`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    FULL_TIME = 'FULL_TIME'
    PART_TIME = 'PART_TIME'
    CONTRACT = 'CONTRACT'
    INTERNSHIP = 'INTERNSHIP'
    FREELANCE = 'FREELANCE'
    WORKING_STUDENT = 'WORKING_STUDENT'
    APPRENTICESHIP = 'APPRENTICESHIP'
    TRAINING = 'TRAINING'


@dataclasses.dataclass
class GetHrisEmploymentsSuccessfulResponseDataResultsEmploymentType:
    pass

class GetHrisEmploymentsSuccessfulResponseDataResultsPayFrequency1(str, Enum):
    r"""One of 9 standardized values (`DAILY`, `WEEKLY`, `BIWEEKLY`, `MONTHLY`, `SEMIMONTHLY`, `QUARTERLY`, `SEMIANNUALLY`, `ANNUALLY`, or `PRO_RATA`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    BIWEEKLY = 'BIWEEKLY'
    MONTHLY = 'MONTHLY'
    SEMIMONTHLY = 'SEMIMONTHLY'
    QUARTERLY = 'QUARTERLY'
    SEMIANNUALLY = 'SEMIANNUALLY'
    ANNUALLY = 'ANNUALLY'
    PRO_RATA = 'PRO_RATA'


@dataclasses.dataclass
class GetHrisEmploymentsSuccessfulResponseDataResultsPayFrequency:
    pass

class GetHrisEmploymentsSuccessfulResponseDataResultsPayPeriod1(str, Enum):
    r"""One of 10 standardized values (`HOUR`, `DAY`, `WEEK`, `TWO_WEEKS`, `HALF_MONTH`, `MONTH`, `TWO_MONTHS`, `QUARTER`, `HALF_YEAR`, or `YEAR`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    HOUR = 'HOUR'
    DAY = 'DAY'
    WEEK = 'WEEK'
    TWO_WEEKS = 'TWO_WEEKS'
    HALF_MONTH = 'HALF_MONTH'
    MONTH = 'MONTH'
    TWO_MONTHS = 'TWO_MONTHS'
    QUARTER = 'QUARTER'
    HALF_YEAR = 'HALF_YEAR'
    YEAR = 'YEAR'


@dataclasses.dataclass
class GetHrisEmploymentsSuccessfulResponseDataResultsPayPeriod:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetHrisEmploymentsSuccessfulResponseDataResults:
    changed_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changed_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""YYYY-MM-DDTHH:mm:ss.sssZ
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    effective_date: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('effective_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""YYYY-MM-DDTHH:mm:ss.sssZ
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    employee_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employee_id') }})
    employment_type: Optional[Union[GetHrisEmploymentsSuccessfulResponseDataResultsEmploymentType1, str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employment_type') }})
    r"""One of 8 standardized values (`FULL_TIME`, `PART_TIME`, `CONTRACT`, `INTERNSHIP`, `FREELANCE`, `WORKING_STUDENT`, `APPRENTICESHIP`, or `TRAINING`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    job_title: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('job_title') }})
    r"""**(⚠️ Deprecated)** We now provide the `job_title` directly on the employee model."""
    pay_currency: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_currency') }})
    r"""Pay currency usually returned in [ISO 4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html)."""
    pay_frequency: Optional[Union[GetHrisEmploymentsSuccessfulResponseDataResultsPayFrequency1, str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_frequency') }})
    r"""One of 9 standardized values (`DAILY`, `WEEKLY`, `BIWEEKLY`, `MONTHLY`, `SEMIMONTHLY`, `QUARTERLY`, `SEMIANNUALLY`, `ANNUALLY`, or `PRO_RATA`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    pay_period: Optional[Union[GetHrisEmploymentsSuccessfulResponseDataResultsPayPeriod1, str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_period') }})
    r"""One of 10 standardized values (`HOUR`, `DAY`, `WEEK`, `TWO_WEEKS`, `HALF_MONTH`, `MONTH`, `TWO_MONTHS`, `QUARTER`, `HALF_YEAR`, or `YEAR`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    pay_rate: Optional[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_rate') }})
    remote_data: Optional[Dict[str, Any]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_data') }})
    remote_deleted_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_deleted_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""YYYY-MM-DDTHH:mm:ss.sssZ
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    remote_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_id') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetHrisEmploymentsSuccessfulResponseData:
    next: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next') }})
    r"""Cursor string that can be passed to the `cursor` query parameter to get the next page. If this is `null`, then there are no more pages."""
    results: List[GetHrisEmploymentsSuccessfulResponseDataResults] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results') }})
    


class GetHrisEmploymentsSuccessfulResponseStatus(str, Enum):
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetHrisEmploymentsSuccessfulResponse:
    data: GetHrisEmploymentsSuccessfulResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    status: GetHrisEmploymentsSuccessfulResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

