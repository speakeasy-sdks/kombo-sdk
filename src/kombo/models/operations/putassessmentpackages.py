"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import putassessmentpackageserrorresponse as shared_putassessmentpackageserrorresponse
from ..shared import putassessmentpackagessuccessfulresponse as shared_putassessmentpackagessuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from kombo import utils
from typing import Optional

class PutAssessmentPackagesRequestBodyPackagesType(str, Enum):
    BEHAVIORAL = 'BEHAVIORAL'
    VIDEO_INTERVIEW = 'VIDEO_INTERVIEW'
    SKILLS_TEST = 'SKILLS_TEST'
    BACKGROUND_CHECK = 'BACKGROUND_CHECK'
    REFERENCE_CHECK = 'REFERENCE_CHECK'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAssessmentPackagesRequestBodyPackages:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""Description about the package. Some ATSs will display this in their UI."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""A unique identifier for the assessment package."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the assessment package."""
    type: PutAssessmentPackagesRequestBodyPackagesType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PutAssessmentPackagesRequestBody:
    r"""PUT /assessment/packages request body"""
    packages: list[PutAssessmentPackagesRequestBodyPackages] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('packages') }})
    




@dataclasses.dataclass
class PutAssessmentPackagesRequest:
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    request_body: Optional[PutAssessmentPackagesRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""PUT /assessment/packages request body"""
    




@dataclasses.dataclass
class PutAssessmentPackagesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    put_assessment_packages_error_response: Optional[shared_putassessmentpackageserrorresponse.PutAssessmentPackagesErrorResponse] = dataclasses.field(default=None)
    r"""PUT /assessment/packages Error response"""
    put_assessment_packages_successful_response: Optional[shared_putassessmentpackagessuccessfulresponse.PutAssessmentPackagesSuccessfulResponse] = dataclasses.field(default=None)
    r"""PUT /assessment/packages Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

