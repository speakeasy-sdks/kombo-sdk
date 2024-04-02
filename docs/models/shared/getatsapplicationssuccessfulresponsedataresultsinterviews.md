# GetAtsApplicationsSuccessfulResponseDataResultsInterviews


## Fields

| Field                                                                                                                                                                              | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ending_at`                                                                                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                               | :heavy_check_mark:                                                                                                                                                                 | The end time of the interview.<br/><br/>[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)                                      |
| `id`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                 | The globally unique Kombo ID of the interview.                                                                                                                                     |
| `location`                                                                                                                                                                         | [Optional[shared.GetAtsApplicationsSuccessfulResponseDataResultsInterviewsLocation]](undefined/models/shared/getatsapplicationssuccessfulresponsedataresultsinterviewslocation.md) | :heavy_check_mark:                                                                                                                                                                 | Location of the interview.                                                                                                                                                         |
| `remote_id`                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                 | The ID of the interview in the integrated system.                                                                                                                                  |
| `starting_at`                                                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                               | :heavy_check_mark:                                                                                                                                                                 | The start time of the interview.<br/><br/>[](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)                                    |
| `title`                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                 | The title of the interview.                                                                                                                                                        |