# GetHrisEmployeesResponseBody

Returned when the authentication header was invalid or missing.


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | Raw HTTP response; suitable for custom response parsing                               |
| `error`                                                                               | [errors.GetHrisEmployeesError](../../models/errors/gethrisemployeeserror.md)          | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `status`                                                                              | [errors.GetHrisEmployeesStatus](../../models/errors/gethrisemployeesstatus.md)        | :heavy_check_mark:                                                                    | N/A                                                                                   |