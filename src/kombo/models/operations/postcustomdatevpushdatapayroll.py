"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from ..shared import postcustomdatevpushdatapayrollerrorresponse as shared_postcustomdatevpushdatapayrollerrorresponse
from ..shared import postcustomdatevpushdatapayrollsuccessfulresponse as shared_postcustomdatevpushdatapayrollsuccessfulresponse
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from kombo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostCustomDatevPushDataPayrollRequestBody:
    r"""POST /custom/datev/push-data/payroll request body"""
    payroll_month: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payroll_month'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Specify the month for which the payroll data should be submitted. The date must be specified as the first day of a month (e.g. 2022-12-01).
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
    """
    




@dataclasses.dataclass
class PostCustomDatevPushDataPayrollRequest:
    x_integration_id: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Integration-Id', 'style': 'simple', 'explode': False }})
    r"""ID of the integration you want to interact with."""
    request_body: Optional[PostCustomDatevPushDataPayrollRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""POST /custom/datev/push-data/payroll request body"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostCustomDatevPushDataPayroll503ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostCustomDatevPushDataPayroll503ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostCustomDatevPushDataPayroll503ApplicationJSON:
    r"""Returned when no sync has finished successfully yet"""
    error: PostCustomDatevPushDataPayroll503ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostCustomDatevPushDataPayroll503ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostCustomDatevPushDataPayroll404ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostCustomDatevPushDataPayroll404ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostCustomDatevPushDataPayroll404ApplicationJSON:
    r"""Returned when a requested resource is not found."""
    error: PostCustomDatevPushDataPayroll404ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostCustomDatevPushDataPayroll404ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostCustomDatevPushDataPayroll403ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostCustomDatevPushDataPayroll403ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostCustomDatevPushDataPayroll403ApplicationJSON:
    r"""Returned when the passed integration is inactive."""
    error: PostCustomDatevPushDataPayroll403ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostCustomDatevPushDataPayroll403ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostCustomDatevPushDataPayroll401ApplicationJSONError:
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    


class PostCustomDatevPushDataPayroll401ApplicationJSONStatus(str, Enum):
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostCustomDatevPushDataPayroll401ApplicationJSON:
    r"""Returned when the authentication header was invalid or missing."""
    error: PostCustomDatevPushDataPayroll401ApplicationJSONError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    status: PostCustomDatevPushDataPayroll401ApplicationJSONStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    




@dataclasses.dataclass
class PostCustomDatevPushDataPayrollResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    post_custom_datev_push_data_payroll_401_application_json_object: Optional[PostCustomDatevPushDataPayroll401ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the authentication header was invalid or missing."""
    post_custom_datev_push_data_payroll_403_application_json_object: Optional[PostCustomDatevPushDataPayroll403ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when the passed integration is inactive."""
    post_custom_datev_push_data_payroll_404_application_json_object: Optional[PostCustomDatevPushDataPayroll404ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when a requested resource is not found."""
    post_custom_datev_push_data_payroll_503_application_json_object: Optional[PostCustomDatevPushDataPayroll503ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned when no sync has finished successfully yet"""
    post_custom_datev_push_data_payroll_error_response: Optional[shared_postcustomdatevpushdatapayrollerrorresponse.PostCustomDatevPushDataPayrollErrorResponse] = dataclasses.field(default=None)
    r"""POST /custom/datev/push-data/payroll Error response"""
    post_custom_datev_push_data_payroll_successful_response: Optional[shared_postcustomdatevpushdatapayrollsuccessfulresponse.PostCustomDatevPushDataPayrollSuccessfulResponse] = dataclasses.field(default=None)
    r"""POST /custom/datev/push-data/payroll Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

