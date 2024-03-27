# PostForceSyncResponseBody

Returned when the authentication header was invalid or missing.


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `error`                                                                               | [errors.PostForceSyncError](../../models/errors/postforcesyncerror.md)                | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `status`                                                                              | [errors.PostForceSyncStatus](../../models/errors/postforcesyncstatus.md)              | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | Raw HTTP response; suitable for custom response parsing                               |