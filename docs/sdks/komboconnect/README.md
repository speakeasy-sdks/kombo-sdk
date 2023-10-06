# KomboConnect
(*kombo_connect*)

## Overview

Endpoints for Kombo Connect, our end-user-facing flow for setting up new integrations.

### Available Operations

* [post_connect_activate_integration](#post_connect_activate_integration) - Activate integration
* [post_connect_create_link](#post_connect_create_link) - Create connection link

## post_connect_activate_integration

Activate an integration that was just created via Kombo Connect.

> Check out [our full guide](/connect/embedded-flow) for more details about implementing the connection flow into your app.

### Example Request Body

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZXNzYWdlIjoiVGhpcyBpcyBub3QgYW4gYWN0dWFsIHRva2VuLiJ9.JulqgOZBMKceI8vh9YLpVX51efND0ZyfUNHDXLrPz_4"
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

req = operations.PostConnectActivateIntegrationRequestBody(
    token='application',
)

res = s.kombo_connect.post_connect_activate_integration(req)

if res.post_connect_activate_integration_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PostConnectActivateIntegrationRequestBody](../../models/operations/postconnectactivateintegrationrequestbody.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.PostConnectActivateIntegrationResponse](../../models/operations/postconnectactivateintegrationresponse.md)**


## post_connect_create_link

Generate a unique link that allows your user to enter the embedded Kombo Connect flow.

> Check out [our full guide](/connect/embedded-flow) for more details about implementing the connection flow into your app.

> Kombo will not deduplicate integrations for you that are created with this endpoint. You are responsible for keeping track of integrations in your system and prevent customers from connecting the same tool again. Use the [reconnection link](/v1/post-integrations-integration-id-relink) endpoint if you want a customer to update their credentials.

### Example Request Body

```json
{
  "end_user_email": "test@example.com",
  "end_user_organization_name": "Test Inc.",
  "end_user_origin_id": "123",
  "integration_category": "HRIS",
  "integration_tool": "personio",
  "language": "en"
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

req = operations.PostConnectCreateLinkRequestBody(
    end_user_email='Barney59@yahoo.com',
    end_user_organization_name='Peso Cotton',
    end_user_origin_id='Roentgenium Honda reinvent',
    integration_category=operations.PostConnectCreateLinkRequestBodyIntegrationCategory.ATS,
    integration_tool=operations.PostConnectCreateLinkRequestBodyIntegrationTool.GREENHOUSE,
    language=operations.PostConnectCreateLinkRequestBodyLanguage.EN,
    remote_environment='platforms male',
    scope_config_id='Cis Northeast Chrysler',
)

res = s.kombo_connect.post_connect_create_link(req)

if res.post_connect_create_link_successful_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PostConnectCreateLinkRequestBody](../../models/operations/postconnectcreatelinkrequestbody.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PostConnectCreateLinkResponse](../../models/operations/postconnectcreatelinkresponse.md)**

