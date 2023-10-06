"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import postatscandidatescandidateidresultlinkserrorresponse as shared_postatscandidatescandidateidresultlinkserrorresponse
from ..shared import postatscandidatescandidateidresultlinkssuccessfulresponse as shared_postatscandidatescandidateidresultlinkssuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from speakeasybar import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinksRequestBodyDetailsAttributes:
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    r"""The name of the attribute"""
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""The value of the attribute"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinksRequestBodyDetails:
    r"""Additional details with attributes that will be added to the result. This can be percentages, scores, or any text.

    We generally recommend using short attribute keys and a short custom_field_name_prefix to avoid overflowing the ATS UI.
    """
    attributes: list[PostAtsCandidatesCandidateIDResultLinksRequestBodyDetailsAttributes] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes') }})
    custom_field_name_prefix: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_field_name_prefix') }})
    r"""That will be added to the attribute labels if they are used for custom fields. If you specify `Acme:` as the prefix, the custom field will be named `Acme: Score`. Putting in the name of your company/product is a good idea."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinksRequestBodyRemoteFieldsGreenhousePostHeaders:
    r"""Headers we will pass with `POST` requests to Greenhouse."""
    on_behalf_of: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('On-Behalf-Of') }})
    r"""ID of the the user that will show up as having performed the action in Greenhouse. We already pass a value by default, but you can use this to override it."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinksRequestBodyRemoteFieldsGreenhouse:
    r"""Fields specific to Greenhouse."""
    post_headers: Optional[PostAtsCandidatesCandidateIDResultLinksRequestBodyRemoteFieldsGreenhousePostHeaders] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('post_headers'), 'exclude': lambda f: f is None }})
    r"""Headers we will pass with `POST` requests to Greenhouse."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinksRequestBodyRemoteFields:
    r"""Additional fields that we will pass through to specific ATS systems."""
    greenhouse: Optional[PostAtsCandidatesCandidateIDResultLinksRequestBodyRemoteFieldsGreenhouse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('greenhouse'), 'exclude': lambda f: f is None }})
    r"""Fields specific to Greenhouse."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinksRequestBody:
    r"""POST /ats/candidates/:candidate_id/result-links request body"""
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    r"""If we can display a display name for the link, we will use this label."""
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""URL of the link."""
    details: Optional[PostAtsCandidatesCandidateIDResultLinksRequestBodyDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    r"""Additional details with attributes that will be added to the result. This can be percentages, scores, or any text.

    We generally recommend using short attribute keys and a short custom_field_name_prefix to avoid overflowing the ATS UI.
    """
    remote_fields: Optional[PostAtsCandidatesCandidateIDResultLinksRequestBodyRemoteFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_fields'), 'exclude': lambda f: f is None }})
    r"""Additional fields that we will pass through to specific ATS systems."""
    




@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinksRequest:
    candidate_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'candidate_id', 'style': 'simple', 'explode': False }})
    r"""Kombo ID of the candidate you want to create the link for."""
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    request_body: Optional[PostAtsCandidatesCandidateIDResultLinksRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""POST /ats/candidates/:candidate_id/result-links request body"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinks503ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostAtsCandidatesCandidateIDResultLinks503ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinks503ApplicationJSON:
    r"""Returned when no sync has finished successfully yet"""
    error: PostAtsCandidatesCandidateIDResultLinks503ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostAtsCandidatesCandidateIDResultLinks503ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinks404ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostAtsCandidatesCandidateIDResultLinks404ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinks404ApplicationJSON:
    r"""Returned when a requested resource is not found."""
    error: PostAtsCandidatesCandidateIDResultLinks404ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostAtsCandidatesCandidateIDResultLinks404ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinks403ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostAtsCandidatesCandidateIDResultLinks403ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinks403ApplicationJSON:
    r"""Returned when the passed integration is inactive."""
    error: PostAtsCandidatesCandidateIDResultLinks403ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostAtsCandidatesCandidateIDResultLinks403ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinks401ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostAtsCandidatesCandidateIDResultLinks401ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinks401ApplicationJSON:
    r"""Returned when the authentication header was invalid or missing."""
    error: PostAtsCandidatesCandidateIDResultLinks401ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostAtsCandidatesCandidateIDResultLinks401ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    




@dataclasses.dataclass
class PostAtsCandidatesCandidateIDResultLinksResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    post_ats_candidates_candidate_id_result_links_401_application_json_object: Optional[PostAtsCandidatesCandidateIDResultLinks401ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the authentication header was invalid or missing."""
    post_ats_candidates_candidate_id_result_links_403_application_json_object: Optional[PostAtsCandidatesCandidateIDResultLinks403ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the passed integration is inactive."""
    post_ats_candidates_candidate_id_result_links_404_application_json_object: Optional[PostAtsCandidatesCandidateIDResultLinks404ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when a requested resource is not found."""
    post_ats_candidates_candidate_id_result_links_503_application_json_object: Optional[PostAtsCandidatesCandidateIDResultLinks503ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when no sync has finished successfully yet"""
    post_ats_candidates_candidate_id_result_links_error_response: Optional[shared_postatscandidatescandidateidresultlinkserrorresponse.PostAtsCandidatesCandidateIDResultLinksErrorResponse] = dataclasses.field(default=None)
    r"""POST /ats/candidates/:candidate_id/result-links Error response"""
    post_ats_candidates_candidate_id_result_links_successful_response: Optional[shared_postatscandidatescandidateidresultlinkssuccessfulresponse.PostAtsCandidatesCandidateIDResultLinksSuccessfulResponse] = dataclasses.field(default=None)
    r"""POST /ats/candidates/:candidate_id/result-links Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

