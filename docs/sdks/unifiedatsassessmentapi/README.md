# UnifiedATSAssessmentAPI
(*.unified_ats_assessment_api*)

### Available Operations

* [get_assessment_orders_open](#get_assessment_orders_open) - Get open orders
* [get_assessment_packages](#get_assessment_packages) - Get packages
* [put_assessment_orders_assessment_order_id_result](#put_assessment_orders_assessment_order_id_result) - Update order result
* [put_assessment_packages](#put_assessment_packages) - Set packages

## get_assessment_orders_open

Get all open assessment orders of an integration.

### Example Usage

```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_assessment_api.get_assessment_orders_open(x_integration_id='string', cursor='string', page_size=927886)

if res.get_assessment_orders_open_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                           | *str*                                                                                                                        | :heavy_check_mark:                                                                                                           | ID of the integration you want to interact with.                                                                             |
| `cursor`                                                                                                                     | *Optional[str]*                                                                                                              | :heavy_minus_sign:                                                                                                           | An optional cursor string used for pagination. This can be retrieved from the `next` property of the previous page response. |
| `page_size`                                                                                                                  | *Optional[int]*                                                                                                              | :heavy_minus_sign:                                                                                                           | The number of results to return per page.                                                                                    |


### Response

**[operations.GetAssessmentOrdersOpenResponse](../../models/operations/getassessmentordersopenresponse.md)**


## get_assessment_packages

Get all available assessment packages for an integration.

This is mainly intended for debugging. As you always need to submit the full list of available packages when using ["set packages"](/assessment/v1/put-packages), there shouldn't ever be a need to call this endpoint in production.

### Example Usage

```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_assessment_api.get_assessment_packages(x_integration_id='string')

if res.get_assessment_packages_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                        | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `x_integration_id`                               | *str*                                            | :heavy_check_mark:                               | ID of the integration you want to interact with. |


### Response

**[operations.GetAssessmentPackagesResponse](../../models/operations/getassessmentpackagesresponse.md)**


## put_assessment_orders_assessment_order_id_result

Updates an assessment order result.

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
  src="https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Recruitee</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Greenhouse</li>
<li style={{display: 'flex', alignItems: 'center'}}><img
  src="https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg"
  style={{"width":"16px","height":"16px","marginTop":"0 !important","marginBottom":"0 !important","marginRight":"8px !important"}}
/>Ashby</li>
</ul>

You'd like to see this feature for another integration? Please reach out!
We're always happy to discuss extending our coverage.
</Accordion>
### Example Request Body

```json
{
  "status": "COMPLETED",
  "result_url": "https://example.com",
  "completed_at": "2023-04-04T00:00:00.000Z",
  "score": 90,
  "max_score": 100,
  "attributes": [
    {
      "field": "remarks",
      "value": "Test completed with passing score"
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
        api_key="",
    ),
)


res = s.unified_ats_assessment_api.put_assessment_orders_assessment_order_id_result(x_integration_id='string', assessment_order_id='string', request_body=operations.PutAssessmentOrdersAssessmentOrderIDResultRequestBody(
    attributes=[
        operations.Attributes(
            field='string',
            value='string',
        ),
    ],
    completed_at=dateutil.parser.isoparse('2023-02-12T07:45:50.009Z'),
    result_url='https://white-theism.biz',
    status=operations.Status.OPEN,
))

if res.put_assessment_orders_assessment_order_id_result_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                                                             | *str*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                             | ID of the integration you want to interact with.                                                                                                               |
| `assessment_order_id`                                                                                                                                          | *str*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                             | PUT /assessment/orders/:assessment_order_id/result parameter                                                                                                   |
| `request_body`                                                                                                                                                 | [Optional[operations.PutAssessmentOrdersAssessmentOrderIDResultRequestBody]](../../models/operations/putassessmentordersassessmentorderidresultrequestbody.md) | :heavy_minus_sign:                                                                                                                                             | PUT /assessment/orders/:assessment_order_id/result request body                                                                                                |


### Response

**[operations.PutAssessmentOrdersAssessmentOrderIDResultResponse](../../models/operations/putassessmentordersassessmentorderidresultresponse.md)**


## put_assessment_packages

Replaces the list of available assessment packages.

Packages that have been previously submitted through this endpoint but aren't included again will be marked as deleted.

### Example Usage

```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_assessment_api.put_assessment_packages(x_integration_id='string', request_body=operations.PutAssessmentPackagesRequestBody(
    packages=[
        operations.Packages(
            description='Future-proofed 5th generation framework',
            id='<ID>',
            name='string',
            type=operations.Type.BEHAVIORAL,
        ),
    ],
))

if res.put_assessment_packages_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                                                   | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | ID of the integration you want to interact with.                                                                     |
| `request_body`                                                                                                       | [Optional[operations.PutAssessmentPackagesRequestBody]](../../models/operations/putassessmentpackagesrequestbody.md) | :heavy_minus_sign:                                                                                                   | PUT /assessment/packages request body                                                                                |


### Response

**[operations.PutAssessmentPackagesResponse](../../models/operations/putassessmentpackagesresponse.md)**

