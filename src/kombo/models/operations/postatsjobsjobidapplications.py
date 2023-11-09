"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from ...models.shared import postatsjobsjobidapplicationssuccessfulresponse as shared_postatsjobsjobidapplicationssuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from kombo import utils
from typing import Any, Dict, List, Optional, Union

class PostAtsJobsJobIDApplicationsType(str, Enum):
    CV = 'CV'
    COVER_LETTER = 'COVER_LETTER'
    OTHER = 'OTHER'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsAttachments:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the file you want to upload."""
    type: PostAtsJobsJobIDApplicationsType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    content_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content_type'), 'exclude': lambda f: f is None }})
    r"""Content/MIME type of the file (e.g., `application/pdf`). This is required if you provide `data` and optional if you provide `data_url`."""
    data: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    r"""Base64-encoded contents of the file you want to upload. You must provide either this or `data_url`."""
    data_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_url'), 'exclude': lambda f: f is None }})
    r"""Publicly accessible URL to the file you want to upload. You must provide either this or `data`."""
    


class PostAtsJobsJobIDApplicationsGender(str, Enum):
    r"""The gender of the applicant. Must be one of `MALE`, `FEMALE`, or `OTHER`."""
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsLocation:
    country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    r"""The uppercase two-letter ISO country (e.g., `DE`) of the applicant."""
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city'), 'exclude': lambda f: f is None }})
    


class PostAtsJobsJobIDApplicationsPeriod(str, Enum):
    r"""The period of the salary expectations. Must be one of `MONTH` or `YEAR`."""
    MONTH = 'MONTH'
    YEAR = 'YEAR'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsSalaryExpectations:
    r"""The salary expectations of the applicant. We will automatically convert the amount to a format that is suitable for the ATS you are using. For example, if you are using monthly salary expectations, we will convert the amount to a yearly salary if the ATS expects yearly salary expectations."""
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The amount of the salary expectations."""
    period: PostAtsJobsJobIDApplicationsPeriod = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('period') }})
    r"""The period of the salary expectations. Must be one of `MONTH` or `YEAR`."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsSocialLinks:
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsCandidate:
    email_address: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_address') }})
    r"""The primary email address this application will be created with."""
    first_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('first_name') }})
    last_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_name') }})
    availability_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('availability_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The date the applicant is available to start working.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company'), 'exclude': lambda f: f is None }})
    r"""The company where the applicant is currently working."""
    gender: Optional[PostAtsJobsJobIDApplicationsGender] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gender'), 'exclude': lambda f: f is None }})
    r"""The gender of the applicant. Must be one of `MALE`, `FEMALE`, or `OTHER`."""
    location: Optional[PostAtsJobsJobIDApplicationsLocation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location'), 'exclude': lambda f: f is None }})
    phone_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone_number'), 'exclude': lambda f: f is None }})
    salary_expectations: Optional[PostAtsJobsJobIDApplicationsSalaryExpectations] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('salary_expectations'), 'exclude': lambda f: f is None }})
    r"""The salary expectations of the applicant. We will automatically convert the amount to a format that is suitable for the ATS you are using. For example, if you are using monthly salary expectations, we will convert the amount to a yearly salary if the ATS expects yearly salary expectations."""
    social_links: Optional[List[PostAtsJobsJobIDApplicationsSocialLinks]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('social_links'), 'exclude': lambda f: f is None }})
    r"""A list of social media links of the applicant. The links must be valid URLs."""
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""The current job title of the applicant."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsGdprConsent:
    r"""Optional GDPR consent information required in some jurisdictions (like the Czech Republic or Slovakia)."""
    expires_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""Until when the candidate has granted the company they're applying to permission to process their personal data.
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    given: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('given'), 'exclude': lambda f: f is None }})
    r"""Whether the candidate has given consent."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsPostHeaders:
    r"""Headers we will pass with `POST` requests to Greenhouse."""
    on_behalf_of: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('On-Behalf-Of') }})
    r"""ID of the the user that will show up as having performed the action in Greenhouse. We already pass a value by default, but you can use this to override it."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsGreenhouse:
    r"""Fields specific to Greenhouse."""
    post_headers: Optional[PostAtsJobsJobIDApplicationsPostHeaders] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('post_headers'), 'exclude': lambda f: f is None }})
    r"""Headers we will pass with `POST` requests to Greenhouse."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsLever:
    r"""Fields specific to Lever."""
    candidate: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('candidate'), 'exclude': lambda f: f is None }})
    r"""Fields that we will pass through to Lever's `Candidate` object. Note: make sure to submit the keys and values in the correct form data format."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsSuccessfactors:
    r"""Fields specific to SAP SuccessFactors."""
    candidate: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Candidate'), 'exclude': lambda f: f is None }})
    r"""Fields that we will pass through to SuccessFactor's `Candidate` object."""
    job_application: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('JobApplication'), 'exclude': lambda f: f is None }})
    r"""Fields that we will pass through to SuccessFactor's `JobApplication` object."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsTeamtailor:
    candidate: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('candidate'), 'exclude': lambda f: f is None }})
    r"""Fields that we will pass through to Teamtailor's `Candidate` object."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsWorkable:
    r"""Fields specific to Workable."""
    candidate: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('candidate'), 'exclude': lambda f: f is None }})
    r"""Fields that we will pass through to Workable's `Candidate` object."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsRemoteFields:
    r"""Additional fields that we will pass through to specific ATS systems."""
    greenhouse: Optional[PostAtsJobsJobIDApplicationsGreenhouse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('greenhouse'), 'exclude': lambda f: f is None }})
    r"""Fields specific to Greenhouse."""
    lever: Optional[PostAtsJobsJobIDApplicationsLever] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lever'), 'exclude': lambda f: f is None }})
    r"""Fields specific to Lever."""
    successfactors: Optional[PostAtsJobsJobIDApplicationsSuccessfactors] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('successfactors'), 'exclude': lambda f: f is None }})
    r"""Fields specific to SAP SuccessFactors."""
    teamtailor: Optional[PostAtsJobsJobIDApplicationsTeamtailor] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('teamtailor'), 'exclude': lambda f: f is None }})
    workable: Optional[PostAtsJobsJobIDApplicationsWorkable] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workable'), 'exclude': lambda f: f is None }})
    r"""Fields specific to Workable."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsScreeningQuestionAnswers:
    answer: Union[str, bool, float, List[str], datetime] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer'), 'encoder': utils.union_encoder({datetime: utils.datetimeisoformat(False)}), 'decoder': utils.union_decoder([dateutil.parser.isoparse]) }})
    r"""Answer to a question. This will be validated based on the question format and throw an error if the answer is invalid."""
    question_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('question_id') }})
    r"""ID of the question returned by the Kombo API. We'll report a warning in the logs if the question can't be found on the job."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsSource:
    r"""Optional source information that will be attached to the candidate. If you're a job board or recruiting service, you can use this to make sure your customers can see which candidates came from you."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the source (e.g., `\\"Example Job Board\\"`).

    Note that this **only** works for ATS systems that support creating a source through the API right now. This includes Breezy HR, Fountain, Pinpoint, RECRU, Recruitee, Sage HR, and Haufe Umantis. For all other ATSs, the source will be ignored at the moment.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsRequestBody:
    r"""POST /ats/jobs/:job_id/applications request body"""
    candidate: PostAtsJobsJobIDApplicationsCandidate = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('candidate') }})
    attachments: Optional[List[PostAtsJobsJobIDApplicationsAttachments]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachments'), 'exclude': lambda f: f is None }})
    r"""Array of the attachments you would like upload."""
    gdpr_consent: Optional[PostAtsJobsJobIDApplicationsGdprConsent] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gdpr_consent'), 'exclude': lambda f: f is None }})
    r"""Optional GDPR consent information required in some jurisdictions (like the Czech Republic or Slovakia)."""
    remote_fields: Optional[PostAtsJobsJobIDApplicationsRemoteFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remote_fields'), 'exclude': lambda f: f is None }})
    r"""Additional fields that we will pass through to specific ATS systems."""
    screening_question_answers: Optional[List[PostAtsJobsJobIDApplicationsScreeningQuestionAnswers]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('screening_question_answers'), 'exclude': lambda f: f is None }})
    r"""Array of answers to screening questions. Currently, not all question types are supported and unsupported ones will not be submitted.

    The available questions a job can be retrieved from the get jobs endpoint. The answers will be validated based on the format of the the questions. Make sure to follow this schema to avoid errors.
    """
    source: Optional[PostAtsJobsJobIDApplicationsSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    r"""Optional source information that will be attached to the candidate. If you're a job board or recruiting service, you can use this to make sure your customers can see which candidates came from you."""
    stage_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stage_id'), 'exclude': lambda f: f is None }})
    r"""Stage this candidate should be in. If left out, the default stage for this job will be used."""
    



@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsRequest:
    job_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'job_id', 'style': 'simple', 'explode': False }})
    r"""Kombo ID or Remote ID of the Job this candidate should apply for. If you want to use the ID of the integrated system (remote_id) you need to prefix the id with \\"remote:\\". You can use the remote ID if you do not want to sync jobs."""
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    request_body: Optional[PostAtsJobsJobIDApplicationsRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""POST /ats/jobs/:job_id/applications request body"""
    



@dataclasses.dataclass
class PostAtsJobsJobIDApplicationsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    post_ats_jobs_job_id_applications_successful_response: Optional[shared_postatsjobsjobidapplicationssuccessfulresponse.PostAtsJobsJobIDApplicationsSuccessfulResponse] = dataclasses.field(default=None)
    r"""POST /ats/jobs/:job_id/applications Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

