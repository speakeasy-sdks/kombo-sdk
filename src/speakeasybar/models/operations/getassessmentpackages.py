"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getassessmentpackageserrorresponse as shared_getassessmentpackageserrorresponse
from ..shared import getassessmentpackagessuccessfulresponse as shared_getassessmentpackagessuccessfulresponse
from typing import Optional



@dataclasses.dataclass
class GetAssessmentPackagesRequest:
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    




@dataclasses.dataclass
class GetAssessmentPackagesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_assessment_packages_error_response: Optional[shared_getassessmentpackageserrorresponse.GetAssessmentPackagesErrorResponse] = dataclasses.field(default=None)
    r"""GET /assessment/packages Error response"""
    get_assessment_packages_successful_response: Optional[shared_getassessmentpackagessuccessfulresponse.GetAssessmentPackagesSuccessfulResponse] = dataclasses.field(default=None)
    r"""GET /assessment/packages Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

