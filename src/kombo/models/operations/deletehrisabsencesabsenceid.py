"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import deletehrisabsencesabsenceidrequestbody as shared_deletehrisabsencesabsenceidrequestbody
from ...models.shared import deletehrisabsencesabsenceidsuccessfulresponse as shared_deletehrisabsencesabsenceidsuccessfulresponse
from typing import Optional


@dataclasses.dataclass
class DeleteHrisAbsencesAbsenceIDRequest:
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    absence_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'absence_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the absence"""
    delete_hris_absences_absence_id_request_body: Optional[shared_deletehrisabsencesabsenceidrequestbody.DeleteHrisAbsencesAbsenceIDRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""DELETE /hris/absences/:absence_id request body"""
    



@dataclasses.dataclass
class DeleteHrisAbsencesAbsenceIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    delete_hris_absences_absence_id_successful_response: Optional[shared_deletehrisabsencesabsenceidsuccessfulresponse.DeleteHrisAbsencesAbsenceIDSuccessfulResponse] = dataclasses.field(default=None)
    r"""DELETE /hris/absences/:absence_id Successful response"""
    

