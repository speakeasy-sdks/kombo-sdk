"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import putatsapplicationsapplicationidstageerrorresponse as shared_putatsapplicationsapplicationidstageerrorresponse
from ..shared import putatsapplicationsapplicationidstagesuccessfulresponse as shared_putatsapplicationsapplicationidstagesuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from kombo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStageRequestBodyRemoteFieldsGreenhousePostHeaders:
    r"""Headers we will pass with `POST` requests to Greenhouse."""
    on_behalf_of: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('On-Behalf-Of') }})
    r"""ID of the the user that will show up as having performed the action in Greenhouse. We already pass a value by default, but you can use this to override it."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStageRequestBodyRemoteFieldsGreenhouse:
    r"""Fields specific to Greenhouse."""
    post_headers: Optional[PutAtsApplicationsApplicationIDStageRequestBodyRemoteFieldsGreenhousePostHeaders] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('post_headers'), 'exclude': lambda f: f is None }})
    r"""Headers we will pass with `POST` requests to Greenhouse."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStageRequestBodyRemoteFields:
    r"""Additional fields that we will pass through to specific ATS systems."""
    greenhouse: Optional[PutAtsApplicationsApplicationIDStageRequestBodyRemoteFieldsGreenhouse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('greenhouse'), 'exclude': lambda f: f is None }})
    r"""Fields specific to Greenhouse."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStageRequestBody:
    r"""PUT /ats/applications/:application_id/stage request body"""
    stage_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stage_id') }})
    r"""The ID of the stage to move the application to. This ID must be the ID of a stage that is connected to the job that the application is connected to."""
    remote_fields: Optional[PutAtsApplicationsApplicationIDStageRequestBodyRemoteFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_fields'), 'exclude': lambda f: f is None }})
    r"""Additional fields that we will pass through to specific ATS systems."""
    




@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStageRequest:
    application_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'application_id', 'style': 'simple', 'explode': False }})
    r"""PUT /ats/applications/:application_id/stage parameter"""
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    request_body: Optional[PutAtsApplicationsApplicationIDStageRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""PUT /ats/applications/:application_id/stage request body"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStage503ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PutAtsApplicationsApplicationIDStage503ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStage503ApplicationJSON:
    r"""Returned when no sync has finished successfully yet"""
    error: PutAtsApplicationsApplicationIDStage503ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PutAtsApplicationsApplicationIDStage503ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStage404ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PutAtsApplicationsApplicationIDStage404ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStage404ApplicationJSON:
    r"""Returned when a requested resource is not found."""
    error: PutAtsApplicationsApplicationIDStage404ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PutAtsApplicationsApplicationIDStage404ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStage403ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PutAtsApplicationsApplicationIDStage403ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStage403ApplicationJSON:
    r"""Returned when the passed integration is inactive."""
    error: PutAtsApplicationsApplicationIDStage403ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PutAtsApplicationsApplicationIDStage403ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStage401ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PutAtsApplicationsApplicationIDStage401ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStage401ApplicationJSON:
    r"""Returned when the authentication header was invalid or missing."""
    error: PutAtsApplicationsApplicationIDStage401ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PutAtsApplicationsApplicationIDStage401ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    




@dataclasses.dataclass
class PutAtsApplicationsApplicationIDStageResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    put_ats_applications_application_id_stage_401_application_json_object: Optional[PutAtsApplicationsApplicationIDStage401ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the authentication header was invalid or missing."""
    put_ats_applications_application_id_stage_403_application_json_object: Optional[PutAtsApplicationsApplicationIDStage403ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the passed integration is inactive."""
    put_ats_applications_application_id_stage_404_application_json_object: Optional[PutAtsApplicationsApplicationIDStage404ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when a requested resource is not found."""
    put_ats_applications_application_id_stage_503_application_json_object: Optional[PutAtsApplicationsApplicationIDStage503ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when no sync has finished successfully yet"""
    put_ats_applications_application_id_stage_error_response: Optional[shared_putatsapplicationsapplicationidstageerrorresponse.PutAtsApplicationsApplicationIDStageErrorResponse] = dataclasses.field(default=None)
    r"""PUT /ats/applications/:application_id/stage Error response"""
    put_ats_applications_application_id_stage_successful_response: Optional[shared_putatsapplicationsapplicationidstagesuccessfulresponse.PutAtsApplicationsApplicationIDStageSuccessfulResponse] = dataclasses.field(default=None)
    r"""PUT /ats/applications/:application_id/stage Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
