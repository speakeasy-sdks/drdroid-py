# Default
(*default*)

### Available Operations

* [post_e_ingest_events_v2](#post_e_ingest_events_v2) - Ingestion V2

## post_e_ingest_events_v2

Ingestion V2

### Example Usage

```python
import test
from test.models import operations, shared

s = test.Test(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
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

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PostEIngestEventsV2Request](../../models/operations/posteingesteventsv2request.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.PostEIngestEventsV2Response](../../models/operations/posteingesteventsv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
