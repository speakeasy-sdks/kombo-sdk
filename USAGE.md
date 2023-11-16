<!-- Start SDK Example Usage -->
```python
import kombo
from kombo.models import operations, shared

s = kombo.Kombo(
    security=shared.Security(
        api_key="",
    ),
)


res = s.unified_ats_assessment_api.get_assessment_orders_open(x_integration_id='string', cursor='string', page_size=927886)

if res.get_assessment_orders_open_successful_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->