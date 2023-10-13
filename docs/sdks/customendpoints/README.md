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
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.custom_endpoints.get_custom_datev_data_pushes(x_integration_id='magenta')

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


## post_custom_datev_passthrough

This action allows to send an arbitrary ASCII file directly to DATEV LODAS or Lohn und Gehalt. Kombo adds validation for the file format but not on the content. This action allows you to implement any use case that you might have with DATEV payroll ASCII imports.

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


res = s.custom_endpoints.post_custom_datev_passthrough(x_integration_id='generating', request_body=operations.PostCustomDatevPassthroughRequestBody(
    accounting_month=dateutil.parser.isoparse('2023-04-24T14:34:59.751Z'),
    file_content='AI',
    file_name='interface.wav',
    file_type=operations.PostCustomDatevPassthroughRequestBodyFileType.BEWEGUNGSDATEN,
    target_system=operations.PostCustomDatevPassthroughRequestBodyTargetSystem.LODAS,
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


## post_custom_datev_push_data_general

Uploads the currently relevant general data (employees, compensations, and time offs) to DATEV. This will create so called ASCII files that the accountant has to import in DATEV. You can call this endpoint to implement an on-demand sync to DATEV, for example if you want to offer your users a button to do that in your application.

### Example Usage

```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.custom_endpoints.post_custom_datev_push_data_general(x_integration_id='fulfil', post_custom_datev_push_data_general_request_body=shared.PostCustomDatevPushDataGeneralRequestBody())

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


## post_custom_datev_push_data_payroll

Uploads the currently relevant payroll data (supplements) to DATEV. This will create so called ASCII files that the accountant has to import in DATEV. After finishing the payroll preparation or after correcting payroll, you can call this.

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


res = s.custom_endpoints.post_custom_datev_push_data_payroll(x_integration_id='Scandium', request_body=operations.PostCustomDatevPushDataPayrollRequestBody(
    payroll_month=dateutil.parser.isoparse('2021-02-25T13:39:42.284Z'),
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
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.custom_endpoints.put_custom_datev_employees_employee_id_compensations(x_integration_id='Cambridgeshire', employee_id='sensor', request_body=operations.PutCustomDatevEmployeesEmployeeIDCompensationsRequestBody(
    compensations=[
        operations.PutCustomDatevEmployeesEmployeeIDCompensationsRequestBodyCompensations(
            amount=9554.11,
            currency=operations.PutCustomDatevEmployeesEmployeeIDCompensationsRequestBodyCompensationsCurrency.EUR,
            period=operations.PutCustomDatevEmployeesEmployeeIDCompensationsRequestBodyCompensationsPeriod.HOUR,
        ),
    ],
    effective_date=dateutil.parser.isoparse('2022-09-23T20:02:32.324Z'),
))

if res.put_custom_datev_employees_employee_id_compensations_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                                                                     | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | ID of the integration you want to interact with.                                                                                                                       |
| `employee_id`                                                                                                                                                          | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | ID of the employee that should be updated. You can use their Kombo `id` or their ID in the remote system by prefixing it with `remote:` (e.g., `remote:12312`)         |
| `request_body`                                                                                                                                                         | [Optional[operations.PutCustomDatevEmployeesEmployeeIDCompensationsRequestBody]](../../models/operations/putcustomdatevemployeesemployeeidcompensationsrequestbody.md) | :heavy_minus_sign:                                                                                                                                                     | PUT /custom/datev/employees/:employee_id/compensations request body                                                                                                    |


### Response

**[operations.PutCustomDatevEmployeesEmployeeIDCompensationsResponse](../../models/operations/putcustomdatevemployeesemployeeidcompensationsresponse.md)**


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
import kombo
import dateutil.parser
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.custom_endpoints.put_custom_datev_employees_employee_id_prepare_payroll(x_integration_id='ampere', employee_id='bandwidth', request_body=operations.PutCustomDatevEmployeesEmployeeIDPreparePayrollRequestBody(
    fixed_payments=[
        operations.PutCustomDatevEmployeesEmployeeIDPreparePayrollRequestBodyFixedPayments(
            amount=6262.65,
            lohnart=3093.97,
        ),
    ],
    hourly_payments=[
        operations.PutCustomDatevEmployeesEmployeeIDPreparePayrollRequestBodyHourlyPayments(
            hours=2503.18,
            lohnart=2435.37,
        ),
    ],
    payroll_run=operations.PutCustomDatevEmployeesEmployeeIDPreparePayrollRequestBodyPayrollRun(
        date_=dateutil.parser.isoparse('2022-12-07T19:19:50.329Z'),
    ),
))

if res.put_custom_datev_employees_employee_id_prepare_payroll_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `x_integration_id`                                                                                                                                                       | *str*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                       | ID of the integration you want to interact with.                                                                                                                         |
| `employee_id`                                                                                                                                                            | *str*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                       | ID of the employee that should be updated. You can use their Kombo `id` or their ID in the remote system by prefixing it with `remote:` (e.g., `remote:12312`)           |
| `request_body`                                                                                                                                                           | [Optional[operations.PutCustomDatevEmployeesEmployeeIDPreparePayrollRequestBody]](../../models/operations/putcustomdatevemployeesemployeeidpreparepayrollrequestbody.md) | :heavy_minus_sign:                                                                                                                                                       | PUT /custom/datev/employees/:employee_id/prepare-payroll request body                                                                                                    |


### Response

**[operations.PutCustomDatevEmployeesEmployeeIDPreparePayrollResponse](../../models/operations/putcustomdatevemployeesemployeeidpreparepayrollresponse.md)**

