"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import postconnectcreatelinksuccessfulresponse as shared_postconnectcreatelinksuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from kombo import utils
from typing import Optional

class IntegrationCategory(str, Enum):
    r"""Category of the integration you want your customer to create."""
    HRIS = 'HRIS'
    ATS = 'ATS'
    ASSESSMENT = 'ASSESSMENT'

class IntegrationTool(str, Enum):
    r"""Pre-define a tool this integration link can be used for."""
    PERSONIO = 'personio'
    WORKDAY = 'workday'
    SUCCESSFACTORS = 'successfactors'
    SMARTRECRUITERS = 'smartrecruiters'
    FACTORIAL = 'factorial'
    LEVER = 'lever'
    RECRUITEE = 'recruitee'
    GREENHOUSE = 'greenhouse'
    TEAMTAILOR = 'teamtailor'
    ASHBY = 'ashby'
    ONLYFY = 'onlyfy'
    REXX = 'rexx'
    AFAS = 'afas'
    BAMBOOHR = 'bamboohr'
    BULLHORN = 'bullhorn'
    WORKABLE = 'workable'
    PAYFIT = 'payfit'
    FOUNTAIN = 'fountain'
    KENJO = 'kenjo'
    HEAVENHR = 'heavenhr'
    HIBOB = 'hibob'
    SOFTGARDEN = 'softgarden'
    AZUREAD = 'azuread'
    GOOGLEWORKSPACE = 'googleworkspace'
    PINPOINT = 'pinpoint'
    WELCOMETOTHEJUNGLE = 'welcometothejungle'
    DVINCI = 'dvinci'
    JOIN = 'join'
    DEEL = 'deel'
    REMOTECOM = 'remotecom'
    JOBVITE = 'jobvite'
    OKTA = 'okta'
    SAGEHR = 'sagehr'
    HUMAANS = 'humaans'
    TRAFFIT = 'traffit'
    ERECRUITER = 'erecruiter'
    EURECIA = 'eurecia'
    UMANTIS = 'umantis'
    ORACLEHCM = 'oraclehcm'
    ORACLERECRUITING = 'oraclerecruiting'
    TALEEZ = 'taleez'
    OFFICIENT = 'officient'
    SESAMEHR = 'sesamehr'
    CHARLIEHR = 'charliehr'
    HRWORKS = 'hrworks'
    OTYS = 'otys'
    GUSTO = 'gusto'
    BREATHEHR = 'breathehr'
    RIPPLING = 'rippling'
    NMBRS = 'nmbrs'
    HEYRECRUIT = 'heyrecruit'
    PEOPLEHR = 'peoplehr'
    RECRUHR = 'recruhr'
    JAZZHR = 'jazzhr'
    LUCCA = 'lucca'
    BITE = 'bite'
    HOMERUN = 'homerun'
    HAILEYHR = 'haileyhr'
    SILAE = 'silae'
    MYSOLUTION = 'mysolution'
    DATEV = 'datev'
    DATEVLUG = 'datevlug'
    SYMPA = 'sympa'
    BREEZYHR = 'breezyhr'
    FLATCHR = 'flatchr'
    APPLICANTSTACK = 'applicantstack'
    IRISCASCADE = 'iriscascade'
    SANDBOX = 'sandbox'

class PostConnectCreateLinkLanguage(str, Enum):
    r"""Language of the connection flow UI."""
    EN = 'en'
    DE = 'de'
    FR = 'fr'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostConnectCreateLinkRequestBody:
    r"""POST /connect/create-link request body"""
    end_user_email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_user_email') }})
    r"""The email of the user this link is meant for."""
    end_user_organization_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_user_organization_name') }})
    r"""The name of the user's organization."""
    end_user_origin_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_user_origin_id') }})
    r"""The id the user/organization has in your own database."""
    integration_category: Optional[IntegrationCategory] = dataclasses.field(default=IntegrationCategory.HRIS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration_category'), 'exclude': lambda f: f is None }})
    r"""Category of the integration you want your customer to create."""
    integration_tool: Optional[IntegrationTool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration_tool') }})
    r"""Pre-define a tool this integration link can be used for."""
    language: Optional[PostConnectCreateLinkLanguage] = dataclasses.field(default=PostConnectCreateLinkLanguage.EN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('language'), 'exclude': lambda f: f is None }})
    r"""Language of the connection flow UI."""
    remote_environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_environment') }})
    r"""If the tool you want to connect offers different environments, you can specify which one you want to connect to here. If you don't specify this, we'll assume you want to use the production environment. Note that this can only be used if you've also specified a tool through `integration_tool`."""
    scope_config_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scope_config_id') }})
    r"""Specify a scope config that should be used for this integration. This is an advanced feature, only use it if you know what you're doing!"""
    



@dataclasses.dataclass
class PostConnectCreateLinkResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    post_connect_create_link_successful_response: Optional[shared_postconnectcreatelinksuccessfulresponse.PostConnectCreateLinkSuccessfulResponse] = dataclasses.field(default=None)
    r"""POST /connect/create-link Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

