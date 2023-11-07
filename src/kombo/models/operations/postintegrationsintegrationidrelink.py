"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import postintegrationsintegrationidrelinksuccessfulresponse as shared_postintegrationsintegrationidrelinksuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from kombo import utils
from typing import Optional

class Language(str, Enum):
    r"""Language of the connection flow UI."""
    EN = 'en'
    DE = 'de'
    FR = 'fr'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostIntegrationsIntegrationIDRelinkRequestBody:
    r"""POST /integrations/:integration_id/relink request body"""
    language: Optional[Language] = dataclasses.field(default=Language.EN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('language'), 'exclude': lambda f: f is None }})
    r"""Language of the connection flow UI."""
    



@dataclasses.dataclass
class PostIntegrationsIntegrationIDRelinkRequest:
    integration_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'integration_id', 'style': 'simple', 'explode': False }})
    r"""POST /integrations/:integration_id/relink parameter"""
    request_body: Optional[PostIntegrationsIntegrationIDRelinkRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""POST /integrations/:integration_id/relink request body"""
    



@dataclasses.dataclass
class PostIntegrationsIntegrationIDRelinkResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    post_integrations_integration_id_relink_successful_response: Optional[shared_postintegrationsintegrationidrelinksuccessfulresponse.PostIntegrationsIntegrationIDRelinkSuccessfulResponse] = dataclasses.field(default=None)
    r"""POST /integrations/:integration_id/relink Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

