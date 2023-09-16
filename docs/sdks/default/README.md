# Default

### Available Operations

* [post_e_ingest_events_v2](#post_e_ingest_events_v2) - Ingestion V2

## post_e_ingest_events_v2

Ingestion V2

### Example Usage

```python
import test
from test.models import operations

s = test.Test()

req = operations.PostEIngestEventsV2Request(
    request_body=operations.PostEIngestEventsV2RequestBody(),
    x_request_org='provident',
)

res = s.default.post_e_ingest_events_v2(req, operations.PostEIngestEventsV2Security(
    bearer_auth="",
))

if res.post_e_ingest_events_v2_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PostEIngestEventsV2Request](../../models/operations/posteingesteventsv2request.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.PostEIngestEventsV2Security](../../models/operations/posteingesteventsv2security.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.PostEIngestEventsV2Response](../../models/operations/posteingesteventsv2response.md)**

