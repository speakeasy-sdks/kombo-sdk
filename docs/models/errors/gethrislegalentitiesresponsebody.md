# GetHrisLegalEntitiesResponseBody

Returned when the authentication header was invalid or missing.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `error`                                                                                | [errors.GetHrisLegalEntitiesError](../../models/errors/gethrislegalentitieserror.md)   | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `status`                                                                               | [errors.GetHrisLegalEntitiesStatus](../../models/errors/gethrislegalentitiesstatus.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `raw_response`                                                                         | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)  | :heavy_minus_sign:                                                                     | Raw HTTP response; suitable for custom response parsing                                |