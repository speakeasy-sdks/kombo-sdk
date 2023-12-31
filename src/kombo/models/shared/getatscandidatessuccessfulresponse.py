"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from kombo import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsCandidatesSuccessfulResponseDataResultsApplicationsCurrentStage:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    remote_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_id') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsCandidatesSuccessfulResponseDataResultsApplicationsJob:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The globally unique ID of this object generated by Kombo. We recommend using this as a stable primary key for syncing."""
    name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Title of the job."""
    remote_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_id') }})
    r"""The raw ID of the object in the remote system. We don't recommend using this as a primary key on your side as it might sometimes be compromised of multiple identifiers if a system doesn't provide a clear primary key."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsCandidatesSuccessfulResponseDataResultsApplications:
    current_stage: Optional[GetAtsCandidatesSuccessfulResponseDataResultsApplicationsCurrentStage] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_stage') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    job: Optional[GetAtsCandidatesSuccessfulResponseDataResultsApplicationsJob] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('job') }})
    remote_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_id') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsCandidatesSuccessfulResponseDataResultsEmailAddresses:
    type: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Kombo exposes type information through this field. If we don't get any information from the tool, we will set this to `null`."""
    email_address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_address') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsCandidatesSuccessfulResponseDataResultsLocation:
    r"""Location of the candidate."""
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city') }})
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    r"""Contains the ISO2 country code if possible. If not, it contains the original value."""
    raw: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw') }})
    state: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    street_1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_1') }})
    street_2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_2') }})
    zip_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('zip_code') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsCandidatesSuccessfulResponseDataResultsPhoneNumbers:
    phone_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Kombo exposes type information through this field. If we don't get any information from the tool, we will set this to `null`."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsCandidatesSuccessfulResponseDataResultsSocialMedia:
    link: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    username: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsCandidatesSuccessfulResponseDataResultsTags:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    remote_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_id') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsCandidatesSuccessfulResponseDataResults:
    applications: list[GetAtsCandidatesSuccessfulResponseDataResultsApplications] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('applications') }})
    changed_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changed_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""YYYY-MM-DDTHH:mm:ss.sssZ
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    company: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company') }})
    r"""The current company of the candidate."""
    confidential: Optional[bool] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confidential') }})
    r"""Whether the candidate's profile is confidential in the ATS."""
    email_addresses: Optional[list[GetAtsCandidatesSuccessfulResponseDataResultsEmailAddresses]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_addresses') }})
    r"""A list of email addresses of the candidate with an optional type. If an email address is invalid, it will be filtered out."""
    first_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name') }})
    r"""First name of the candidate."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    last_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name') }})
    r"""Last name of the candidate."""
    location: Optional[GetAtsCandidatesSuccessfulResponseDataResultsLocation] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})
    r"""Location of the candidate."""
    phone_numbers: Optional[list[GetAtsCandidatesSuccessfulResponseDataResultsPhoneNumbers]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_numbers') }})
    r"""A list of phone numbers of the candidate."""
    remote_created_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""YYYY-MM-DDTHH:mm:ss.sssZ
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    remote_data: Optional[dict[str, Any]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_data') }})
    remote_deleted_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_deleted_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""YYYY-MM-DDTHH:mm:ss.sssZ
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    remote_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_id') }})
    remote_updated_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""YYYY-MM-DDTHH:mm:ss.sssZ
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    social_media: Optional[list[GetAtsCandidatesSuccessfulResponseDataResultsSocialMedia]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('social_media') }})
    r"""List of social media accounts of the candidate."""
    source: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source') }})
    tags: list[GetAtsCandidatesSuccessfulResponseDataResultsTags] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags') }})
    title: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    r"""The current job title of the candidate."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsCandidatesSuccessfulResponseData:
    next: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next') }})
    r"""Cursor string that can be passed to the `cursor` query parameter to get the next page. If this is `null`, then there are no more pages."""
    results: list[GetAtsCandidatesSuccessfulResponseDataResults] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results') }})
    


class GetAtsCandidatesSuccessfulResponseStatus(str, Enum):
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAtsCandidatesSuccessfulResponse:
    data: GetAtsCandidatesSuccessfulResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    status: GetAtsCandidatesSuccessfulResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    

