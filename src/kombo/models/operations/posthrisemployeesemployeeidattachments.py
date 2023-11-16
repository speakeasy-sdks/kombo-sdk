"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import posthrisemployeesemployeeidattachmentsrequestbody as shared_posthrisemployeesemployeeidattachmentsrequestbody
from ...models.shared import posthrisemployeesemployeeidattachmentssuccessfulresponse as shared_posthrisemployeesemployeeidattachmentssuccessfulresponse
from typing import Optional


@dataclasses.dataclass
class PostHrisEmployeesEmployeeIDAttachmentsRequest:
    employee_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'employee_id', 'style': 'simple', 'explode': False }})
    r"""POST /hris/employees/:employee_id/attachments parameter"""
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    post_hris_employees_employee_id_attachments_request_body: Optional[shared_posthrisemployeesemployeeidattachmentsrequestbody.PostHrisEmployeesEmployeeIDAttachmentsRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""POST /hris/employees/:employee_id/attachments request body"""
    



@dataclasses.dataclass
class PostHrisEmployeesEmployeeIDAttachmentsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    post_hris_employees_employee_id_attachments_successful_response: Optional[shared_posthrisemployeesemployeeidattachmentssuccessfulresponse.PostHrisEmployeesEmployeeIDAttachmentsSuccessfulResponse] = dataclasses.field(default=None)
    r"""POST /hris/employees/:employee_id/attachments Successful response"""
    

