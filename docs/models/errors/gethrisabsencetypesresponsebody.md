# GetHrisAbsenceTypesResponseBody

Returned when the authentication header was invalid or missing.


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `error`                                                                               | [errors.GetHrisAbsenceTypesError](../../models/errors/gethrisabsencetypeserror.md)    | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `status`                                                                              | [errors.GetHrisAbsenceTypesStatus](../../models/errors/gethrisabsencetypesstatus.md)  | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | Raw HTTP response; suitable for custom response parsing                               |