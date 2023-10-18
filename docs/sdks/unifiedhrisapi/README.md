# UnifiedHRISAPI
(*unified_hris_api*)

## Overview

Unified endpoints to access all the HR concepts you might need.

### Available Operations

* [delete_hris_absences_absence_id](#delete_hris_absences_absence_id) - Delete absence
* [get_hris_absence_types](#get_hris_absence_types) - Get absence types
* [get_hris_absences](#get_hris_absences) - Get absences
* [get_hris_employees](#get_hris_employees) - Get employees
* [get_hris_employments](#get_hris_employments) - Get employments
* [get_hris_groups](#get_hris_groups) - Get groups
* [get_hris_legal_entities](#get_hris_legal_entities) - Get legal entities
* [get_hris_locations](#get_hris_locations) - Get locations
* [get_hris_teams](#get_hris_teams) - Get teams (deprecated)
* [get_hris_time_off_balances](#get_hris_time_off_balances) - Get time off balances
* [patch_hris_employees_employee_id](#patch_hris_employees_employee_id) - Update employee
* [post_hris_absences](#post_hris_absences) - Create absence
* [post_hris_employees](#post_hris_employees) - Create employee
* [post_hris_employees_employee_id_attachments](#post_hris_employees_employee_id_attachments) - Add attachment to employees 🦄

## delete_hris_absences_absence_id

Delete this absence.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/factorial/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Factorial</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hibob/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HiBob</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/deel/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Deel</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sesamehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sesame HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

<Note>
  This endpoint requires the permission **Manage absences** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "absence_id": "wXJMxwDvPAjrJ4CyqdV9"
}
```

### Example Usage

```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_hris_api.delete_hris_absences_absence_id(x_integration_id='Movies', absence_id='Electric', delete_hris_absences_absence_id_request_body=shared.DeleteHrisAbsencesAbsenceIDRequestBody())

if res.delete_hris_absences_absence_id_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `x_integration_id`                                                                                                       | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | ID of the integration you want to interact with.                                                                         |
| `absence_id`                                                                                                             | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | The ID of the absence                                                                                                    |
| `delete_hris_absences_absence_id_request_body`                                                                           | [Optional[shared.DeleteHrisAbsencesAbsenceIDRequestBody]](../../models/shared/deletehrisabsencesabsenceidrequestbody.md) | :heavy_minus_sign:                                                                                                       | DELETE /hris/absences/:absence_id request body                                                                           |


### Response

**[operations.DeleteHrisAbsencesAbsenceIDResponse](../../models/operations/deletehrisabsencesabsenceidresponse.md)**


## get_hris_absence_types

Retrieve all absence types.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/factorial/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Factorial</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/rexx/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>rexx systems</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/payfit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>PayFit</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/kenjo/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Kenjo</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hibob/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HiBob</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/deel/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Deel</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sagehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sage HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/humaans/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Humaans</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/eurecia/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Eurécia</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/officient/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Officient</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sesamehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sesame HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/charliehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Charlie</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/rippling/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Rippling</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/datev/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>DATEV LODAS</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/datevlug/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>DATEV Lohn & Gehalt</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

Top level filters use AND, while individual filters use OR if they accept multiple arguments. That means filters will be resolved like this: `(id IN ids) AND (remote_id IN remote_ids)`

### Example Usage

```python
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetHrisAbsenceTypesRequest(
    x_integration_id='Oval',
)

res = s.unified_hris_api.get_hris_absence_types(req)

if res.get_hris_absence_types_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetHrisAbsenceTypesRequest](../../models/operations/gethrisabsencetypesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetHrisAbsenceTypesResponse](../../models/operations/gethrisabsencetypesresponse.md)**


## get_hris_absences

Retrieve all absences.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/factorial/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Factorial</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/rexx/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>rexx systems</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/payfit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>PayFit</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/kenjo/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Kenjo</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hibob/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HiBob</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/deel/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Deel</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sagehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sage HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/humaans/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Humaans</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/eurecia/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Eurécia</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/officient/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Officient</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sesamehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sesame HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/charliehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Charlie</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/rippling/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Rippling</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/haileyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Hailey HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

Top level filters use AND, while individual filters use OR if they accept multiple arguments. That means filters will be resolved like this: `(id IN ids) AND (remote_id IN remote_ids)`

### Example Usage

```python
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetHrisAbsencesRequest(
    x_integration_id='infect',
)

res = s.unified_hris_api.get_hris_absences(req)

if res.get_hris_absences_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetHrisAbsencesRequest](../../models/operations/gethrisabsencesrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetHrisAbsencesResponse](../../models/operations/gethrisabsencesresponse.md)**


## get_hris_employees

Retrieve all employees.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/factorial/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Factorial</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/rexx/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>rexx systems</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/afas/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>AFAS Software</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/payfit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>PayFit</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/kenjo/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Kenjo</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/heavenhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HeavenHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hibob/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HiBob</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/azuread/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Azure AD</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/googleworkspace/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Google Workspace</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/deel/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Deel</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/remotecom/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Remote</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/okta/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Okta</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sagehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sage HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/humaans/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Humaans</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/eurecia/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Eurécia</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/oraclehcm/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Oracle HCM</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/officient/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Officient</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sesamehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sesame HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/charliehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Charlie</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/gusto/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Gusto</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breathehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breathe HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/rippling/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Rippling</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/nmbrs/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Nmbrs</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/peoplehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>PeopleHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lucca/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lucca</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/haileyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Hailey HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/silae/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Silae</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/iriscascade/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>IRIS Cascade</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

<Note>Not interested in most fields? You can use our [our Scopes feature](/scopes) to customize what data points are synced.</Note>

Top level filters use AND, while individual filters use OR if they accept multiple arguments. That means filters will be resolved like this: `(id IN ids) AND (remote_id IN remote_ids)`

### Example Usage

```python
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetHrisEmployeesRequest(
    x_integration_id='inside',
)

res = s.unified_hris_api.get_hris_employees(req)

if res.get_hris_employees_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetHrisEmployeesRequest](../../models/operations/gethrisemployeesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetHrisEmployeesResponse](../../models/operations/gethrisemployeesresponse.md)**


## get_hris_employments

Retrieve all employments.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/factorial/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Factorial</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/rexx/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>rexx systems</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/payfit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>PayFit</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/kenjo/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Kenjo</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/heavenhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HeavenHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hibob/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HiBob</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/deel/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Deel</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/remotecom/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Remote</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sagehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sage HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/humaans/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Humaans</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/eurecia/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Eurécia</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/oraclehcm/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Oracle HCM</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/officient/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Officient</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/charliehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Charlie</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breathehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breathe HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/nmbrs/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Nmbrs</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/peoplehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>PeopleHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lucca/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lucca</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/haileyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Hailey HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/silae/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Silae</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/iriscascade/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>IRIS Cascade</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

Top level filters use AND, while individual filters use OR if they accept multiple arguments. That means filters will be resolved like this: `(id IN ids) AND (remote_id IN remote_ids)`

### Example Usage

```python
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetHrisEmploymentsRequest(
    x_integration_id='Elegant',
)

res = s.unified_hris_api.get_hris_employments(req)

if res.get_hris_employments_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetHrisEmploymentsRequest](../../models/operations/gethrisemploymentsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetHrisEmploymentsResponse](../../models/operations/gethrisemploymentsresponse.md)**


## get_hris_groups

Retrieve all "groups" (teams, departments, and cost centers).

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/factorial/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Factorial</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/rexx/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>rexx systems</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/afas/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>AFAS Software</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/payfit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>PayFit</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/kenjo/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Kenjo</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/heavenhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HeavenHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hibob/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HiBob</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/azuread/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Azure AD</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/googleworkspace/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Google Workspace</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/deel/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Deel</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/okta/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Okta</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/humaans/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Humaans</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/eurecia/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Eurécia</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/oraclehcm/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Oracle HCM</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/officient/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Officient</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sesamehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sesame HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/charliehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Charlie</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/gusto/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Gusto</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breathehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breathe HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/rippling/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Rippling</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/nmbrs/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Nmbrs</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/peoplehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>PeopleHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lucca/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lucca</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/haileyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Hailey HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/silae/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Silae</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/iriscascade/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>IRIS Cascade</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

Top level filters use AND, while individual filters use OR if they accept multiple arguments. That means filters will be resolved like this: `(id IN ids) AND (remote_id IN remote_ids)`

### Example Usage

```python
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetHrisGroupsRequest(
    x_integration_id='Zloty',
)

res = s.unified_hris_api.get_hris_groups(req)

if res.get_hris_groups_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetHrisGroupsRequest](../../models/operations/gethrisgroupsrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetHrisGroupsResponse](../../models/operations/gethrisgroupsresponse.md)**


## get_hris_legal_entities

Retrieve all legal entites.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/factorial/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Factorial</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/payfit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>PayFit</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/deel/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Deel</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/gusto/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Gusto</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/nmbrs/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Nmbrs</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lucca/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lucca</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

Top level filters use AND, while individual filters use OR if they accept multiple arguments. That means filters will be resolved like this: `(id IN ids) AND (remote_id IN remote_ids)`

### Example Usage

```python
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetHrisLegalEntitiesRequest(
    x_integration_id='into',
)

res = s.unified_hris_api.get_hris_legal_entities(req)

if res.get_hris_legal_entities_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetHrisLegalEntitiesRequest](../../models/operations/gethrislegalentitiesrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetHrisLegalEntitiesResponse](../../models/operations/gethrislegalentitiesresponse.md)**


## get_hris_locations

Retrieve all locations.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/factorial/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Factorial</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/payfit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>PayFit</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/kenjo/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Kenjo</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/heavenhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HeavenHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hibob/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HiBob</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/deel/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Deel</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/remotecom/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Remote</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/humaans/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Humaans</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/oraclehcm/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Oracle HCM</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sesamehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sesame HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/charliehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Charlie</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/gusto/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Gusto</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breathehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breathe HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/rippling/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Rippling</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/nmbrs/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Nmbrs</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/peoplehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>PeopleHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/haileyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Hailey HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

Top level filters use AND, while individual filters use OR if they accept multiple arguments. That means filters will be resolved like this: `(id IN ids) AND (remote_id IN remote_ids)`

### Example Usage

```python
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetHrisLocationsRequest(
    x_integration_id='input',
)

res = s.unified_hris_api.get_hris_locations(req)

if res.get_hris_locations_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetHrisLocationsRequest](../../models/operations/gethrislocationsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetHrisLocationsResponse](../../models/operations/gethrislocationsresponse.md)**


## get_hris_teams

Get the teams.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/factorial/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Factorial</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/rexx/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>rexx systems</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/afas/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>AFAS Software</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/payfit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>PayFit</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/kenjo/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Kenjo</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/heavenhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HeavenHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hibob/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HiBob</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/azuread/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Azure AD</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/googleworkspace/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Google Workspace</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/deel/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Deel</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/okta/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Okta</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/humaans/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Humaans</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/eurecia/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Eurécia</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/oraclehcm/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Oracle HCM</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/officient/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Officient</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sesamehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sesame HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/charliehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Charlie</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/gusto/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Gusto</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breathehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breathe HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/rippling/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Rippling</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/nmbrs/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Nmbrs</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/peoplehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>PeopleHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lucca/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lucca</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/haileyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Hailey HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/silae/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Silae</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/iriscascade/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>IRIS Cascade</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

**(⚠️ Deprecated)** Please use [the `/groups` endpoint](/hris/v1/get-groups) instead. It returns the same data but the naming makes more sense as the model not only includes teams but also departments and cost centers.

Top level filters use AND, while individual filters use OR if they accept multiple arguments. That means filters will be resolved like this: `(id IN ids) AND (remote_id IN remote_ids)`

### Example Usage

```python
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetHrisTeamsRequest(
    x_integration_id='Consultant',
)

res = s.unified_hris_api.get_hris_teams(req)

if res.get_hris_teams_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetHrisTeamsRequest](../../models/operations/gethristeamsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetHrisTeamsResponse](../../models/operations/gethristeamsresponse.md)**


## get_hris_time_off_balances

Retrieve all time off balances.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hibob/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HiBob</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/deel/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Deel</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sagehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sage HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/humaans/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Humaans</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/eurecia/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Eurécia</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/charliehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Charlie</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

Top level filters use AND, while individual filters use OR if they accept multiple arguments. That means filters will be resolved like this: `(id IN ids) AND (remote_id IN remote_ids)`

### Example Usage

```python
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetHrisTimeOffBalancesRequest(
    x_integration_id='Southwest',
)

res = s.unified_hris_api.get_hris_time_off_balances(req)

if res.get_hris_time_off_balances_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetHrisTimeOffBalancesRequest](../../models/operations/gethristimeoffbalancesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetHrisTimeOffBalancesResponse](../../models/operations/gethristimeoffbalancesresponse.md)**


## patch_hris_employees_employee_id

Update an employee.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/datev/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>DATEV LODAS</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/datevlug/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>DATEV Lohn & Gehalt</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

<Note>
  This endpoint requires the permission **Create and manage employees** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "employee_id": "BkgfzSr5muN9cUTMD4wDQFn4",
  "first_name": "John",
  "last_name": "Doe",
  "work_email": "john.doe@acme.com",
  "ssn": "555-32-6395",
  "tax_id": "12 345 678 901",
  "gender": "MALE",
  "marital_status": "MARRIED",
  "date_of_birth": "1986-01-01",
  "start_date": "2020-04-07",
  "termination_date": "2022-05-20",
  "job_title": "Integrations Team Lead",
  "nationality": "DE",
  "home_address": {
    "city": "Berlin",
    "country": "DE",
    "state": "Berlin",
    "street_1": "Sonnenallee 63",
    "zip_code": "12045"
  }
}
```

### Example Usage

```python
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_hris_api.patch_hris_employees_employee_id(x_integration_id='provided', employee_id='Chips', patch_hris_employees_employee_id_request_body=shared.PatchHrisEmployeesEmployeeIDRequestBody(
    first_name='Elisha',
    home_address=shared.PatchHrisEmployeesEmployeeIDRequestBodyHomeAddress(),
    last_name='Dach',
    remote_fields=shared.PatchHrisEmployeesEmployeeIDRequestBodyRemoteFields(
        humaans=shared.PatchHrisEmployeesEmployeeIDRequestBodyRemoteFieldsHumaans(
            employee={
                "whether": 'Loan',
            },
        ),
    ),
    work_email='Kolby6@gmail.com',
))

if res.patch_hris_employees_employee_id_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                                                             | *str*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                             | ID of the integration you want to interact with.                                                                                                               |
| `employee_id`                                                                                                                                                  | *str*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                             | ID of the employee that should be updated. You can use their Kombo `id` or their ID in the remote system by prefixing it with `remote:` (e.g., `remote:12312`) |
| `patch_hris_employees_employee_id_request_body`                                                                                                                | [Optional[shared.PatchHrisEmployeesEmployeeIDRequestBody]](../../models/shared/patchhrisemployeesemployeeidrequestbody.md)                                     | :heavy_minus_sign:                                                                                                                                             | PATCH /hris/employees/:employee_id request body                                                                                                                |


### Response

**[operations.PatchHrisEmployeesEmployeeIDResponse](../../models/operations/patchhrisemployeesemployeeidresponse.md)**


## post_hris_absences

Create a new absence.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/factorial/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Factorial</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hibob/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HiBob</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/deel/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Deel</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sesamehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sesame HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/datev/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>DATEV LODAS</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/datevlug/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>DATEV Lohn & Gehalt</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

Check [this page](/hris/features/creating-absences) for a detailed guide.

<Note>
  This endpoint requires the permission **Manage absences** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "employee_id": "wXJMxwDvPAjrJ4CyqdV9",
  "absence_type_id": "3YKtQ7qedsrcCady1jSyAkY1",
  "start_date": "2019-09-17",
  "end_date": "2019-09-21",
  "start_half_day": false,
  "end_half_day": false,
  "employee_note": "Visiting the aliens",
  "start_time": "08:30:00",
  "end_time": "16:00:00"
}
```

### Example Usage

```python
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_hris_api.post_hris_absences(x_integration_id='Plastic', request_body=operations.PostHrisAbsencesRequestBody(
    absence_type_id='East',
    employee_id='application',
    employee_note='transition',
))

if res.post_hris_absences_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                         | *str*                                                                                                      | :heavy_check_mark:                                                                                         | ID of the integration you want to interact with.                                                           |
| `request_body`                                                                                             | [Optional[operations.PostHrisAbsencesRequestBody]](../../models/operations/posthrisabsencesrequestbody.md) | :heavy_minus_sign:                                                                                         | POST /hris/absences request body                                                                           |


### Response

**[operations.PostHrisAbsencesResponse](../../models/operations/posthrisabsencesresponse.md)**


## post_hris_employees

Create a new employee.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/factorial/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Factorial</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hibob/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HiBob</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/remotecom/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Remote</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sagehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sage HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/humaans/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Humaans</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breathehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breathe HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/nmbrs/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Nmbrs</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

<Note>
  This endpoint requires the permission **Create and manage employees** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "work_email": "john.doe@acme.com",
  "gender": "MALE",
  "job_title": "Integrations Team Lead",
  "home_address": {
    "city": "Berlin",
    "country": "DE",
    "state": "Berlin",
    "street_1": "Sonnenallee 63",
    "zip_code": "12045"
  },
  "date_of_birth": "1986-01-01",
  "start_date": "2020-04-07"
}
```

### Example Usage

```python
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_hris_api.post_hris_employees(x_integration_id='parse', request_body=operations.PostHrisEmployeesRequestBody(
    first_name='Brandy',
    home_address=operations.PostHrisEmployeesRequestBodyHomeAddress(),
    last_name='Kulas',
    remote_fields=operations.PostHrisEmployeesRequestBodyRemoteFields(
        humaans=operations.PostHrisEmployeesRequestBodyRemoteFieldsHumaans(
            employee={
                "Pants": 'Platinum',
            },
        ),
    ),
    work_email='Albert_Kunde@hotmail.com',
))

if res.post_hris_employees_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `x_integration_id`                                                                                           | *str*                                                                                                        | :heavy_check_mark:                                                                                           | ID of the integration you want to interact with.                                                             |
| `request_body`                                                                                               | [Optional[operations.PostHrisEmployeesRequestBody]](../../models/operations/posthrisemployeesrequestbody.md) | :heavy_minus_sign:                                                                                           | POST /hris/employees request body                                                                            |


### Response

**[operations.PostHrisEmployeesResponse](../../models/operations/posthrisemployeesresponse.md)**


## post_hris_employees_employee_id_attachments

Currently in closed beta.
<Warning>**This endpoint is currently in closed beta!** We're testing it with selected customers before its public release. If you're interested in learning more or getting early access, please reach out.</Warning>

### Example Usage

```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_hris_api.post_hris_employees_employee_id_attachments(x_integration_id='Mouse', employee_id='wireless', post_hris_employees_employee_id_attachments_request_body=shared.PostHrisEmployeesEmployeeIDAttachmentsRequestBody())

if res.post_hris_employees_employee_id_attachments_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                                             | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | ID of the integration you want to interact with.                                                                                               |
| `employee_id`                                                                                                                                  | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | POST /hris/employees/:employee_id/attachments parameter                                                                                        |
| `post_hris_employees_employee_id_attachments_request_body`                                                                                     | [Optional[shared.PostHrisEmployeesEmployeeIDAttachmentsRequestBody]](../../models/shared/posthrisemployeesemployeeidattachmentsrequestbody.md) | :heavy_minus_sign:                                                                                                                             | POST /hris/employees/:employee_id/attachments request body                                                                                     |


### Response

**[operations.PostHrisEmployeesEmployeeIDAttachmentsResponse](../../models/operations/posthrisemployeesemployeeidattachmentsresponse.md)**

