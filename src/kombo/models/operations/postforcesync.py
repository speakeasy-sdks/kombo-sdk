"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import postforcesyncrequestbody as shared_postforcesyncrequestbody
from ...models.shared import postforcesyncsuccessfulresponse as shared_postforcesyncsuccessfulresponse
from typing import Optional


@dataclasses.dataclass
class PostForceSyncRequest:
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    post_force_sync_request_body: Optional[shared_postforcesyncrequestbody.PostForceSyncRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""POST /force-sync request body"""
    



@dataclasses.dataclass
class PostForceSyncResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    post_force_sync_successful_response: Optional[shared_postforcesyncsuccessfulresponse.PostForceSyncSuccessfulResponse] = dataclasses.field(default=None)
    r"""POST /force-sync Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

