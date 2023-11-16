# DeleteAtsCandidatesCandidateIDTagsRequestBody

DELETE /ats/candidates/:candidate_id/tags request body


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `remote_fields`                                                              | [Optional[operations.RemoteFields]](../../models/operations/remotefields.md) | :heavy_minus_sign:                                                           | Additional fields that we will pass through to specific ATS systems.         |
| `tag`                                                                        | [operations.Tag](../../models/operations/tag.md)                             | :heavy_check_mark:                                                           | N/A                                                                          |