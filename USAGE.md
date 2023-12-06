<!-- Start SDK Example Usage [usage] -->
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
)

res = s.default.post_e_ingest_events_v2(req)

if res.object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->