# PostAtsCandidatesRequestBodyRemoteFieldsSuccessfactors

Fields specific to SAP SuccessFactors.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `candidate`                                                                  | Dict[str, *Any*]                                                             | :heavy_minus_sign:                                                           | Fields that we will pass through to SuccessFactor's `Candidate` object.      |
| `job_application`                                                            | Dict[str, *Any*]                                                             | :heavy_minus_sign:                                                           | Fields that we will pass through to SuccessFactor's `JobApplication` object. |