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
class GetHrisLegalEntitiesSuccessfulResponseDataResultsAddress:
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
class GetHrisLegalEntitiesSuccessfulResponseDataResults:
    address: Optional[GetHrisLegalEntitiesSuccessfulResponseDataResultsAddress] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    changed_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('changed_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The timestamp when this object was last changed. This value is tracked by Kombo based on changes in the data.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The globally unique ID of this object generated by Kombo. We recommend using this as a stable primary key for syncing."""
    name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    remote_data: Optional[dict[str, Any]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_data') }})
    remote_deleted_at: Optional[datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_deleted_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date and time the object was deleted in the remote system. Objects are automatically marked as deleted when Kombo can't retrieve them from the remote system anymore. Kombo will also anonymize entries 14 days after they disappear.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    remote_id: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_id') }})
    r"""The raw ID of the object in the remote system. We don't recommend using this as a primary key on your side as it might sometimes be compromised of multiple identifiers if a system doesn't provide a clear primary key."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisLegalEntitiesSuccessfulResponseData:
    next: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next') }})
    r"""Cursor string that can be passed to the `cursor` query parameter to get the next page. If this is `null`, then there are no more pages."""
    results: list[GetHrisLegalEntitiesSuccessfulResponseDataResults] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results') }})
    


class GetHrisLegalEntitiesSuccessfulResponseStatus(str, Enum):
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetHrisLegalEntitiesSuccessfulResponse:
    data: GetHrisLegalEntitiesSuccessfulResponseData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    status: GetHrisLegalEntitiesSuccessfulResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    
