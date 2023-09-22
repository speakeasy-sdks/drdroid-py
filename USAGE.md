<!-- Start SDK Example Usage -->


```python
import test
from test.models import operations, shared

s = test.Test(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.PostEIngestEventsV2Request(
    request_body=operations.PostEIngestEventsV2RequestBody(),
    x_request_org='corrupti',
)

res = s.default.post_e_ingest_events_v2(req)

if res.post_e_ingest_events_v2_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->