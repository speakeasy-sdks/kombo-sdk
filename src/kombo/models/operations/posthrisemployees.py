"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from ...models.shared import posthrisemployeessuccessfulresponse as shared_posthrisemployeessuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from kombo import utils
from typing import Any, Dict, Optional

class PostHrisEmployeesGender(str, Enum):
    r"""The gender of the employee."""
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    NON_BINARY = 'NON_BINARY'
    NOT_SPECIFIED = 'NOT_SPECIFIED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class HomeAddress:
    r"""The employee's home address."""
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city'), 'exclude': lambda f: f is None }})
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""The uppercase two-letter ISO country (e.g., `DE`) of the employee's home address. For systems that have other formats than `ISO 3166-1 alpha-2` codes, Kombo transforms the ISO Codes to the appropriate value."""
    state: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state'), 'exclude': lambda f: f is None }})
    street_1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_1'), 'exclude': lambda f: f is None }})
    street_2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_2'), 'exclude': lambda f: f is None }})
    zip_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('zip_code'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Humaans:
    r"""Fields specific to Humaans."""
    employee: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('employee'), 'exclude': lambda f: f is None }})
    r"""Fields that we will pass through to Humaans `Employee` object."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostHrisEmployeesRemoteFields:
    r"""Additional fields that we will pass through to specific HRIS systems."""
    humaans: Optional[Humaans] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('humaans'), 'exclude': lambda f: f is None }})
    r"""Fields specific to Humaans."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostHrisEmployeesRequestBody:
    r"""POST /hris/employees request body"""
    first_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name') }})
    last_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name') }})
    work_email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('work_email') }})
    date_of_birth: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date_of_birth'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The employee's date of birth. This is a plain date (i.e., `yyyy-MM-dd`), all time information is discarded.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    gender: Optional[PostHrisEmployeesGender] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gender'), 'exclude': lambda f: f is None }})
    r"""The gender of the employee."""
    home_address: Optional[HomeAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('home_address'), 'exclude': lambda f: f is None }})
    r"""The employee's home address."""
    job_title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('job_title'), 'exclude': lambda f: f is None }})
    r"""Title of the position this person is working in."""
    mobile_phone_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mobile_phone_number'), 'exclude': lambda f: f is None }})
    nationality: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nationality'), 'exclude': lambda f: f is None }})
    r"""The uppercase two-letter ISO country (e.g., `DE`) of the employee's nationality. For systems that have other formats than `ISO 3166-1 alpha-2` codes, Kombo transforms the ISO Codes to the appropriate value."""
    remote_fields: Optional[PostHrisEmployeesRemoteFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_fields'), 'exclude': lambda f: f is None }})
    r"""Additional fields that we will pass through to specific HRIS systems."""
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""Start date of the employee. Also considered to be the hire date. This is a plain date (i.e., `yyyy-MM-dd`), all time information is discarded.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    



@dataclasses.dataclass
class PostHrisEmployeesRequest:
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    request_body: Optional[PostHrisEmployeesRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""POST /hris/employees request body"""
    



@dataclasses.dataclass
class PostHrisEmployeesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    post_hris_employees_successful_response: Optional[shared_posthrisemployeessuccessfulresponse.PostHrisEmployeesSuccessfulResponse] = dataclasses.field(default=None)
    r"""POST /hris/employees Successful response"""
    

