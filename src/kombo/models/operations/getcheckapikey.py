"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getcheckapikeyerrorresponse as shared_getcheckapikeyerrorresponse
from ..shared import getcheckapikeysuccessfulresponse as shared_getcheckapikeysuccessfulresponse
from typing import Optional



@dataclasses.dataclass
class GetCheckAPIKeyResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_check_api_key_error_response: Optional[shared_getcheckapikeyerrorresponse.GetCheckAPIKeyErrorResponse] = dataclasses.field(default=None)
    r"""GET /check-api-key Error response"""
    get_check_api_key_successful_response: Optional[shared_getcheckapikeysuccessfulresponse.GetCheckAPIKeySuccessfulResponse] = dataclasses.field(default=None)
    r"""GET /check-api-key Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
