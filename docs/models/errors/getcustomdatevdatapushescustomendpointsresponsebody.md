# GetCustomDatevDataPushesCustomEndpointsResponseBody

Returned when the passed integration is inactive.


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `error`                                                                                        | [errors.GetCustomDatevDataPushesError](../../models/errors/getcustomdatevdatapusheserror.md)   | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `status`                                                                                       | [errors.GetCustomDatevDataPushesStatus](../../models/errors/getcustomdatevdatapushesstatus.md) | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `raw_response`                                                                                 | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)          | :heavy_minus_sign:                                                                             | Raw HTTP response; suitable for custom response parsing                                        |