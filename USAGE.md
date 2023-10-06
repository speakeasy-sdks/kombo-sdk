<!-- Start SDK Example Usage -->


```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.custom_endpoints.get_custom_datev_data_pushes(x_integration_id='magenta')

if res.get_custom_datev_data_pushes_successful_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->