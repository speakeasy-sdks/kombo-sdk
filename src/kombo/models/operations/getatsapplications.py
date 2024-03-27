"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import getatsapplicationsparameterincludedeleted as shared_getatsapplicationsparameterincludedeleted
from ...models.shared import getatsapplicationsparameteroutcome as shared_getatsapplicationsparameteroutcome
from ...models.shared import getatsapplicationssuccessfulresponse as shared_getatsapplicationssuccessfulresponse
from datetime import datetime
from typing import Optional


@dataclasses.dataclass
class GetAtsApplicationsRequest:
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""An optional cursor string used for pagination. This can be retrieved from the `next` property of the previous page response."""
    ids: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ids', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of IDs such as `222k7eCGyUdgt2JWZDNnkDs3,B5DVmypWENfU6eMe6gYDyJG3`."""
    include_deleted: Optional[shared_getatsapplicationsparameterincludedeleted.GetAtsApplicationsParameterIncludeDeleted] = dataclasses.field(default=shared_getatsapplicationsparameterincludedeleted.GetAtsApplicationsParameterIncludeDeleted.FALSE, metadata={'query_param': { 'field_name': 'include_deleted', 'style': 'form', 'explode': True }})
    r"""By default, deleted entries are not returned. Use the `include_deleted` query param to include deleted entries too."""
    outcome: Optional[shared_getatsapplicationsparameteroutcome.GetAtsApplicationsParameterOutcome] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'outcome', 'style': 'form', 'explode': True }})
    r"""**(⚠️ Deprecated)** Filter applications by outcome. This allows you to get applications that are for example `PENDING`, `HIRED`, or `DECLINED`."""
    outcomes: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'outcomes', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of `PENDING`, `HIRED`, `DECLINED`"""
    page_size: Optional[int] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'page_size', 'style': 'form', 'explode': True }})
    r"""The number of results to return per page."""
    remote_created_after: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'remote_created_after', 'style': 'form', 'explode': True }})
    r"""Filter applications by the day they were created in the remote system. This allows you to get applications that were created on or after a certain day."""
    remote_ids: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'remote_ids', 'style': 'form', 'explode': True }})
    r"""Filter by a comma-separated list of remote IDs."""
    updated_after: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updated_after', 'style': 'form', 'explode': True }})
    r"""Filter the entries based on the modification date. If you want to track entry deletion, also set the `include_deleted=true` query parameter, because otherwise, deleted entries will be hidden."""
    



@dataclasses.dataclass
class GetAtsApplicationsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_ats_applications_successful_response: Optional[shared_getatsapplicationssuccessfulresponse.GetAtsApplicationsSuccessfulResponse] = dataclasses.field(default=None)
    r"""GET /ats/applications Successful response"""
    

