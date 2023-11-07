"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import deleteintegrationsintegrationidrequestbody as shared_deleteintegrationsintegrationidrequestbody
from ...models.shared import deleteintegrationsintegrationidsuccessfulresponse as shared_deleteintegrationsintegrationidsuccessfulresponse
from typing import Optional


@dataclasses.dataclass
class DeleteIntegrationsIntegrationIDRequest:
    integration_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'integration_id', 'style': 'simple', 'explode': False }})
    r"""DELETE /integrations/:integration_id parameter"""
    delete_integrations_integration_id_request_body: Optional[shared_deleteintegrationsintegrationidrequestbody.DeleteIntegrationsIntegrationIDRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""DELETE /integrations/:integration_id request body"""
    



@dataclasses.dataclass
class DeleteIntegrationsIntegrationIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    delete_integrations_integration_id_successful_response: Optional[shared_deleteintegrationsintegrationidsuccessfulresponse.DeleteIntegrationsIntegrationIDSuccessfulResponse] = dataclasses.field(default=None)
    r"""DELETE /integrations/:integration_id Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

