# UnifiedATSAPI
(*unified_ats_api*)

## Overview

Unified endpoints to access all the ATS concepts you might need.

### Available Operations

* [delete_ats_candidates_candidate_id_tags](#delete_ats_candidates_candidate_id_tags) - Remove tag from candidate
* [get_ats_application_stages](#get_ats_application_stages) - Get application stages
* [get_ats_applications](#get_ats_applications) - Get applications
* [get_ats_candidates](#get_ats_candidates) - Get candidates
* [get_ats_jobs](#get_ats_jobs) - Get jobs
* [get_ats_tags](#get_ats_tags) - Get tags
* [get_ats_users](#get_ats_users) - Get users
* [patch_ats_candidates_candidate_id](#patch_ats_candidates_candidate_id) - Update candidate 🦄
* [post_ats_applications_application_id_notes](#post_ats_applications_application_id_notes) - Add note to application
* [post_ats_applications_application_id_result_links](#post_ats_applications_application_id_result_links) - Add result link to application
* [post_ats_candidates](#post_ats_candidates) - Create candidate
* [post_ats_candidates_candidate_id_attachments](#post_ats_candidates_candidate_id_attachments) - Add attachment to candidate
* [post_ats_candidates_candidate_id_result_links](#post_ats_candidates_candidate_id_result_links) - Add result link to candidate
* [post_ats_candidates_candidate_id_tags](#post_ats_candidates_candidate_id_tags) - Add tag to candidate
* [post_ats_jobs_job_id_applications](#post_ats_jobs_job_id_applications) - Create application
* [put_ats_applications_application_id_stage](#put_ats_applications_application_id_stage) - Move application to stage

## delete_ats_candidates_candidate_id_tags

Remove a tag from a candidate based on its name.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SmartRecruiters</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/onlyfy/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Onlyfy</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workable/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workable</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/welcometothejungle/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Welcome to the Jungle</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/erecruiter/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>eRecruiter</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

This will also succeed if the tag does not exist on the candidate.

<Note>
  This endpoint requires the permission **Create and manage candidates and applications** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "tag": {
    "name": "Excellent Fit"
  }
}
```

### Example Usage

```python
import speakeasybar
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_api.delete_ats_candidates_candidate_id_tags(x_integration_id='Practical', candidate_id='Account', request_body=operations.DeleteAtsCandidatesCandidateIDTagsRequestBody(
    remote_fields=operations.DeleteAtsCandidatesCandidateIDTagsRequestBodyRemoteFields(
        greenhouse=operations.DeleteAtsCandidatesCandidateIDTagsRequestBodyRemoteFieldsGreenhouse(
            post_headers=operations.DeleteAtsCandidatesCandidateIDTagsRequestBodyRemoteFieldsGreenhousePostHeaders(
                on_behalf_of='salmon Shoes',
            ),
        ),
    ),
    tag=operations.DeleteAtsCandidatesCandidateIDTagsRequestBodyTag(
        name='matrix overriding Handmade',
    ),
))

if res.delete_ats_candidates_candidate_id_tags_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                                             | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | ID of the integration you want to interact with.                                                                                               |
| `candidate_id`                                                                                                                                 | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | Kombo ID of the candidate you want to remove the tag from.                                                                                     |
| `request_body`                                                                                                                                 | [Optional[operations.DeleteAtsCandidatesCandidateIDTagsRequestBody]](../../models/operations/deleteatscandidatescandidateidtagsrequestbody.md) | :heavy_minus_sign:                                                                                                                             | DELETE /ats/candidates/:candidate_id/tags request body                                                                                         |


### Response

**[operations.DeleteAtsCandidatesCandidateIDTagsResponse](../../models/operations/deleteatscandidatescandidateidtagsresponse.md)**


## get_ats_application_stages

Get all application stages available in the ATS.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SmartRecruiters</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/onlyfy/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Onlyfy</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/afas/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>AFAS Software</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bullhorn/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Bullhorn</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workable/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workable</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/fountain/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Fountain</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/softgarden/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Softgarden</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/pinpoint/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Pinpoint</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/welcometothejungle/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Welcome to the Jungle</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/dvinci/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>d.vinci</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jobvite/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Jobvite</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sagehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sage HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/traffit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>TRAFFIT</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/erecruiter/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>eRecruiter</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/umantis/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Haufe Umantis</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/oraclerecruiting/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Oracle Recruiting Cloud</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/taleez/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Taleez</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/otys/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>OTYS</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>RECRU</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jazzhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JazzHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bite/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BITE</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/homerun/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Homerun</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breezyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breezy HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/flatchr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Flatchr</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/applicantstack/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>ApplicantStack</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

**(⚠️ Deprecated)** Get all application stages available in the ATS. This is deprecated because most ATS systems have separate sets of stages for each job. We'd recommend using the `stages` property on jobs instead.

Top level filters use AND, while individual filters use OR if they accept multiple arguments. That means filters will be resolved like this: `(id IN ids) AND (remote_id IN remote_ids)`

### Example Usage

```python
import speakeasybar
import dateutil.parser
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetAtsApplicationStagesRequest(
    x_integration_id='bamboozle',
    cursor='core East SAS',
    ids='bombard',
    include_deleted=shared.GetAtsApplicationStagesParameterIncludeDeleted.TRUE,
    page_size=777909,
    remote_ids='Account National',
    updated_after=dateutil.parser.isoparse('2022-04-09T01:25:02.164Z'),
)

res = s.unified_ats_api.get_ats_application_stages(req)

if res.get_ats_application_stages_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetAtsApplicationStagesRequest](../../models/operations/getatsapplicationstagesrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetAtsApplicationStagesResponse](../../models/operations/getatsapplicationstagesresponse.md)**


## get_ats_applications

Retrieve all applications.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SmartRecruiters</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/onlyfy/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Onlyfy</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/afas/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>AFAS Software</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bullhorn/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Bullhorn</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workable/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workable</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/fountain/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Fountain</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/softgarden/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Softgarden</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/pinpoint/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Pinpoint</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/welcometothejungle/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Welcome to the Jungle</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/dvinci/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>d.vinci</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/join/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JOIN</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jobvite/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Jobvite</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sagehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sage HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/traffit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>TRAFFIT</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/erecruiter/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>eRecruiter</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/umantis/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Haufe Umantis</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/oraclerecruiting/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Oracle Recruiting Cloud</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/taleez/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Taleez</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/otys/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>OTYS</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>RECRU</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jazzhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JazzHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bite/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BITE</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/homerun/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Homerun</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breezyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breezy HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/flatchr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Flatchr</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/applicantstack/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>ApplicantStack</li>
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
import speakeasybar
import dateutil.parser
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetAtsApplicationsRequest(
    x_integration_id='Gasoline bypass',
    cursor='flexibility',
    ids='Gasoline',
    include_deleted=shared.GetAtsApplicationsParameterIncludeDeleted.TRUE,
    outcome=shared.GetAtsApplicationsParameterOutcome.DECLINED,
    outcomes='badly',
    page_size=918792,
    remote_created_after=dateutil.parser.isoparse('2021-05-30T08:12:30.327Z'),
    remote_ids='extensible',
    updated_after=dateutil.parser.isoparse('2022-08-03T06:59:25.595Z'),
)

res = s.unified_ats_api.get_ats_applications(req)

if res.get_ats_applications_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAtsApplicationsRequest](../../models/operations/getatsapplicationsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetAtsApplicationsResponse](../../models/operations/getatsapplicationsresponse.md)**


## get_ats_candidates

Retrieve all candidates.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SmartRecruiters</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/onlyfy/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Onlyfy</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/afas/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>AFAS Software</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bamboohr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BambooHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bullhorn/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Bullhorn</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workable/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workable</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/fountain/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Fountain</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/pinpoint/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Pinpoint</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/welcometothejungle/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Welcome to the Jungle</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/join/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JOIN</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jobvite/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Jobvite</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sagehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sage HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/traffit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>TRAFFIT</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/erecruiter/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>eRecruiter</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/umantis/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Haufe Umantis</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/oraclerecruiting/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Oracle Recruiting Cloud</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/taleez/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Taleez</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/otys/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>OTYS</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>RECRU</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jazzhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JazzHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bite/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BITE</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/homerun/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Homerun</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breezyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breezy HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/flatchr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Flatchr</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/applicantstack/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>ApplicantStack</li>
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
import speakeasybar
import dateutil.parser
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetAtsCandidatesRequest(
    x_integration_id='Handmade Movies even',
    cursor='charset International',
    ids='female',
    include_deleted=shared.GetAtsCandidatesParameterIncludeDeleted.FALSE,
    page_size=332950,
    remote_ids='Berkshire Data',
    updated_after=dateutil.parser.isoparse('2023-08-20T22:30:10.141Z'),
)

res = s.unified_ats_api.get_ats_candidates(req)

if res.get_ats_candidates_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetAtsCandidatesRequest](../../models/operations/getatscandidatesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetAtsCandidatesResponse](../../models/operations/getatscandidatesresponse.md)**


## get_ats_jobs

Retrieve all jobs.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SmartRecruiters</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/onlyfy/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Onlyfy</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
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
  src="https://storage.googleapis.com/kombo-assets/integrations/bullhorn/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Bullhorn</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workable/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workable</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/fountain/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Fountain</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/softgarden/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Softgarden</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/pinpoint/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Pinpoint</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/welcometothejungle/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Welcome to the Jungle</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/dvinci/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>d.vinci</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/join/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JOIN</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jobvite/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Jobvite</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sagehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sage HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/traffit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>TRAFFIT</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/erecruiter/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>eRecruiter</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/umantis/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Haufe Umantis</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/oraclerecruiting/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Oracle Recruiting Cloud</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/taleez/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Taleez</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/otys/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>OTYS</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/heyrecruit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Heyrecruit</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>RECRU</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jazzhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JazzHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bite/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BITE</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/homerun/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Homerun</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/mysolution/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Mysolution</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breezyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breezy HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/flatchr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Flatchr</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/applicantstack/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>ApplicantStack</li>
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
import speakeasybar
import dateutil.parser
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetAtsJobsRequest(
    x_integration_id='Maine',
    cursor='Camden Platinum utterly',
    ids='Towels global East',
    include_deleted=shared.GetAtsJobsParameterIncludeDeleted.FALSE,
    job_codes='World than',
    name_contains='deliver Sheboygan',
    page_size=619175,
    post_url='Developer',
    remote_ids='Porsche Table cyan',
    status=shared.GetAtsJobsParameterStatus.CLOSED,
    statuses='carpeting Sausages female',
    updated_after=dateutil.parser.isoparse('2023-07-05T15:21:37.316Z'),
)

res = s.unified_ats_api.get_ats_jobs(req)

if res.get_ats_jobs_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetAtsJobsRequest](../../models/operations/getatsjobsrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetAtsJobsResponse](../../models/operations/getatsjobsresponse.md)**


## get_ats_tags

Retrieve all tags.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SmartRecruiters</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/onlyfy/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Onlyfy</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workable/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workable</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/pinpoint/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Pinpoint</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/welcometothejungle/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Welcome to the Jungle</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/join/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JOIN</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/traffit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>TRAFFIT</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/erecruiter/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>eRecruiter</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>RECRU</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breezyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breezy HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/flatchr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Flatchr</li>
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
import speakeasybar
import dateutil.parser
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetAtsTagsRequest(
    x_integration_id='Lakes',
    cursor='capacity synthesize',
    ids='Porsche cyan Auto',
    include_deleted=shared.GetAtsTagsParameterIncludeDeleted.TRUE,
    page_size=681587,
    remote_ids='Honolulu Boulder Cambridgeshire',
    updated_after=dateutil.parser.isoparse('2022-12-09T17:54:24.185Z'),
)

res = s.unified_ats_api.get_ats_tags(req)

if res.get_ats_tags_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetAtsTagsRequest](../../models/operations/getatstagsrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetAtsTagsResponse](../../models/operations/getatstagsresponse.md)**


## get_ats_users

Retrieve all users.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SmartRecruiters</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/onlyfy/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Onlyfy</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workable/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workable</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/softgarden/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Softgarden</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/pinpoint/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Pinpoint</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/dvinci/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>d.vinci</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/join/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JOIN</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jobvite/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Jobvite</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/traffit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>TRAFFIT</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/otys/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>OTYS</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>RECRU</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jazzhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JazzHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breezyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breezy HR</li>
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
import speakeasybar
import dateutil.parser
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetAtsUsersRequest(
    x_integration_id='imaginary Praseodymium',
    cursor='approach Fresh',
    ids='Touring',
    include_deleted=shared.GetAtsUsersParameterIncludeDeleted.FALSE,
    page_size=497581,
    remote_ids='Avon Bespoke bandwidth',
    updated_after=dateutil.parser.isoparse('2022-09-14T16:45:22.931Z'),
)

res = s.unified_ats_api.get_ats_users(req)

if res.get_ats_users_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetAtsUsersRequest](../../models/operations/getatsusersrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetAtsUsersResponse](../../models/operations/getatsusersresponse.md)**


## patch_ats_candidates_candidate_id

Currently in closed beta.
<Warning>**This endpoint is currently in closed beta!** We're testing it with selected customers before its public release. If you're interested in learning more or getting early access, please reach out.</Warning>

### Example Usage

```python
import speakeasybar
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_api.patch_ats_candidates_candidate_id(x_integration_id='Supervisor', candidate_id='East', patch_ats_candidates_candidate_id_request_body=shared.PatchAtsCandidatesCandidateIDRequestBody())

if res.patch_ats_candidates_candidate_id_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                           | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | ID of the integration you want to interact with.                                                                             |
| `candidate_id`                                                                                                               | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | PATCH /ats/candidates/:candidate_id parameter                                                                                |
| `patch_ats_candidates_candidate_id_request_body`                                                                             | [Optional[shared.PatchAtsCandidatesCandidateIDRequestBody]](../../models/shared/patchatscandidatescandidateidrequestbody.md) | :heavy_minus_sign:                                                                                                           | PATCH /ats/candidates/:candidate_id request body                                                                             |


### Response

**[operations.PatchAtsCandidatesCandidateIDResponse](../../models/operations/patchatscandidatescandidateidresponse.md)**


## post_ats_applications_application_id_notes

Add a note to an application.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/homerun/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Homerun</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

Add extra information to an application. This can be any extra text information you want to add to an application.

<Note>
  This endpoint requires the permission **Create and manage candidates and applications** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "content": "A new message from the candidate is available in YourChat!",
  "content_type": "PLAIN_TEXT"
}
```

### Example Usage

```python
import speakeasybar
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_api.post_ats_applications_application_id_notes(x_integration_id='IB', application_id='South', request_body=operations.PostAtsApplicationsApplicationIDNotesRequestBody(
    content='Facilitator teal',
    content_type=operations.PostAtsApplicationsApplicationIDNotesRequestBodyContentType.PLAIN_TEXT,
    remote_fields=operations.PostAtsApplicationsApplicationIDNotesRequestBodyRemoteFields(
        teamtailor=operations.PostAtsApplicationsApplicationIDNotesRequestBodyRemoteFieldsTeamtailor(
            user_id='Lev',
        ),
    ),
))

if res.post_ats_applications_application_id_notes_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                                                   | *str*                                                                                                                                                | :heavy_check_mark:                                                                                                                                   | ID of the integration you want to interact with.                                                                                                     |
| `application_id`                                                                                                                                     | *str*                                                                                                                                                | :heavy_check_mark:                                                                                                                                   | Kombo ID of the application you want to create the note for.                                                                                         |
| `request_body`                                                                                                                                       | [Optional[operations.PostAtsApplicationsApplicationIDNotesRequestBody]](../../models/operations/postatsapplicationsapplicationidnotesrequestbody.md) | :heavy_minus_sign:                                                                                                                                   | POST /ats/applications/:application_id/notes request body                                                                                            |


### Response

**[operations.PostAtsApplicationsApplicationIDNotesResponse](../../models/operations/postatsapplicationsapplicationidnotesresponse.md)**


## post_ats_applications_application_id_result_links

Add a result link to an application.
This can, for example, be used to link a candidate back to a test result/assessment in your application. As not all ATS tools have a "result link" feature, we sometimes repurpose other fields to expose it.

<Note>
  This endpoint requires the permission **Create and manage candidates and applications** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "application_id": "8Xi6iZrwusZqJmDGXs49GBmJ",
  "label": "Assessment Result",
  "url": "https://example.com/test-results/5BtP1WC1UboS7CF3yxjKcvjG",
  "details": {
    "custom_field_name_prefix": "Acme:",
    "attributes": [
      {
        "key": "Score",
        "value": "100%"
      },
      {
        "key": "Time",
        "value": "2:30h"
      }
    ]
  }
}
```

### Example Usage

```python
import speakeasybar
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_api.post_ats_applications_application_id_result_links(x_integration_id='Electric', application_id='Computer', request_body=operations.PostAtsApplicationsApplicationIDResultLinksRequestBody(
    details=operations.PostAtsApplicationsApplicationIDResultLinksRequestBodyDetails(
        attributes=[
            operations.PostAtsApplicationsApplicationIDResultLinksRequestBodyDetailsAttributes(
                key='<key>',
                value='Gasoline magenta',
            ),
        ],
        custom_field_name_prefix='whoa Bedfordshire',
    ),
    label='cultivate Bronze how',
    url='http://closed-terrapin.info',
))

if res.post_ats_applications_application_id_result_links_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                                                               | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | ID of the integration you want to interact with.                                                                                                                 |
| `application_id`                                                                                                                                                 | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | Kombo ID of the application you want to create the link for.                                                                                                     |
| `request_body`                                                                                                                                                   | [Optional[operations.PostAtsApplicationsApplicationIDResultLinksRequestBody]](../../models/operations/postatsapplicationsapplicationidresultlinksrequestbody.md) | :heavy_minus_sign:                                                                                                                                               | POST /ats/applications/:application_id/result-links request body                                                                                                 |


### Response

**[operations.PostAtsApplicationsApplicationIDResultLinksResponse](../../models/operations/postatsapplicationsapplicationidresultlinksresponse.md)**


## post_ats_candidates

Create a new candidate and application for the specified job.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SmartRecruiters</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/onlyfy/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Onlyfy</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
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
  src="https://storage.googleapis.com/kombo-assets/integrations/bullhorn/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Bullhorn</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workable/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workable</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/fountain/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Fountain</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/softgarden/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Softgarden</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/pinpoint/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Pinpoint</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/welcometothejungle/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Welcome to the Jungle</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/dvinci/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>d.vinci</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/join/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JOIN</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sagehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sage HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/traffit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>TRAFFIT</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/erecruiter/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>eRecruiter</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/umantis/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Haufe Umantis</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/oraclerecruiting/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Oracle Recruiting Cloud</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/taleez/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Taleez</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/otys/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>OTYS</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/heyrecruit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Heyrecruit</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>RECRU</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jazzhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JazzHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bite/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BITE</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/homerun/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Homerun</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/mysolution/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Mysolution</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breezyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breezy HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/flatchr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Flatchr</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

<Warning>
      **This endpoint is deprecated!**

      We realized that in practice it was always more about creating _applications_ instead of _candidates_, so we created a new, more aptly named one that you should use instead: [Create application](/ats/v1/post-jobs-job-id-applications)

      Using it also has the benefit that we return the newly created applicant at the root level, so you can easily store its ID.
    </Warning>

<Note>
  This endpoint requires the permission **Create and manage candidates and applications** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "candidate": {
    "first_name": "Frank",
    "last_name": "Doe",
    "company": "Acme Inc.",
    "title": "Head of Integrations",
    "email_address": "frank.doe@example.com",
    "phone_number": "+1-541-754-3010",
    "gender": "MALE",
    "salary_expectations": {
      "amount": 100000,
      "period": "YEAR"
    },
    "availability_date": "2021-01-01",
    "location": {
      "city": "New York",
      "country": "US"
    },
    "social_links": [
      {
        "url": "https://www.linkedin.com/in/frank-doe-123456789/"
      },
      {
        "url": "https://twitter.com/frankdoe"
      }
    ]
  },
  "application": {
    "job_id": "BDpgnpZ148nrGh4mYHNxJBgx",
    "stage_id": "8x3YKRDcuRnwShdh96ShBNn1"
  },
  "screening_question_answers": [
    {
      "question_id": "3phFBNXRweGnDmsU9o2vdPuQ",
      "answer": "Yes"
    },
    {
      "question_id": "EYJjhMQT3LtVKXnTbnRT8s6U",
      "answer": [
        "GUzE666zfyjeoCJX6A8n7wh6",
        "5WPHzzKAv8cx97KtHRUV96U8",
        "7yZfKGzWigXxxRTygqAfHvyE"
      ]
    }
  ],
  "attachments": [
    {
      "name": "Frank Doe CV.txt",
      "data": "SGkgdGhlcmUsIEtvbWJvIGlzIGN1cnJlbnRseSBoaXJpbmcgZW5naW5lZXJzIHRoYXQgbG92ZSB0byB3b3JrIG9uIGRldmVsb3BlciBwcm9kdWN0cy4=",
      "type": "CV",
      "content_type": "text/plain"
    }
  ]
}
```

### Example Usage

```python
import speakeasybar
import dateutil.parser
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_api.post_ats_candidates(x_integration_id='Principal', request_body=operations.PostAtsCandidatesRequestBody(
    application=operations.PostAtsCandidatesRequestBodyApplication(
        job_id='Tandem',
        stage_id='accidentally Southeast to',
    ),
    attachments=[
        operations.PostAtsCandidatesRequestBodyAttachments(
            content_type='Personal',
            data='Pop',
            data_url='https://known-company.info',
            name='Southeast RSS Home',
            type=operations.PostAtsCandidatesRequestBodyAttachmentsType.COVER_LETTER,
        ),
    ],
    candidate=operations.PostAtsCandidatesRequestBodyCandidate(
        availability_date=dateutil.parser.isoparse('2022-01-26T15:21:04.678Z'),
        company='Deckow, Yost and Leuschke',
        email_address='Rosella9@yahoo.com',
        first_name='Princess',
        gender=operations.PostAtsCandidatesRequestBodyCandidateGender.MALE,
        last_name='Casper',
        location=operations.PostAtsCandidatesRequestBodyCandidateLocation(
            city='New Bedford',
            country='Svalbard & Jan Mayen Islands',
        ),
        phone_number='Southwest lux primary',
        salary_expectations=operations.PostAtsCandidatesRequestBodyCandidateSalaryExpectations(
            amount=2701.41,
            period=operations.PostAtsCandidatesRequestBodyCandidateSalaryExpectationsPeriod.MONTH,
        ),
        social_links=[
            operations.PostAtsCandidatesRequestBodyCandidateSocialLinks(
                url='https://squeaky-tract.biz',
            ),
        ],
        title='challenge',
    ),
    gdpr_consent=operations.PostAtsCandidatesRequestBodyGdprConsent(
        expires_at=dateutil.parser.isoparse('2023-07-16T16:09:03.636Z'),
        given=False,
    ),
    remote_fields=operations.PostAtsCandidatesRequestBodyRemoteFields(
        greenhouse=operations.PostAtsCandidatesRequestBodyRemoteFieldsGreenhouse(
            post_headers=operations.PostAtsCandidatesRequestBodyRemoteFieldsGreenhousePostHeaders(
                on_behalf_of='frame Oriental',
            ),
        ),
        lever=operations.PostAtsCandidatesRequestBodyRemoteFieldsLever(
            candidate={
                "dolore": 'bluetooth',
            },
        ),
        successfactors=operations.PostAtsCandidatesRequestBodyRemoteFieldsSuccessfactors(
            candidate={
                "dolorem": 'male',
            },
            job_application={
                "debitis": 'quantifying',
            },
        ),
        teamtailor=operations.PostAtsCandidatesRequestBodyRemoteFieldsTeamtailor(
            candidate={
                "reprehenderit": 'Manager',
            },
        ),
        workable=operations.PostAtsCandidatesRequestBodyRemoteFieldsWorkable(
            candidate={
                "odit": 'female',
            },
        ),
    ),
    screening_question_answers=[
        operations.PostAtsCandidatesRequestBodyScreeningQuestionAnswers(
            answer=[],
            question_id='API Polonium Libby',
        ),
    ],
    source=operations.PostAtsCandidatesRequestBodySource(
        name='frenetically East',
    ),
))

if res.post_ats_candidates_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `x_integration_id`                                                                                           | *str*                                                                                                        | :heavy_check_mark:                                                                                           | ID of the integration you want to interact with.                                                             |
| `request_body`                                                                                               | [Optional[operations.PostAtsCandidatesRequestBody]](../../models/operations/postatscandidatesrequestbody.md) | :heavy_minus_sign:                                                                                           | POST /ats/candidates request body                                                                            |


### Response

**[operations.PostAtsCandidatesResponse](../../models/operations/postatscandidatesresponse.md)**


## post_ats_candidates_candidate_id_attachments

Uploads an attachment file for the specified candidate.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SmartRecruiters</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/onlyfy/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Onlyfy</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bullhorn/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Bullhorn</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workable/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workable</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/welcometothejungle/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Welcome to the Jungle</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/erecruiter/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>eRecruiter</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/taleez/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Taleez</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/otys/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>OTYS</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/homerun/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Homerun</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breezyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breezy HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

<Note>
  This endpoint requires the permission **Create and manage candidates and applications** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "candidate_id": "GRKdd9dibYKKCrmGRSMJf3wu",
  "attachment": {
    "name": "Frank Doe CV.txt",
    "data": "SGkgdGhlcmUsIEtvbWJvIGlzIGN1cnJlbnRseSBoaXJpbmcgZW5naW5lZXJzIHRoYXQgbG92ZSB0byB3b3JrIG9uIGRldmVsb3BlciBwcm9kdWN0cy4=",
    "type": "CV",
    "content_type": "text/plain"
  }
}
```

### Example Usage

```python
import speakeasybar
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_api.post_ats_candidates_candidate_id_attachments(x_integration_id='Assistant', candidate_id='dimly', request_body=operations.PostAtsCandidatesCandidateIDAttachmentsRequestBody(
    attachment=operations.PostAtsCandidatesCandidateIDAttachmentsRequestBodyAttachment(
        content_type='Small soon South',
        data='recontextualize',
        data_url='http://qualified-trigger.org',
        name='Integration Planner',
        type=operations.PostAtsCandidatesCandidateIDAttachmentsRequestBodyAttachmentType.COVER_LETTER,
    ),
    remote_fields=operations.PostAtsCandidatesCandidateIDAttachmentsRequestBodyRemoteFields(
        greenhouse=operations.PostAtsCandidatesCandidateIDAttachmentsRequestBodyRemoteFieldsGreenhouse(
            post_headers=operations.PostAtsCandidatesCandidateIDAttachmentsRequestBodyRemoteFieldsGreenhousePostHeaders(
                on_behalf_of='Iowa',
            ),
        ),
    ),
))

if res.post_ats_candidates_candidate_id_attachments_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                                                       | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | ID of the integration you want to interact with.                                                                                                         |
| `candidate_id`                                                                                                                                           | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | POST /ats/candidates/:candidate_id/attachments parameter                                                                                                 |
| `request_body`                                                                                                                                           | [Optional[operations.PostAtsCandidatesCandidateIDAttachmentsRequestBody]](../../models/operations/postatscandidatescandidateidattachmentsrequestbody.md) | :heavy_minus_sign:                                                                                                                                       | POST /ats/candidates/:candidate_id/attachments request body                                                                                              |


### Response

**[operations.PostAtsCandidatesCandidateIDAttachmentsResponse](../../models/operations/postatscandidatescandidateidattachmentsresponse.md)**


## post_ats_candidates_candidate_id_result_links

**(⚠️ Deprecated)** Add a result link to a candidate.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SmartRecruiters</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/onlyfy/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Onlyfy</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bullhorn/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Bullhorn</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workable/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workable</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/welcometothejungle/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Welcome to the Jungle</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/join/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JOIN</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jobvite/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Jobvite</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/erecruiter/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>eRecruiter</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/otys/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>OTYS</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jazzhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JazzHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/homerun/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Homerun</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breezyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breezy HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

Please use [add result link to application](/ats/v1/post-applications-application-id-result-links) instead.
This can, for example, be used to link a candidate back to a test result/assessment in your application. As not all ATS tools have a "result link" feature, we sometimes repurpose other fields to expose it.

This action is deprecated because result links usually concern applications and not candidates. Use endpoint nested under `/applications` instead.

<Note>
  This endpoint requires the permission **Create and manage candidates and applications** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "label": "Assessment Result",
  "url": "https://example.com/test-results/5BtP1WC1UboS7CF3yxjKcvjG",
  "details": {
    "custom_field_name_prefix": "Acme:",
    "attributes": [
      {
        "key": "Score",
        "value": "100%"
      },
      {
        "key": "Time",
        "value": "2:30h"
      }
    ]
  }
}
```

### Example Usage

```python
import speakeasybar
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_api.post_ats_candidates_candidate_id_result_links(x_integration_id='Chicken', candidate_id='Antioch', request_body=operations.PostAtsCandidatesCandidateIDResultLinksRequestBody(
    details=operations.PostAtsCandidatesCandidateIDResultLinksRequestBodyDetails(
        attributes=[
            operations.PostAtsCandidatesCandidateIDResultLinksRequestBodyDetailsAttributes(
                key='<key>',
                value='Garden',
            ),
        ],
        custom_field_name_prefix='Movies whether',
    ),
    label='East Plastic',
    remote_fields=operations.PostAtsCandidatesCandidateIDResultLinksRequestBodyRemoteFields(
        greenhouse=operations.PostAtsCandidatesCandidateIDResultLinksRequestBodyRemoteFieldsGreenhouse(
            post_headers=operations.PostAtsCandidatesCandidateIDResultLinksRequestBodyRemoteFieldsGreenhousePostHeaders(
                on_behalf_of='Refined Tennessee',
            ),
        ),
    ),
    url='http://infinite-pilaf.biz',
))

if res.post_ats_candidates_candidate_id_result_links_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                                                       | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | ID of the integration you want to interact with.                                                                                                         |
| `candidate_id`                                                                                                                                           | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | Kombo ID of the candidate you want to create the link for.                                                                                               |
| `request_body`                                                                                                                                           | [Optional[operations.PostAtsCandidatesCandidateIDResultLinksRequestBody]](../../models/operations/postatscandidatescandidateidresultlinksrequestbody.md) | :heavy_minus_sign:                                                                                                                                       | POST /ats/candidates/:candidate_id/result-links request body                                                                                             |


### Response

**[operations.PostAtsCandidatesCandidateIDResultLinksResponse](../../models/operations/postatscandidatescandidateidresultlinksresponse.md)**


## post_ats_candidates_candidate_id_tags

Add a tag to a candidate.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SmartRecruiters</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/onlyfy/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Onlyfy</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workable/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workable</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/welcometothejungle/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Welcome to the Jungle</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/erecruiter/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>eRecruiter</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>RECRU</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

Kombo takes care of creating the tag if required, finding out the right ID, and appending it to the list of tags.

<Note>
  This endpoint requires the permission **Create and manage candidates and applications** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "tag": {
    "name": "Excellent Fit"
  }
}
```

### Example Usage

```python
import speakeasybar
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_api.post_ats_candidates_candidate_id_tags(x_integration_id='Specialist', candidate_id='Gorgeous', request_body=operations.PostAtsCandidatesCandidateIDTagsRequestBody(
    remote_fields=operations.PostAtsCandidatesCandidateIDTagsRequestBodyRemoteFields(
        greenhouse=operations.PostAtsCandidatesCandidateIDTagsRequestBodyRemoteFieldsGreenhouse(
            post_headers=operations.PostAtsCandidatesCandidateIDTagsRequestBodyRemoteFieldsGreenhousePostHeaders(
                on_behalf_of='Demiflux',
            ),
        ),
    ),
    tag=operations.PostAtsCandidatesCandidateIDTagsRequestBodyTag(
        name='Interactions bypass female',
    ),
))

if res.post_ats_candidates_candidate_id_tags_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `x_integration_id`                                                                                                                         | *str*                                                                                                                                      | :heavy_check_mark:                                                                                                                         | ID of the integration you want to interact with.                                                                                           |
| `candidate_id`                                                                                                                             | *str*                                                                                                                                      | :heavy_check_mark:                                                                                                                         | Kombo ID of the candidate you want to add the tag to.                                                                                      |
| `request_body`                                                                                                                             | [Optional[operations.PostAtsCandidatesCandidateIDTagsRequestBody]](../../models/operations/postatscandidatescandidateidtagsrequestbody.md) | :heavy_minus_sign:                                                                                                                         | POST /ats/candidates/:candidate_id/tags request body                                                                                       |


### Response

**[operations.PostAtsCandidatesCandidateIDTagsResponse](../../models/operations/postatscandidatescandidateidtagsresponse.md)**


## post_ats_jobs_job_id_applications

Create a new application and candidate for the specified job. The first CV in the attachments will be treated as the resume of the candidate when the tool allows previewing a resume.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SmartRecruiters</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/onlyfy/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Onlyfy</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/personio/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Personio</li>
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
  src="https://storage.googleapis.com/kombo-assets/integrations/bullhorn/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Bullhorn</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workable/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workable</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/fountain/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Fountain</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/softgarden/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Softgarden</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/pinpoint/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Pinpoint</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/welcometothejungle/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Welcome to the Jungle</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/dvinci/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>d.vinci</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/join/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JOIN</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sagehr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sage HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/traffit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>TRAFFIT</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/erecruiter/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>eRecruiter</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/umantis/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Haufe Umantis</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/oraclerecruiting/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Oracle Recruiting Cloud</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/taleez/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Taleez</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/hrworks/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>HRworks</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/otys/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>OTYS</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/heyrecruit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Heyrecruit</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>RECRU</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/jazzhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>JazzHR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/bite/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>BITE</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/homerun/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Homerun</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/mysolution/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Mysolution</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/breezyhr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Breezy HR</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/flatchr/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Flatchr</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/sandbox/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Sandbox</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

<Note>
  This endpoint requires the permission **Create and manage candidates and applications** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "stage_id": "8x3YKRDcuRnwShdh96ShBNn1",
  "candidate": {
    "first_name": "Frank",
    "last_name": "Doe",
    "company": "Acme Inc.",
    "title": "Head of Integrations",
    "email_address": "frank.doe@example.com",
    "phone_number": "+1-541-754-3010",
    "gender": "MALE",
    "salary_expectations": {
      "amount": 100000,
      "period": "YEAR"
    },
    "availability_date": "2021-01-01",
    "location": {
      "city": "New York",
      "country": "US"
    }
  },
  "attachments": [
    {
      "name": "Frank Doe CV.txt",
      "data": "SGkgdGhlcmUsIEtvbWJvIGlzIGN1cnJlbnRseSBoaXJpbmcgZW5naW5lZXJzIHRoYXQgbG92ZSB0byB3b3JrIG9uIGRldmVsb3BlciBwcm9kdWN0cy4=",
      "type": "CV",
      "content_type": "text/plain"
    }
  ],
  "screening_question_answers": [
    {
      "question_id": "3phFBNXRweGnDmsU9o2vdPuQ",
      "answer": "Yes"
    },
    {
      "question_id": "EYJjhMQT3LtVKXnTbnRT8s6U",
      "answer": [
        "GUzE666zfyjeoCJX6A8n7wh6",
        "5WPHzzKAv8cx97KtHRUV96U8",
        "7yZfKGzWigXxxRTygqAfHvyE"
      ]
    }
  ]
}
```

### Example Usage

```python
import speakeasybar
import dateutil.parser
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_api.post_ats_jobs_job_id_applications(x_integration_id='Web', job_id='magenta', request_body=operations.PostAtsJobsJobIDApplicationsRequestBody(
    attachments=[
        operations.PostAtsJobsJobIDApplicationsRequestBodyAttachments(
            content_type='overriding Clothing',
            data='salmon',
            data_url='https://rapid-chit-chat.org',
            name='Electric plum',
            type=operations.PostAtsJobsJobIDApplicationsRequestBodyAttachmentsType.COVER_LETTER,
        ),
    ],
    candidate=operations.PostAtsJobsJobIDApplicationsRequestBodyCandidate(
        availability_date=dateutil.parser.isoparse('2021-10-14T06:06:14.425Z'),
        company='Nitzsche - Wehner',
        email_address='Irving62@hotmail.com',
        first_name='Herbert',
        gender=operations.PostAtsJobsJobIDApplicationsRequestBodyCandidateGender.OTHER,
        last_name='Carroll',
        location=operations.PostAtsJobsJobIDApplicationsRequestBodyCandidateLocation(
            city='Fort Esperanza',
            country='Mayotte',
        ),
        phone_number='bus Applications Electric',
        salary_expectations=operations.PostAtsJobsJobIDApplicationsRequestBodyCandidateSalaryExpectations(
            amount=709.38,
            period=operations.PostAtsJobsJobIDApplicationsRequestBodyCandidateSalaryExpectationsPeriod.MONTH,
        ),
        social_links=[
            operations.PostAtsJobsJobIDApplicationsRequestBodyCandidateSocialLinks(
                url='http://unrealistic-helium.net',
            ),
        ],
        title='fossick Sports South',
    ),
    gdpr_consent=operations.PostAtsJobsJobIDApplicationsRequestBodyGdprConsent(
        expires_at=dateutil.parser.isoparse('2023-02-16T12:49:17.127Z'),
        given=False,
    ),
    remote_fields=operations.PostAtsJobsJobIDApplicationsRequestBodyRemoteFields(
        greenhouse=operations.PostAtsJobsJobIDApplicationsRequestBodyRemoteFieldsGreenhouse(
            post_headers=operations.PostAtsJobsJobIDApplicationsRequestBodyRemoteFieldsGreenhousePostHeaders(
                on_behalf_of='Assurance state USB',
            ),
        ),
        lever=operations.PostAtsJobsJobIDApplicationsRequestBodyRemoteFieldsLever(
            candidate={
                "aspernatur": 'nihil',
            },
        ),
        successfactors=operations.PostAtsJobsJobIDApplicationsRequestBodyRemoteFieldsSuccessfactors(
            candidate={
                "itaque": 'Hybrid',
            },
            job_application={
                "asperiores": 'SUV',
            },
        ),
        teamtailor=operations.PostAtsJobsJobIDApplicationsRequestBodyRemoteFieldsTeamtailor(
            candidate={
                "vitae": 'Convertible',
            },
        ),
        workable=operations.PostAtsJobsJobIDApplicationsRequestBodyRemoteFieldsWorkable(
            candidate={
                "illum": 'Washington',
            },
        ),
    ),
    screening_question_answers=[
        operations.PostAtsJobsJobIDApplicationsRequestBodyScreeningQuestionAnswers(
            answer=[],
            question_id='Diesel Operations',
        ),
    ],
    source=operations.PostAtsJobsJobIDApplicationsRequestBodySource(
        name='Salad magenta gold',
    ),
    stage_id='Assistant Cotton gold',
))

if res.post_ats_jobs_job_id_applications_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                    | ID of the integration you want to interact with.                                                                                                                                                                                      |
| `job_id`                                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                    | Kombo ID or Remote ID of the Job this candidate should apply for. If you want to use the ID of the integrated system (remote_id) you need to prefix the id with "remote:". You can use the remote ID if you do not want to sync jobs. |
| `request_body`                                                                                                                                                                                                                        | [Optional[operations.PostAtsJobsJobIDApplicationsRequestBody]](../../models/operations/postatsjobsjobidapplicationsrequestbody.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                    | POST /ats/jobs/:job_id/applications request body                                                                                                                                                                                      |


### Response

**[operations.PostAtsJobsJobIDApplicationsResponse](../../models/operations/postatsjobsjobidapplicationsresponse.md)**


## put_ats_applications_application_id_stage

Moves an application to a specified stage.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workday</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SAP SuccessFactors</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>SmartRecruiters</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/lever/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Lever</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/teamtailor/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Teamtailor</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/workable/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Workable</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/traffit/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>TRAFFIT</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/oraclerecruiting/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Oracle Recruiting Cloud</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/homerun/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Homerun</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

<Note>
  This endpoint requires the permission **Create and manage candidates and applications** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "stage_id": "3PJ8PZhZZa1eEdd2DtPNtVup"
}
```

### Example Usage

```python
import speakeasybar
from speakeasybar.models import operations, shared

s = speakeasybar.Speakeasybar(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_api.put_ats_applications_application_id_stage(x_integration_id='Francium', application_id='Cotton', request_body=operations.PutAtsApplicationsApplicationIDStageRequestBody(
    remote_fields=operations.PutAtsApplicationsApplicationIDStageRequestBodyRemoteFields(
        greenhouse=operations.PutAtsApplicationsApplicationIDStageRequestBodyRemoteFieldsGreenhouse(
            post_headers=operations.PutAtsApplicationsApplicationIDStageRequestBodyRemoteFieldsGreenhousePostHeaders(
                on_behalf_of='Arsenic',
            ),
        ),
    ),
    stage_id='Diesel',
))

if res.put_ats_applications_application_id_stage_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                                                 | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | ID of the integration you want to interact with.                                                                                                   |
| `application_id`                                                                                                                                   | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | PUT /ats/applications/:application_id/stage parameter                                                                                              |
| `request_body`                                                                                                                                     | [Optional[operations.PutAtsApplicationsApplicationIDStageRequestBody]](../../models/operations/putatsapplicationsapplicationidstagerequestbody.md) | :heavy_minus_sign:                                                                                                                                 | PUT /ats/applications/:application_id/stage request body                                                                                           |


### Response

**[operations.PutAtsApplicationsApplicationIDStageResponse](../../models/operations/putatsapplicationsapplicationidstageresponse.md)**

