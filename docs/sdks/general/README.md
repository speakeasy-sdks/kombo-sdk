# General
(*general*)

### Available Operations

* [delete_integrations_integration_id](#delete_integrations_integration_id) - Delete integration
* [get_check_api_key](#get_check_api_key) - Check API key
* [get_integrations_integration_id](#get_integrations_integration_id) - Get integration details
* [get_tools_category](#get_tools_category) - Get tools
* [post_force_sync](#post_force_sync) - Trigger sync
* [post_integrations_integration_id_relink](#post_integrations_integration_id_relink) - Create reconnection link
* [post_passthrough_tool_api](#post_passthrough_tool_api) - Send passthrough request

## delete_integrations_integration_id

Delete the specified integration.
**⚠️ This can not be undone!**

### Example Usage

```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.general.delete_integrations_integration_id(integration_id='string', delete_integrations_integration_id_request_body=shared.DeleteIntegrationsIntegrationIDRequestBody())

if res.delete_integrations_integration_id_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `integration_id`                                                                                                                 | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | DELETE /integrations/:integration_id parameter                                                                                   |
| `delete_integrations_integration_id_request_body`                                                                                | [Optional[shared.DeleteIntegrationsIntegrationIDRequestBody]](../../models/shared/deleteintegrationsintegrationidrequestbody.md) | :heavy_minus_sign:                                                                                                               | DELETE /integrations/:integration_id request body                                                                                |


### Response

**[operations.DeleteIntegrationsIntegrationIDResponse](../../models/operations/deleteintegrationsintegrationidresponse.md)**
### Errors

| Error Object                                        | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| errors.DeleteIntegrationsIntegrationIDErrorResponse | 400                                                 | application/json                                    |
| errors.DeleteIntegrationsIntegrationIDResponseBody  | 401                                                 | application/json                                    |
| errors.SDKError                                     | 400-600                                             | */*                                                 |

## get_check_api_key

Check whether your API key is working properly.

### Example Usage

```python
import kombo
from kombo.models import shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.general.get_check_api_key()

if res.get_check_api_key_successful_response is not None:
    # handle response
    pass
```


### Response

**[operations.GetCheckAPIKeyResponse](../../models/operations/getcheckapikeyresponse.md)**
### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GetCheckAPIKeyErrorResponse | 400                                | application/json                   |
| errors.SDKError                    | 400-600                            | */*                                |

## get_integrations_integration_id

Get the specified integration with everything you need to display it to your customer.

### Example Usage

```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.general.get_integrations_integration_id(integration_id='string')

if res.get_integrations_integration_id_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                   | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `integration_id`                            | *str*                                       | :heavy_check_mark:                          | GET /integrations/:integration_id parameter |


### Response

**[operations.GetIntegrationsIntegrationIDResponse](../../models/operations/getintegrationsintegrationidresponse.md)**
### Errors

| Error Object                                     | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| errors.GetIntegrationsIntegrationIDErrorResponse | 400                                              | application/json                                 |
| errors.GetIntegrationsIntegrationIDResponseBody  | 401                                              | application/json                                 |
| errors.SDKError                                  | 400-600                                          | */*                                              |

## get_tools_category

Get a list of the tools (i.e., integrations) enabled in your environment.
 This can (in combination with the `integration_tool` parameter of [the "Create Link" endpoint](/v1/post-create-link)) be used to, for example, display a custom list or grid of available integrations to your end users instead of exposing Kombo Connect's standard tool selector.

### Example Usage

```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.general.get_tools_category(category=shared.GetToolsCategoryParameterCategory.ASSESSMENT)

if res.get_tools_category_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `category`                                                                                           | [shared.GetToolsCategoryParameterCategory](../../models/shared/gettoolscategoryparametercategory.md) | :heavy_check_mark:                                                                                   | GET /tools/:category parameter                                                                       |


### Response

**[operations.GetToolsCategoryResponse](../../models/operations/gettoolscategoryresponse.md)**
### Errors

| Error Object                         | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.GetToolsCategoryErrorResponse | 400                                  | application/json                     |
| errors.SDKError                      | 400-600                              | */*                                  |

## post_force_sync

Trigger a sync for a specific integration.

<Warning>Please note that it is **not** necessary nor recommended to call this endpoint periodically on your side. Kombo already performs period syncs for you and you should only trigger syncs yourself in special cases (like when a user clicks on a "Sync" button in your app).</Warning>

### Example Usage

```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.general.post_force_sync(x_integration_id='string', post_force_sync_request_body=shared.PostForceSyncRequestBody())

if res.post_force_sync_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `x_integration_id`                                                                           | *str*                                                                                        | :heavy_check_mark:                                                                           | ID of the integration you want to interact with.                                             |
| `post_force_sync_request_body`                                                               | [Optional[shared.PostForceSyncRequestBody]](../../models/shared/postforcesyncrequestbody.md) | :heavy_minus_sign:                                                                           | POST /force-sync request body                                                                |


### Response

**[operations.PostForceSyncResponse](../../models/operations/postforcesyncresponse.md)**
### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PostForceSyncErrorResponse | 400                               | application/json                  |
| errors.PostForceSyncResponseBody  | 401                               | application/json                  |
| errors.SDKError                   | 400-600                           | */*                               |

## post_integrations_integration_id_relink

Create a link that will allow the user to reconnect an integration. This is useful if you want to allow your users to update the credentials if the old ones for example expired.

Embed this the same way you would [embed the connect link](/connect/embedded-flow). By default, the link will be valid for 1 hour.

### Example Request Body

```json
{
  "language": "en"
}
```

### Example Usage

```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.general.post_integrations_integration_id_relink(integration_id='string', request_body=operations.PostIntegrationsIntegrationIDRelinkRequestBody())

if res.post_integrations_integration_id_relink_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `integration_id`                                                                                                                                 | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | POST /integrations/:integration_id/relink parameter                                                                                              |
| `request_body`                                                                                                                                   | [Optional[operations.PostIntegrationsIntegrationIDRelinkRequestBody]](../../models/operations/postintegrationsintegrationidrelinkrequestbody.md) | :heavy_minus_sign:                                                                                                                               | POST /integrations/:integration_id/relink request body                                                                                           |


### Response

**[operations.PostIntegrationsIntegrationIDRelinkResponse](../../models/operations/postintegrationsintegrationidrelinkresponse.md)**
### Errors

| Error Object                                            | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| errors.PostIntegrationsIntegrationIDRelinkErrorResponse | 400                                                     | application/json                                        |
| errors.PostIntegrationsIntegrationIDRelinkResponseBody  | 401                                                     | application/json                                        |
| errors.SDKError                                         | 400-600                                                 | */*                                                     |

## post_passthrough_tool_api

Send a request to the specified integration's native API.

At Kombo we put a lot of work into making sure that our unified API covers all our customers' use cases and that they never have to think about integration-specific logic again. There are cases, however, where our customers want to build features that are very integration-specfic. That's where this endpoint comes in.

Pass in details about the request you want to make to the integration's API and we'll forward it for you. We'll also take care of setting the right base URL and authenticating your requests.

To get started, please pick the relevant API (some tools provide multiple to due different base URLs or authentication schemes) from the table below and pass in the `{tool}/{api}` identifier as part of the path.

|Integration|`{tool}/{api}`|Description|
|---|---|---|
|Personio|`personio/personnel`|Personio's [Personnel Data API](https://developer.personio.de/reference/get_company-employees). We automatically authenticate all requests using the client ID and secret and use `https://api.personio.de/v1` as the base URL.|
|SAP SuccessFactors|`successfactors/odata-v2`|[SuccessFactors' OData V2 API](https://help.sap.com/doc/74597e67f54d4f448252bad4c2b601c9/2211/en-US/SF_HCM_OData_API_REF_en.pdf). We automatically authenticate all requests and use `https://{api_domain}/odata/v2` as the base URL.|
|Recruitee|`recruitee/default`|The [Recruitee API](https://api.recruitee.com/docs/index.html). We automatically authenticate all requests and use `https://api.recruitee.com/c/{company_id}` as the base URL.|
|Greenhouse|`greenhouse/harvest`|Greenhouse [Harvest API](https://developers.greenhouse.io/harvest.html). We automatically authenticate all requests using the API key and use `https://harvest.greenhouse.io/v1` as the base URL.|
|Teamtailor|`teamtailor/v1`|Teamtailor's [JSON-API](https://docs.teamtailor.com/). We authenticate all request with the Teamtailor API key and use the base URL `https://api.teamtailor.com/v1`.|
|Personio|`personio/recruiting`|Personio's [Recruiting API](https://developer.personio.de/reference/get_company-employees). We automatically authenticate all requests using the Recruiting access token and use `https://api.personio.de/v1/recruiting` as the base URL.|
|Personio|`personio/jobboard`|API endpoints exposed on Personio's public job board pages ([currently just the XML feed](https://developer.personio.de/reference/get_xml)). We automatically use the right `https://{company}.jobs.personio.de` base URL.|
|BambooHR|`bamboohr/v1`|BambooHR's [API](https://documentation.bamboohr.com/reference/get-employee). We automatically authenticate all requests using the customer credentials `https://api.bamboohr.com/api/gateway.php/{subdomain}/v1` as the base URL.|
|Workable|`workable/v1`|Workable's [API](https://workable.readme.io/reference/generate-an-access-token). We automatically authenticate all requests using the client ID and secret and use `https://subdomain.workable.com/spi/v3` as the base URL.|
|HiBob|`hibob/v1`|[HibBob's v1 API](https://apidocs.hibob.com/reference/get_people). We automatically authenticate all requests using the service user credentials (or, for old integrations, the API key) and use `https://api.hibob.com/v1` as the base URL.|
|Haufe Umantis|`umantis/v1`|[Umantis API v1](https://recruitingapp-91005709.umantis.com/api/v1/swagger-ui). We automatically authenticate all requests and use `https://{subdomain}.umantis.com/api/v1` as the base URL.|

<Note>Please note that the passthrough API endpoints are only meant for edge cases. That's why we only expose them for new integrations after understanding a concrete customer use case. If you have such a use case in mind, please reach out to Kombo.</Note>

### Example Usage

```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="<YOUR_BEARER_TOKEN_HERE>",
    ),
)


res = s.general.post_passthrough_tool_api(api='string', tool='string', request_body=operations.PostPassthroughToolAPIRequestBody(
    api_options={
        'key': 'string',
    },
    headers={
        'key': 'string',
    },
    method=operations.Method.GET,
    params={
        'key': 'string',
    },
    path='/usr/libexec',
))

if res.post_passthrough_tool_api_successful_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `api`                                                                                                                                          | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | The ID of the passthrough API you want to call (some tools provide multiple). Check the endpoint description for a list of all available APIs. |
| `tool`                                                                                                                                         | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | The ID of the tool whose passthrough API you want to call (e.g., `personio`).                                                                  |
| `request_body`                                                                                                                                 | [Optional[operations.PostPassthroughToolAPIRequestBody]](../../models/operations/postpassthroughtoolapirequestbody.md)                         | :heavy_minus_sign:                                                                                                                             | POST /passthrough/:tool/:api request body                                                                                                      |


### Response

**[operations.PostPassthroughToolAPIResponse](../../models/operations/postpassthroughtoolapiresponse.md)**
### Errors

| Error Object                                                | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| errors.PostPassthroughToolAPIErrorResponse                  | 400                                                         | application/json                                            |
| errors.PostPassthroughToolAPIResponseBody                   | 401                                                         | application/json                                            |
| errors.PostPassthroughToolAPIGeneralResponseBody            | 403                                                         | application/json                                            |
| errors.PostPassthroughToolAPIGeneralResponseResponseBody    | 404                                                         | application/json                                            |
| errors.PostPassthroughToolAPIGeneralResponse503ResponseBody | 503                                                         | application/json                                            |
| errors.SDKError                                             | 400-600                                                     | */*                                                         |
