"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from kombo import utils
from typing import Any, Dict, List, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BankAccounts:
    account_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_number') }})
    r"""The bank-specific account number. Some companies use the account number field to put the IBAN here."""
    bank_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_name') }})
    r"""The name of the bank behind this account."""
    bic: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bic') }})
    r"""The internationally unique BIC/SWIFT code identifying the bank behind this account."""
    holder_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('holder_name') }})
    r"""The name of the holder of this account."""
    iban: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iban') }})
    r"""The internationally unique IBAN identifying this account."""
    


class PatchHrisEmployeesEmployeeIDSuccessfulResponse1(str, Enum):
    r"""The current employment status of the employee:

    - `ACTIVE`: the employee is **actively employed**
    - `PENDING`: the employee is **not actively employed yet** (but they signed their contract or are part of an onboarding process)
    - `INACTIVE`: the employee is **not actively employed** anymore
    - `LEAVE`: the employee is still employed but **currently on leave** (note that not all HR systems support this status — use our absences API for detailed information)

    Please note that in rare cases, where we can't find a clear mapping, the original string is passed through.
    """
    ACTIVE = 'ACTIVE'
    PENDING = 'PENDING'
    INACTIVE = 'INACTIVE'
    LEAVE = 'LEAVE'

class PatchHrisEmployeesEmployeeIDSuccessfulResponseSchemas1(str, Enum):
    r"""One of 8 standardized values (`FULL_TIME`, `PART_TIME`, `CONTRACT`, `INTERNSHIP`, `FREELANCE`, `WORKING_STUDENT`, `APPRENTICESHIP`, or `TRAINING`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    FULL_TIME = 'FULL_TIME'
    PART_TIME = 'PART_TIME'
    CONTRACT = 'CONTRACT'
    INTERNSHIP = 'INTERNSHIP'
    FREELANCE = 'FREELANCE'
    WORKING_STUDENT = 'WORKING_STUDENT'
    APPRENTICESHIP = 'APPRENTICESHIP'
    TRAINING = 'TRAINING'

class PatchHrisEmployeesEmployeeIDSuccessfulResponseSchemasData1(str, Enum):
    r"""One of 8 standardized values (`WHITE`, `ASIAN`, `HISPANIC_LATINO`, `HAWAIIAN`, `NATIVE_AMERICAN`, `BLACK_AFRICAN_AMERICAN`, `MULTIPLE_ETHNICITIES`, or `DECLINE_TO_SPECIFY`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    WHITE = 'WHITE'
    ASIAN = 'ASIAN'
    HISPANIC_LATINO = 'HISPANIC_LATINO'
    HAWAIIAN = 'HAWAIIAN'
    NATIVE_AMERICAN = 'NATIVE_AMERICAN'
    BLACK_AFRICAN_AMERICAN = 'BLACK_AFRICAN_AMERICAN'
    MULTIPLE_ETHNICITIES = 'MULTIPLE_ETHNICITIES'
    DECLINE_TO_SPECIFY = 'DECLINE_TO_SPECIFY'

class PatchHrisEmployeesEmployeeIDSuccessfulResponseSchemasDataGender1(str, Enum):
    r"""One of 4 standardized values (`MALE`, `FEMALE`, `NON_BINARY`, or `NOT_SPECIFIED`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    NON_BINARY = 'NON_BINARY'
    NOT_SPECIFIED = 'NOT_SPECIFIED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchHrisEmployeesEmployeeIDSuccessfulResponseHomeAddress:
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city') }})
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    r"""Contains the ISO2 country code if possible. If not, it contains the original value."""
    raw: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw') }})
    state: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    street_1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_1') }})
    street_2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_2') }})
    zip_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('zip_code') }})
    


class PatchHrisEmployeesEmployeeIDSuccessfulResponseSchemasDataMaritalStatus1(str, Enum):
    r"""One of 7 standardized values (`SINGLE`, `MARRIED`, `DOMESTIC_PARTNERSHIP`, `WIDOWED`, `DIVORCED`, `SEPARATED`, or `NOT_MARRIED`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    SINGLE = 'SINGLE'
    MARRIED = 'MARRIED'
    DOMESTIC_PARTNERSHIP = 'DOMESTIC_PARTNERSHIP'
    WIDOWED = 'WIDOWED'
    DIVORCED = 'DIVORCED'
    SEPARATED = 'SEPARATED'
    NOT_MARRIED = 'NOT_MARRIED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchHrisEmployeesEmployeeIDSuccessfulResponseData:
    avatar: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('avatar') }})
    r"""URL to the employee’s avatar. This is either the raw URL from the HR system (in cases where it can be requested without short-lived authentication) _or_ a URL to a temporarily cached version of the file hosted by Kombo. Kombo will delete the cached file after its deletion in the source system."""
    bank_accounts: Optional[List[BankAccounts]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bank_accounts') }})
    changed_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changed_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The timestamp when this object was last changed. This value is tracked by Kombo based on changes in the data.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    custom_fields: Optional[Dict[str, Any]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_fields') }})
    date_of_birth: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_of_birth'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""YYYY-MM-DDTHH:mm:ss.sssZ
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    display_full_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_full_name') }})
    r"""The employee’s full name, including middle names. Not all HR systems provide an explicit display name, so we recommend falling back to `first_name` and `last_name`."""
    employee_number: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employee_number') }})
    r"""An optional, organization-internal employee number."""
    employment_status: Optional[Union[PatchHrisEmployeesEmployeeIDSuccessfulResponse1, str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employment_status') }})
    r"""The current employment status of the employee:

    - `ACTIVE`: the employee is **actively employed**
    - `PENDING`: the employee is **not actively employed yet** (but they signed their contract or are part of an onboarding process)
    - `INACTIVE`: the employee is **not actively employed** anymore
    - `LEAVE`: the employee is still employed but **currently on leave** (note that not all HR systems support this status — use our absences API for detailed information)

    Please note that in rare cases, where we can't find a clear mapping, the original string is passed through.
    """
    employment_type: Optional[Union[PatchHrisEmployeesEmployeeIDSuccessfulResponseSchemas1, str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employment_type') }})
    r"""One of 8 standardized values (`FULL_TIME`, `PART_TIME`, `CONTRACT`, `INTERNSHIP`, `FREELANCE`, `WORKING_STUDENT`, `APPRENTICESHIP`, or `TRAINING`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    ethnicity: Optional[Union[PatchHrisEmployeesEmployeeIDSuccessfulResponseSchemasData1, str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ethnicity') }})
    r"""One of 8 standardized values (`WHITE`, `ASIAN`, `HISPANIC_LATINO`, `HAWAIIAN`, `NATIVE_AMERICAN`, `BLACK_AFRICAN_AMERICAN`, `MULTIPLE_ETHNICITIES`, or `DECLINE_TO_SPECIFY`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    first_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name') }})
    r"""The employee’s first name."""
    gender: Optional[Union[PatchHrisEmployeesEmployeeIDSuccessfulResponseSchemasDataGender1, str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gender') }})
    r"""One of 4 standardized values (`MALE`, `FEMALE`, `NON_BINARY`, or `NOT_SPECIFIED`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    home_address: Optional[PatchHrisEmployeesEmployeeIDSuccessfulResponseHomeAddress] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('home_address') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The globally unique ID of this object generated by Kombo. We recommend using this as a stable primary key for syncing."""
    job_title: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('job_title') }})
    r"""The employee’s job title."""
    last_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name') }})
    r"""The employee’s last name."""
    legal_entity_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legal_entity_id') }})
    r"""The ID of the employee’s legal entity."""
    manager_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('manager_id') }})
    marital_status: Optional[Union[PatchHrisEmployeesEmployeeIDSuccessfulResponseSchemasDataMaritalStatus1, str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('marital_status') }})
    r"""One of 7 standardized values (`SINGLE`, `MARRIED`, `DOMESTIC_PARTNERSHIP`, `WIDOWED`, `DIVORCED`, `SEPARATED`, or `NOT_MARRIED`) **or** — in rare cases where can't find a clear mapping — the original string passed through."""
    mobile_phone_number: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mobile_phone_number') }})
    nationality: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nationality') }})
    r"""The employee’s nationality."""
    personal_email: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('personal_email') }})
    r"""The employee’s personal email address. If the email address is invalid, we will set this to `null`."""
    remote_created_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date and time the object was created in the remote system.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    remote_data: Optional[Dict[str, Any]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_data') }})
    remote_deleted_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_deleted_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date and time the object was deleted in the remote system. Objects are automatically marked as deleted when Kombo can't retrieve them from the remote system anymore. Kombo will also anonymize entries 14 days after they disappear.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    remote_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_id') }})
    r"""The raw ID of the object in the remote system. We don't recommend using this as a primary key on your side as it might sometimes be compromised of multiple identifiers if a system doesn't provide a clear primary key."""
    ssn: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssn') }})
    r"""Social security number"""
    start_date: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date the employee started working for the organization.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    tax_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tax_id') }})
    termination_date: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('termination_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The where the employment ends. Can be in the past or future.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    work_email: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('work_email') }})
    r"""The employee’s work email address. If the email address is invalid, we will set this to `null`."""
    work_location_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('work_location_id') }})
    r"""The ID of the employee’s work location. Can be used to retrieve the work location from the `hris_locations` endpoint."""
    


class PatchHrisEmployeesEmployeeIDSuccessfulResponseStatus(str, Enum):
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchHrisEmployeesEmployeeIDSuccessfulResponse:
    data: PatchHrisEmployeesEmployeeIDSuccessfulResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    status: PatchHrisEmployeesEmployeeIDSuccessfulResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

