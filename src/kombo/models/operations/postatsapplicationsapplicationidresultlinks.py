"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import postatsapplicationsapplicationidresultlinkssuccessfulresponse as shared_postatsapplicationsapplicationidresultlinkssuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from kombo import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsApplicationsApplicationIDResultLinksAttributes:
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    r"""The name of the attribute"""
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""The value of the attribute"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Details:
    r"""Additional details with attributes that will be added to the result. This can be percentages, scores, or any text.

    We generally recommend using short attribute keys and a short custom_field_name_prefix to avoid overflowing the ATS UI.
    """
    attributes: List[PostAtsApplicationsApplicationIDResultLinksAttributes] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes') }})
    custom_field_name_prefix: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_field_name_prefix') }})
    r"""That will be added to the attribute labels if they are used for custom fields. If you specify `Acme:` as the prefix, the custom field will be named `Acme: Score`. Putting in the name of your company/product is a good idea."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsApplicationsApplicationIDResultLinksRequestBody:
    r"""POST /ats/applications/:application_id/result-links request body"""
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    r"""If we can display a display name for the link, we will use this label."""
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""URL of the link."""
    details: Optional[Details] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details'), 'exclude': lambda f: f is None }})
    r"""Additional details with attributes that will be added to the result. This can be percentages, scores, or any text.

    We generally recommend using short attribute keys and a short custom_field_name_prefix to avoid overflowing the ATS UI.
    """
    



@dataclasses.dataclass
class PostAtsApplicationsApplicationIDResultLinksRequest:
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    application_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'application_id', 'style': 'simple', 'explode': False }})
    r"""Kombo ID of the application you want to create the link for."""
    request_body: Optional[PostAtsApplicationsApplicationIDResultLinksRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""POST /ats/applications/:application_id/result-links request body"""
    



@dataclasses.dataclass
class PostAtsApplicationsApplicationIDResultLinksResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    post_ats_applications_application_id_result_links_successful_response: Optional[shared_postatsapplicationsapplicationidresultlinkssuccessfulresponse.PostAtsApplicationsApplicationIDResultLinksSuccessfulResponse] = dataclasses.field(default=None)
    r"""POST /ats/applications/:application_id/result-links Successful response"""
    

