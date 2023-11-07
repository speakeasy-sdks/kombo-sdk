# PostCustomDatevPassthroughCustomEndpointsResponseBody

Returned when the passed integration is inactive.


## Fields

| Field                                                                                                                            | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `raw_response`                                                                                                                   | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                                            | :heavy_minus_sign:                                                                                                               | Raw HTTP response; suitable for custom response parsing                                                                          |
| `error`                                                                                                                          | [errors.PostCustomDatevPassthroughCustomEndpointsError](../../models/errors/postcustomdatevpassthroughcustomendpointserror.md)   | :heavy_check_mark:                                                                                                               | N/A                                                                                                                              |
| `status`                                                                                                                         | [errors.PostCustomDatevPassthroughCustomEndpointsStatus](../../models/errors/postcustomdatevpassthroughcustomendpointsstatus.md) | :heavy_check_mark:                                                                                                               | N/A                                                                                                                              |