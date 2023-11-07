# Employments


## Fields

| Field                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `changed_at`                                                                                                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                               | YYYY-MM-DDTHH:mm:ss.sssZ<br/><br/>[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)                                                                                                          |
| `effective_date`                                                                                                                                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                               | YYYY-MM-DDTHH:mm:ss.sssZ<br/><br/>[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)                                                                                                          |
| `employee_id`                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                              |
| `employment_type`                                                                                                                                                                                                                                | [Optional[Union[shared.GetHrisEmployeesSuccessfulResponseSchemasDataResultsEmployments1, str]]](../../models/shared/gethrisemployeessuccessfulresponseschemasemploymenttype.md)                                                                  | :heavy_check_mark:                                                                                                                                                                                                                               | One of 8 standardized values (`FULL_TIME`, `PART_TIME`, `CONTRACT`, `INTERNSHIP`, `FREELANCE`, `WORKING_STUDENT`, `APPRENTICESHIP`, or `TRAINING`) **or** — in rare cases where can't find a clear mapping — the original string passed through. |
| `id`                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                              |
| `job_title`                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                               | **(⚠️ Deprecated)** We now provide the `job_title` directly on the employee model.                                                                                                                                                               |
| `pay_currency`                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                               | Pay currency usually returned in [ISO 4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).                                                                                                                                    |
| `pay_frequency`                                                                                                                                                                                                                                  | [Optional[Union[shared.GetHrisEmployeesSuccessfulResponseSchemasDataResultsEmploymentsPayFrequency1, str]]](../../models/shared/gethrisemployeessuccessfulresponsepayfrequency.md)                                                               | :heavy_check_mark:                                                                                                                                                                                                                               | One of 9 standardized values (`DAILY`, `WEEKLY`, `BIWEEKLY`, `MONTHLY`, `SEMIMONTHLY`, `QUARTERLY`, `SEMIANNUALLY`, `ANNUALLY`, or `PRO_RATA`) **or** — in rare cases where can't find a clear mapping — the original string passed through.     |
| `pay_period`                                                                                                                                                                                                                                     | [Optional[Union[shared.GetHrisEmployeesSuccessfulResponseSchemasDataResultsEmploymentsPayPeriod1, str]]](../../models/shared/gethrisemployeessuccessfulresponsepayperiod.md)                                                                     | :heavy_check_mark:                                                                                                                                                                                                                               | One of 10 standardized values (`HOUR`, `DAY`, `WEEK`, `TWO_WEEKS`, `HALF_MONTH`, `MONTH`, `TWO_MONTHS`, `QUARTER`, `HALF_YEAR`, or `YEAR`) **or** — in rare cases where can't find a clear mapping — the original string passed through.         |
| `pay_rate`                                                                                                                                                                                                                                       | *Optional[float]*                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                              |
| `remote_data`                                                                                                                                                                                                                                    | Dict[str, *Any*]                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                              |
| `remote_deleted_at`                                                                                                                                                                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                               | YYYY-MM-DDTHH:mm:ss.sssZ<br/><br/>[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)                                                                                                          |
| `remote_id`                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                              |