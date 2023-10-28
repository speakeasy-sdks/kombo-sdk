# Kombo SDK

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>   
</div>

## How to use this repository

**👀** This template repository is designed to bootstrap a [Speakeasy managed SDK repository](https://speakeasyapi.dev/docs/create-client-sdks/) using Github's repository clone feature. Once this repository is setup it will automatically keep your SDK up to date and published to a package manager. 


### Creating an SDK

1. To get started, simply clone the repository by clicking on the "Use template" button and give it a name.
   
![Screenshot 2023-09-06 at 09 20 52](https://github.com/speakeasy-sdks/template-sdk/assets/68016351/b4cf4e43-db4e-455a-9359-0f09f942b997)

3. Configure the Speakeasy workflow to generate the SDK. Go to the [generation workflow file](https://github.com/speakeasy-sdks/template-sdk/blob/main/.github/workflows/speakeasy_sdk_generation.yml) and configure the `language`, `mode` and `location` of your openapi document. For complete documentation on all the available generation configurations, see [here](https://speakeasyapi.dev/docs/create-client-sdks/advanced-setup/github-setup/). You will also need to add a `SPEAKEASY_API_KEY` as a repository secret. If you don't already have a key you can get one by making a workspace on Speakeasy [here](https://app.speakeasyapi.dev/workspaces/cl6augut900003b6b06012z1s).

4. Configure the Speakeasy workflow to publish the SDK. Go to the [publishing workflow file](https://github.com/speakeasy-sdks/template-sdk/blob/main/.github/workflows/speakeasy_sdk_publish.yml) and configure any relevant package manager credentials as repository secrets. For complete documentation on all the available publishing configurations, see [here](https://speakeasyapi.dev/docs/package-publishing/).

5. Configure the generation by editing the `gen.yaml` file in the root of the repo. This file controls the generator and determines various attributes of the SDK like `packageName`, `sdkClassName`, inlining of parameters, and other ergonomics.

6. Finally go to the Actions tab, choose the generation workflow and click "Force Generate". This will trigger a new generation of your SDK using the configuration you provided above. Depending on whether you configured `pr` or `direct` mode above your updated SDK will appear in PR or in the main branch.

![Screenshot 2023-09-06 at 10 01 46](https://github.com/speakeasy-sdks/template-sdk/assets/68016351/35828982-c6de-4a5c-84f5-ae2b4224cece)

🚀 You should have a working SDK for your API 🙂 . To check out all the features of the SDK please see our docs [site](https://speakeasyapi.dev/docs/create-client-sdks/).

### Local development

Once you have the SDK setup you may want to iterate on the SDK. Speakeasy supports OpenAPI vendor extensions that can be added to your spec to customize the SDK ergonomics (method names, namespacing resources etc.) and functionality (adding retries, pagination, multiple server support etc)

To get started install the Speakeasy CLI.

In your terminal, run:

```bash
brew install speakeasy-api/homebrew-tap/speakeasy
```
Once you annonate your spec with an extension you will want to run `speakeasy validate` to check the spec for correctness and `speakeasy generate` to recreate the SDK locally. More documentation on OpenAPI extensions [here](https://speakeasyapi.dev/docs/customize-sdks/namespaces/). Here's an example of adding a multiple server support to the spec so that your SDK supports production and sandbox versions of your API. 

```yaml
info:
  title: Example
  version: 0.0.1
servers:
  - url: https://prod.example.com # Used as the default URL by the SDK
    description: Our production environment
    x-speakeasy-server-id: prod
  - url: https://sandbox.example.com
    description: Our sandbox environment
    x-speakeasy-server-id: sandbox
```

Once you're finished iterating and happy with the output push only the latest version of spec into the repo and regenerate the SDK using step 6 above.

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/kombo-sdk.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.custom_endpoints.get_custom_datev_data_pushes(x_integration_id='string')

if res.get_custom_datev_data_pushes_successful_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [custom_endpoints](docs/sdks/customendpoints/README.md)

* [get_custom_datev_data_pushes](docs/sdks/customendpoints/README.md#get_custom_datev_data_pushes) - Get DATEV data pushes
* [post_custom_datev_passthrough](docs/sdks/customendpoints/README.md#post_custom_datev_passthrough) - Write raw DATEV ASCII file
* [post_custom_datev_push_data_general](docs/sdks/customendpoints/README.md#post_custom_datev_push_data_general) - Push general data to DATEV
* [post_custom_datev_push_data_payroll](docs/sdks/customendpoints/README.md#post_custom_datev_push_data_payroll) - Push payroll data to DATEV
* [put_custom_datev_employees_employee_id_compensations](docs/sdks/customendpoints/README.md#put_custom_datev_employees_employee_id_compensations) - Set DATEV compensations
* [put_custom_datev_employees_employee_id_prepare_payroll](docs/sdks/customendpoints/README.md#put_custom_datev_employees_employee_id_prepare_payroll) - Prepare DATEV Payroll

### [general](docs/sdks/general/README.md)

* [delete_integrations_integration_id](docs/sdks/general/README.md#delete_integrations_integration_id) - Delete integration
* [get_check_api_key](docs/sdks/general/README.md#get_check_api_key) - Check API key
* [get_integrations_integration_id](docs/sdks/general/README.md#get_integrations_integration_id) - Get integration details
* [get_tools_category](docs/sdks/general/README.md#get_tools_category) - Get tools
* [post_force_sync](docs/sdks/general/README.md#post_force_sync) - Trigger sync
* [post_integrations_integration_id_relink](docs/sdks/general/README.md#post_integrations_integration_id_relink) - Create reconnection link
* [post_passthrough_tool_api](docs/sdks/general/README.md#post_passthrough_tool_api) - Send passthrough request

### [kombo_connect](docs/sdks/komboconnect/README.md)

* [post_connect_activate_integration](docs/sdks/komboconnect/README.md#post_connect_activate_integration) - Activate integration
* [post_connect_create_link](docs/sdks/komboconnect/README.md#post_connect_create_link) - Create connection link

### [unified_ats_assessment_api](docs/sdks/unifiedatsassessmentapi/README.md)

* [get_assessment_orders_open](docs/sdks/unifiedatsassessmentapi/README.md#get_assessment_orders_open) - Get open orders
* [get_assessment_packages](docs/sdks/unifiedatsassessmentapi/README.md#get_assessment_packages) - Get packages
* [put_assessment_orders_assessment_order_id_result](docs/sdks/unifiedatsassessmentapi/README.md#put_assessment_orders_assessment_order_id_result) - Update order result
* [put_assessment_packages](docs/sdks/unifiedatsassessmentapi/README.md#put_assessment_packages) - Set packages

### [unified_ats_api](docs/sdks/unifiedatsapi/README.md)

* [delete_ats_candidates_candidate_id_tags](docs/sdks/unifiedatsapi/README.md#delete_ats_candidates_candidate_id_tags) - Remove tag from candidate
* [get_ats_application_stages](docs/sdks/unifiedatsapi/README.md#get_ats_application_stages) - Get application stages
* [get_ats_applications](docs/sdks/unifiedatsapi/README.md#get_ats_applications) - Get applications
* [get_ats_candidates](docs/sdks/unifiedatsapi/README.md#get_ats_candidates) - Get candidates
* [get_ats_jobs](docs/sdks/unifiedatsapi/README.md#get_ats_jobs) - Get jobs
* [get_ats_tags](docs/sdks/unifiedatsapi/README.md#get_ats_tags) - Get tags
* [get_ats_users](docs/sdks/unifiedatsapi/README.md#get_ats_users) - Get users
* [patch_ats_candidates_candidate_id](docs/sdks/unifiedatsapi/README.md#patch_ats_candidates_candidate_id) - Update candidate 🦄
* [post_ats_applications_application_id_notes](docs/sdks/unifiedatsapi/README.md#post_ats_applications_application_id_notes) - Add note to application
* [post_ats_applications_application_id_result_links](docs/sdks/unifiedatsapi/README.md#post_ats_applications_application_id_result_links) - Add result link to application
* [post_ats_candidates](docs/sdks/unifiedatsapi/README.md#post_ats_candidates) - Create candidate
* [post_ats_candidates_candidate_id_attachments](docs/sdks/unifiedatsapi/README.md#post_ats_candidates_candidate_id_attachments) - Add attachment to candidate
* [post_ats_candidates_candidate_id_result_links](docs/sdks/unifiedatsapi/README.md#post_ats_candidates_candidate_id_result_links) - Add result link to candidate
* [post_ats_candidates_candidate_id_tags](docs/sdks/unifiedatsapi/README.md#post_ats_candidates_candidate_id_tags) - Add tag to candidate
* [post_ats_jobs_job_id_applications](docs/sdks/unifiedatsapi/README.md#post_ats_jobs_job_id_applications) - Create application
* [put_ats_applications_application_id_stage](docs/sdks/unifiedatsapi/README.md#put_ats_applications_application_id_stage) - Move application to stage

### [unified_hris_api](docs/sdks/unifiedhrisapi/README.md)

* [delete_hris_absences_absence_id](docs/sdks/unifiedhrisapi/README.md#delete_hris_absences_absence_id) - Delete absence
* [get_hris_absence_types](docs/sdks/unifiedhrisapi/README.md#get_hris_absence_types) - Get absence types
* [get_hris_absences](docs/sdks/unifiedhrisapi/README.md#get_hris_absences) - Get absences
* [get_hris_employees](docs/sdks/unifiedhrisapi/README.md#get_hris_employees) - Get employees
* [get_hris_employments](docs/sdks/unifiedhrisapi/README.md#get_hris_employments) - Get employments
* [get_hris_groups](docs/sdks/unifiedhrisapi/README.md#get_hris_groups) - Get groups
* [get_hris_legal_entities](docs/sdks/unifiedhrisapi/README.md#get_hris_legal_entities) - Get legal entities
* [get_hris_locations](docs/sdks/unifiedhrisapi/README.md#get_hris_locations) - Get locations
* [get_hris_teams](docs/sdks/unifiedhrisapi/README.md#get_hris_teams) - Get teams (deprecated)
* [get_hris_time_off_balances](docs/sdks/unifiedhrisapi/README.md#get_hris_time_off_balances) - Get time off balances
* [patch_hris_employees_employee_id](docs/sdks/unifiedhrisapi/README.md#patch_hris_employees_employee_id) - Update employee
* [post_hris_absences](docs/sdks/unifiedhrisapi/README.md#post_hris_absences) - Create absence
* [post_hris_employees](docs/sdks/unifiedhrisapi/README.md#post_hris_employees) - Create employee
* [post_hris_employees_employee_id_attachments](docs/sdks/unifiedhrisapi/README.md#post_hris_employees_employee_id_attachments) - Add attachment to employees 🦄
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.kombo.dev/v1` | None |

For example:


```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
    server_idx=0
)


res = s.custom_endpoints.get_custom_datev_data_pushes(x_integration_id='string')

if res.get_custom_datev_data_pushes_successful_response is not None:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
    server_url="https://api.kombo.dev/v1"
)


res = s.custom_endpoints.get_custom_datev_data_pushes(x_integration_id='string')

if res.get_custom_datev_data_pushes_successful_response is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import kombo
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = kombo.Kombo(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
