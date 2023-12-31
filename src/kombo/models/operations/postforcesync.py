"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import postforcesyncerrorresponse as shared_postforcesyncerrorresponse
from ..shared import postforcesyncrequestbody as shared_postforcesyncrequestbody
from ..shared import postforcesyncsuccessfulresponse as shared_postforcesyncsuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from kombo import utils
from typing import Optional



@dataclasses.dataclass
class PostForceSyncRequest:
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    post_force_sync_request_body: Optional[shared_postforcesyncrequestbody.PostForceSyncRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""POST /force-sync request body"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostForceSync401ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostForceSync401ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostForceSync401ApplicationJSON:
    r"""Returned when the authentication header was invalid or missing."""
    error: PostForceSync401ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostForceSync401ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    




@dataclasses.dataclass
class PostForceSyncResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    post_force_sync_401_application_json_object: Optional[PostForceSync401ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the authentication header was invalid or missing."""
    post_force_sync_error_response: Optional[shared_postforcesyncerrorresponse.PostForceSyncErrorResponse] = dataclasses.field(default=None)
    r"""POST /force-sync Error response"""
    post_force_sync_successful_response: Optional[shared_postforcesyncsuccessfulresponse.PostForceSyncSuccessfulResponse] = dataclasses.field(default=None)
    r"""POST /force-sync Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

