"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import putatsapplicationsapplicationidstagesuccessfulresponse as shared_putatsapplicationsapplicationidstagesuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from kombo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStagePostHeaders:
    r"""Headers we will pass with `POST` requests to Greenhouse."""
    on_behalf_of: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('On-Behalf-Of') }})
    r"""ID of the the user that will show up as having performed the action in Greenhouse. We already pass a value by default, but you can use this to override it."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStageGreenhouse:
    r"""Fields specific to Greenhouse."""
    post_headers: Optional[PutAtsApplicationsApplicationIDStagePostHeaders] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('post_headers'), 'exclude': lambda f: f is None }})
    r"""Headers we will pass with `POST` requests to Greenhouse."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStageRemoteFields:
    r"""Additional fields that we will pass through to specific ATS systems."""
    greenhouse: Optional[PutAtsApplicationsApplicationIDStageGreenhouse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('greenhouse'), 'exclude': lambda f: f is None }})
    r"""Fields specific to Greenhouse."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStageRequestBody:
    r"""PUT /ats/applications/:application_id/stage request body"""
    stage_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stage_id') }})
    r"""The ID of the stage to move the application to. This ID must be the ID of a stage that is connected to the job that the application is connected to."""
    remote_fields: Optional[PutAtsApplicationsApplicationIDStageRemoteFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_fields'), 'exclude': lambda f: f is None }})
    r"""Additional fields that we will pass through to specific ATS systems."""
    



@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStageRequest:
    application_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'application_id', 'style': 'simple', 'explode': False }})
    r"""PUT /ats/applications/:application_id/stage parameter"""
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    request_body: Optional[PutAtsApplicationsApplicationIDStageRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""PUT /ats/applications/:application_id/stage request body"""
    



@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStageResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    put_ats_applications_application_id_stage_successful_response: Optional[shared_putatsapplicationsapplicationidstagesuccessfulresponse.PutAtsApplicationsApplicationIDStageSuccessfulResponse] = dataclasses.field(default=None)
    r"""PUT /ats/applications/:application_id/stage Successful response"""
    

