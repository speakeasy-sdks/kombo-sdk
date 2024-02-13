# CustomEndpoints
(*custom_endpoints*)

### Available Operations

* [get_custom_datev_data_pushes](#get_custom_datev_data_pushes) - Get DATEV data pushes
* [post_custom_datev_passthrough](#post_custom_datev_passthrough) - Write raw DATEV ASCII file
* [post_custom_datev_push_data_general](#post_custom_datev_push_data_general) - Push general data to DATEV
* [post_custom_datev_push_data_payroll](#post_custom_datev_push_data_payroll) - Push payroll data to DATEV
* [put_custom_datev_employees_employee_id_compensations](#put_custom_datev_employees_employee_id_compensations) - Set DATEV compensations
* [put_custom_datev_employees_employee_id_prepare_payroll](#put_custom_datev_employees_employee_id_prepare_payroll) - Prepare DATEV Payroll

## get_custom_datev_data_pushes

Returns all "DATEV Data Pushes" of the last 2 months. You can use this endpoint to give your users transparency about submitted "ASCII-Files" and their status. Each data push can contain multiple files that were submitted.

### Example Usage

```python
import kombo
from kombo.models import shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.custom_endpoints.get_custom_datev_data_pushes(x_integration_id='string')

if res.get_custom_datev_data_pushes_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                        | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `x_integration_id`                               | *str*                                            | :heavy_check_mark:                               | ID of the integration you want to interact with. |


### Response

**[operations.GetCustomDatevDataPushesResponse](../../models/operations/getcustomdatevdatapushesresponse.md)**
### Errors

| Error Object                                                          | Status Code                                                           | Content Type                                                          |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| errors.GetCustomDatevDataPushesErrorResponse                          | 400                                                                   | application/json                                                      |
| errors.GetCustomDatevDataPushesResponseBody                           | 401                                                                   | application/json                                                      |
| errors.GetCustomDatevDataPushesCustomEndpointsResponseBody            | 403                                                                   | application/json                                                      |
| errors.GetCustomDatevDataPushesCustomEndpointsResponseResponseBody    | 404                                                                   | application/json                                                      |
| errors.GetCustomDatevDataPushesCustomEndpointsResponse503ResponseBody | 503                                                                   | application/json                                                      |
| errors.SDKError                                                       | 4x-5xx                                                                | */*                                                                   |

## post_custom_datev_passthrough

This action allows to send an arbitrary ASCII file directly to DATEV LODAS or Lohn und Gehalt. Kombo adds validation for the file format but not on the content. This action allows you to implement any use case that you might have with DATEV payroll ASCII imports.

### Example Usage

```python
import dateutil.parser
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.custom_endpoints.post_custom_datev_passthrough(x_integration_id='string', request_body=operations.PostCustomDatevPassthroughRequestBody(
    accounting_month=dateutil.parser.isoparse('2023-07-07T11:18:39.230Z'),
    file_content='string',
    file_name='road_bedfordshire.jpg',
    file_type=operations.FileType.STAMMDATEN,
    target_system=operations.TargetSystem.LODAS,
))

if res.post_custom_datev_passthrough_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `x_integration_id`                                                                                                             | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | ID of the integration you want to interact with.                                                                               |
| `request_body`                                                                                                                 | [Optional[operations.PostCustomDatevPassthroughRequestBody]](../../models/operations/postcustomdatevpassthroughrequestbody.md) | :heavy_minus_sign:                                                                                                             | POST /custom/datev/passthrough request body                                                                                    |


### Response

**[operations.PostCustomDatevPassthroughResponse](../../models/operations/postcustomdatevpassthroughresponse.md)**
### Errors

| Error Object                                                            | Status Code                                                             | Content Type                                                            |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| errors.PostCustomDatevPassthroughErrorResponse                          | 400                                                                     | application/json                                                        |
| errors.PostCustomDatevPassthroughResponseBody                           | 401                                                                     | application/json                                                        |
| errors.PostCustomDatevPassthroughCustomEndpointsResponseBody            | 403                                                                     | application/json                                                        |
| errors.PostCustomDatevPassthroughCustomEndpointsResponseResponseBody    | 404                                                                     | application/json                                                        |
| errors.PostCustomDatevPassthroughCustomEndpointsResponse503ResponseBody | 503                                                                     | application/json                                                        |
| errors.SDKError                                                         | 4x-5xx                                                                  | */*                                                                     |

## post_custom_datev_push_data_general

Uploads the currently relevant general data (employees, compensations, and time offs) to DATEV. This will create so called ASCII files that the accountant has to import in DATEV. You can call this endpoint to implement an on-demand sync to DATEV, for example if you want to offer your users a button to do that in your application.

### Example Usage

```python
import kombo
from kombo.models import shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.custom_endpoints.post_custom_datev_push_data_general(x_integration_id='string', post_custom_datev_push_data_general_request_body=shared.PostCustomDatevPushDataGeneralRequestBody())

if res.post_custom_datev_push_data_general_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `x_integration_id`                                                                                                             | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | ID of the integration you want to interact with.                                                                               |
| `post_custom_datev_push_data_general_request_body`                                                                             | [Optional[shared.PostCustomDatevPushDataGeneralRequestBody]](../../models/shared/postcustomdatevpushdatageneralrequestbody.md) | :heavy_minus_sign:                                                                                                             | POST /custom/datev/push-data/general request body                                                                              |


### Response

**[operations.PostCustomDatevPushDataGeneralResponse](../../models/operations/postcustomdatevpushdatageneralresponse.md)**
### Errors

| Error Object                                                                | Status Code                                                                 | Content Type                                                                |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| errors.PostCustomDatevPushDataGeneralErrorResponse                          | 400                                                                         | application/json                                                            |
| errors.PostCustomDatevPushDataGeneralResponseBody                           | 401                                                                         | application/json                                                            |
| errors.PostCustomDatevPushDataGeneralCustomEndpointsResponseBody            | 403                                                                         | application/json                                                            |
| errors.PostCustomDatevPushDataGeneralCustomEndpointsResponseResponseBody    | 404                                                                         | application/json                                                            |
| errors.PostCustomDatevPushDataGeneralCustomEndpointsResponse503ResponseBody | 503                                                                         | application/json                                                            |
| errors.SDKError                                                             | 4x-5xx                                                                      | */*                                                                         |

## post_custom_datev_push_data_payroll

Uploads the currently relevant payroll data (supplements) to DATEV. This will create so called ASCII files that the accountant has to import in DATEV. After finishing the payroll preparation or after correcting payroll, you can call this.

### Example Usage

```python
import dateutil.parser
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.custom_endpoints.post_custom_datev_push_data_payroll(x_integration_id='string', request_body=operations.PostCustomDatevPushDataPayrollRequestBody(
    payroll_month=dateutil.parser.isoparse('2024-03-19T19:15:18.613Z'),
))

if res.post_custom_datev_push_data_payroll_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                                     | *str*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | ID of the integration you want to interact with.                                                                                       |
| `request_body`                                                                                                                         | [Optional[operations.PostCustomDatevPushDataPayrollRequestBody]](../../models/operations/postcustomdatevpushdatapayrollrequestbody.md) | :heavy_minus_sign:                                                                                                                     | POST /custom/datev/push-data/payroll request body                                                                                      |


### Response

**[operations.PostCustomDatevPushDataPayrollResponse](../../models/operations/postcustomdatevpushdatapayrollresponse.md)**
### Errors

| Error Object                                                                | Status Code                                                                 | Content Type                                                                |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| errors.PostCustomDatevPushDataPayrollErrorResponse                          | 400                                                                         | application/json                                                            |
| errors.PostCustomDatevPushDataPayrollResponseBody                           | 401                                                                         | application/json                                                            |
| errors.PostCustomDatevPushDataPayrollCustomEndpointsResponseBody            | 403                                                                         | application/json                                                            |
| errors.PostCustomDatevPushDataPayrollCustomEndpointsResponseResponseBody    | 404                                                                         | application/json                                                            |
| errors.PostCustomDatevPushDataPayrollCustomEndpointsResponse503ResponseBody | 503                                                                         | application/json                                                            |
| errors.SDKError                                                             | 4x-5xx                                                                      | */*                                                                         |

## put_custom_datev_employees_employee_id_compensations

Sets the compensations for an employee on the specified effective date.

<Accordion title="Supported integrations" icon="list-check">
This feature is currently available for the following integrations:

<ul>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/datev/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>DATEV LODAS</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>

 Other compensations will end at the effective date. That means, if you would like to add a compensation, you also have to include the compensations that you would like to keep.

<Note>
  This endpoint requires the permission **Manage payroll** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "employee_id": "3bdhemmSP1TPQDGWtRveRot9",
  "effective_date": "2022-12-01",
  "compensations": [
    {
      "amount": 4500,
      "currency": "EUR",
      "period": "MONTH",
      "lohnart": 200
    },
    {
      "amount": 30,
      "currency": "EUR",
      "period": "HOUR"
    }
  ]
}
```

### Example Usage

```python
import dateutil.parser
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.custom_endpoints.put_custom_datev_employees_employee_id_compensations(x_integration_id='string', employee_id='string', request_body=operations.PutCustomDatevEmployeesEmployeeIDCompensationsRequestBody(
    compensations=[
        operations.Compensations(
            amount=4500,
            currency=operations.Currency.EUR,
            period=operations.Period.MONTH,
            lohnart=200,
        ),
        operations.Compensations(
            amount=30,
            currency=operations.Currency.EUR,
            period=operations.Period.HOUR,
        ),
    ],
    effective_date=dateutil.parser.isoparse('2022-12-01'),
))

if res.put_custom_datev_employees_employee_id_compensations_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            | Example                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                                                                     | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | ID of the integration you want to interact with.                                                                                                                       |                                                                                                                                                                        |
| `employee_id`                                                                                                                                                          | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | ID of the employee that should be updated. You can use their Kombo `id` or their ID in the remote system by prefixing it with `remote:` (e.g., `remote:12312`)         |                                                                                                                                                                        |
| `request_body`                                                                                                                                                         | [Optional[operations.PutCustomDatevEmployeesEmployeeIDCompensationsRequestBody]](../../models/operations/putcustomdatevemployeesemployeeidcompensationsrequestbody.md) | :heavy_minus_sign:                                                                                                                                                     | PUT /custom/datev/employees/:employee_id/compensations request body                                                                                                    | {"effective_date":"2022-12-01","compensations":[{"amount":4500,"currency":"EUR","period":"MONTH","lohnart":200},{"amount":30,"currency":"EUR","period":"HOUR"}]}       |


### Response

**[operations.PutCustomDatevEmployeesEmployeeIDCompensationsResponse](../../models/operations/putcustomdatevemployeesemployeeidcompensationsresponse.md)**
### Errors

| Error Object                                                                                | Status Code                                                                                 | Content Type                                                                                |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| errors.PutCustomDatevEmployeesEmployeeIDCompensationsErrorResponse                          | 400                                                                                         | application/json                                                                            |
| errors.PutCustomDatevEmployeesEmployeeIDCompensationsResponseBody                           | 401                                                                                         | application/json                                                                            |
| errors.PutCustomDatevEmployeesEmployeeIDCompensationsCustomEndpointsResponseBody            | 403                                                                                         | application/json                                                                            |
| errors.PutCustomDatevEmployeesEmployeeIDCompensationsCustomEndpointsResponseResponseBody    | 404                                                                                         | application/json                                                                            |
| errors.PutCustomDatevEmployeesEmployeeIDCompensationsCustomEndpointsResponse503ResponseBody | 503                                                                                         | application/json                                                                            |
| errors.SDKError                                                                             | 4x-5xx                                                                                      | */*                                                                                         |

## put_custom_datev_employees_employee_id_prepare_payroll

What DATEV requires to prepare payroll is very specific and currently, as DATEV is not providing "read", this is not part of the unified model.

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
  This endpoint requires the permission **Manage payroll** to be enabled in [your scope config](/scopes).
</Note>

### Example Request Body

```json
{
  "employee_id": "EvLV61zdahkN4ftPJbmPCkdv",
  "payroll_run": {
    "date": "2022-05-01"
  },
  "hourly_payments": [
    {
      "hours": 14,
      "lohnart": 200
    },
    {
      "hours": 16,
      "lohnart": 232
    }
  ],
  "fixed_payments": [
    {
      "amount": 560,
      "lohnart": 100
    }
  ]
}
```

### Example Usage

```python
import dateutil.parser
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.custom_endpoints.put_custom_datev_employees_employee_id_prepare_payroll(x_integration_id='string', employee_id='string', request_body=operations.PutCustomDatevEmployeesEmployeeIDPreparePayrollRequestBody(
    fixed_payments=[
        operations.FixedPayments(
            amount=560,
            lohnart=100,
        ),
    ],
    hourly_payments=[
        operations.HourlyPayments(
            hours=14,
            lohnart=200,
        ),
        operations.HourlyPayments(
            hours=16,
            lohnart=232,
        ),
    ],
    payroll_run=operations.PayrollRun(
        date_=dateutil.parser.isoparse('2022-05-01'),
    ),
))

if res.put_custom_datev_employees_employee_id_prepare_payroll_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              | Example                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `x_integration_id`                                                                                                                                                       | *str*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                       | ID of the integration you want to interact with.                                                                                                                         |                                                                                                                                                                          |
| `employee_id`                                                                                                                                                            | *str*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                       | ID of the employee that should be updated. You can use their Kombo `id` or their ID in the remote system by prefixing it with `remote:` (e.g., `remote:12312`)           |                                                                                                                                                                          |
| `request_body`                                                                                                                                                           | [Optional[operations.PutCustomDatevEmployeesEmployeeIDPreparePayrollRequestBody]](../../models/operations/putcustomdatevemployeesemployeeidpreparepayrollrequestbody.md) | :heavy_minus_sign:                                                                                                                                                       | PUT /custom/datev/employees/:employee_id/prepare-payroll request body                                                                                                    | {"payroll_run":{"date":"2022-05-01"},"fixed_payments":[{"amount":560,"lohnart":100}],"hourly_payments":[{"hours":14,"lohnart":200},{"hours":16,"lohnart":232}]}          |


### Response

**[operations.PutCustomDatevEmployeesEmployeeIDPreparePayrollResponse](../../models/operations/putcustomdatevemployeesemployeeidpreparepayrollresponse.md)**
### Errors

| Error Object                                                                                 | Status Code                                                                                  | Content Type                                                                                 |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| errors.PutCustomDatevEmployeesEmployeeIDPreparePayrollErrorResponse                          | 400                                                                                          | application/json                                                                             |
| errors.PutCustomDatevEmployeesEmployeeIDPreparePayrollResponseBody                           | 401                                                                                          | application/json                                                                             |
| errors.PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponseBody            | 403                                                                                          | application/json                                                                             |
| errors.PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponseResponseBody    | 404                                                                                          | application/json                                                                             |
| errors.PutCustomDatevEmployeesEmployeeIDPreparePayrollCustomEndpointsResponse503ResponseBody | 503                                                                                          | application/json                                                                             |
| errors.SDKError                                                                              | 4x-5xx                                                                                       | */*                                                                                          |
