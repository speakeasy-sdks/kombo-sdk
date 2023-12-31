"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import postatsapplicationsapplicationidnoteserrorresponse as shared_postatsapplicationsapplicationidnoteserrorresponse
from ..shared import postatsapplicationsapplicationidnotessuccessfulresponse as shared_postatsapplicationsapplicationidnotessuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from kombo import utils
from typing import Optional

class PostAtsApplicationsApplicationIDNotesRequestBodyContentType(str, Enum):
    r"""Content type of the note. Currently only `PLAIN_TEXT` is supported."""
    PLAIN_TEXT = 'PLAIN_TEXT'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotesRequestBodyRemoteFieldsTeamtailor:
    r"""Teamtailor specific remote fields for the note."""
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id'), 'exclude': lambda f: f is None }})
    r"""ID of the user that created the note. Defaults to the first admin user found."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotesRequestBodyRemoteFields:
    r"""Tool specific remote fields for the note."""
    teamtailor: Optional[PostAtsApplicationsApplicationIDNotesRequestBodyRemoteFieldsTeamtailor] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('teamtailor'), 'exclude': lambda f: f is None }})
    r"""Teamtailor specific remote fields for the note."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotesRequestBody:
    r"""POST /ats/applications/:application_id/notes request body"""
    content: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content') }})
    r"""UTF-8 content of the note."""
    content_type: PostAtsApplicationsApplicationIDNotesRequestBodyContentType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content_type') }})
    r"""Content type of the note. Currently only `PLAIN_TEXT` is supported."""
    remote_fields: Optional[PostAtsApplicationsApplicationIDNotesRequestBodyRemoteFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_fields'), 'exclude': lambda f: f is None }})
    r"""Tool specific remote fields for the note."""
    




@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotesRequest:
    application_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'application_id', 'style': 'simple', 'explode': False }})
    r"""Kombo ID of the application you want to create the note for."""
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    request_body: Optional[PostAtsApplicationsApplicationIDNotesRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""POST /ats/applications/:application_id/notes request body"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotes503ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostAtsApplicationsApplicationIDNotes503ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotes503ApplicationJSON:
    r"""Returned when no sync has finished successfully yet"""
    error: PostAtsApplicationsApplicationIDNotes503ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostAtsApplicationsApplicationIDNotes503ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotes404ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostAtsApplicationsApplicationIDNotes404ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotes404ApplicationJSON:
    r"""Returned when a requested resource is not found."""
    error: PostAtsApplicationsApplicationIDNotes404ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostAtsApplicationsApplicationIDNotes404ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotes403ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostAtsApplicationsApplicationIDNotes403ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotes403ApplicationJSON:
    r"""Returned when the passed integration is inactive."""
    error: PostAtsApplicationsApplicationIDNotes403ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostAtsApplicationsApplicationIDNotes403ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotes401ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostAtsApplicationsApplicationIDNotes401ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotes401ApplicationJSON:
    r"""Returned when the authentication header was invalid or missing."""
    error: PostAtsApplicationsApplicationIDNotes401ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostAtsApplicationsApplicationIDNotes401ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    




@dataclasses.dataclass
class PostAtsApplicationsApplicationIDNotesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    post_ats_applications_application_id_notes_401_application_json_object: Optional[PostAtsApplicationsApplicationIDNotes401ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the authentication header was invalid or missing."""
    post_ats_applications_application_id_notes_403_application_json_object: Optional[PostAtsApplicationsApplicationIDNotes403ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the passed integration is inactive."""
    post_ats_applications_application_id_notes_404_application_json_object: Optional[PostAtsApplicationsApplicationIDNotes404ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when a requested resource is not found."""
    post_ats_applications_application_id_notes_503_application_json_object: Optional[PostAtsApplicationsApplicationIDNotes503ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when no sync has finished successfully yet"""
    post_ats_applications_application_id_notes_error_response: Optional[shared_postatsapplicationsapplicationidnoteserrorresponse.PostAtsApplicationsApplicationIDNotesErrorResponse] = dataclasses.field(default=None)
    r"""POST /ats/applications/:application_id/notes Error response"""
    post_ats_applications_application_id_notes_successful_response: Optional[shared_postatsapplicationsapplicationidnotessuccessfulresponse.PostAtsApplicationsApplicationIDNotesSuccessfulResponse] = dataclasses.field(default=None)
    r"""POST /ats/applications/:application_id/notes Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

