"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import patchatscandidatescandidateiderrorresponse as shared_patchatscandidatescandidateiderrorresponse
from ..shared import patchatscandidatescandidateidrequestbody as shared_patchatscandidatescandidateidrequestbody
from ..shared import patchatscandidatescandidateidsuccessfulresponse as shared_patchatscandidatescandidateidsuccessfulresponse
from typing import Optional



@dataclasses.dataclass
class PatchAtsCandidatesCandidateIDRequest:
    candidate_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'candidate_id', 'style': 'simple', 'explode': False }})
    r"""PATCH /ats/candidates/:candidate_id parameter"""
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    patch_ats_candidates_candidate_id_request_body: Optional[shared_patchatscandidatescandidateidrequestbody.PatchAtsCandidatesCandidateIDRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""PATCH /ats/candidates/:candidate_id request body"""
    




@dataclasses.dataclass
class PatchAtsCandidatesCandidateIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    patch_ats_candidates_candidate_id_error_response: Optional[shared_patchatscandidatescandidateiderrorresponse.PatchAtsCandidatesCandidateIDErrorResponse] = dataclasses.field(default=None)
    r"""PATCH /ats/candidates/:candidate_id Error response"""
    patch_ats_candidates_candidate_id_successful_response: Optional[shared_patchatscandidatescandidateidsuccessfulresponse.PatchAtsCandidatesCandidateIDSuccessfulResponse] = dataclasses.field(default=None)
    r"""PATCH /ats/candidates/:candidate_id Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

