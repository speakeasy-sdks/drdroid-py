# Test

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/drdroid-py.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/bolt-php/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/drdroid-py.git
```
<!-- End SDK Installation -->

## SDK Example Usage
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
)

res = s.default.post_e_ingest_events_v2(req)

if res.post_e_ingest_events_v2_200_application_json_object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [default](docs/sdks/default/README.md)

* [post_e_ingest_events_v2](docs/sdks/default/README.md#post_e_ingest_events_v2) - Ingestion V2
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Pagination -->
# Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
<!-- End Pagination -->



<!-- Start Error Handling -->
# Error Handling

Handling errors in your SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.


<!-- End Error Handling -->



<!-- Start Server Selection -->
# Server Selection

## Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `http://{{endpoint}}` | None |

For example:


```python
import test
from test.models import operations, shared

s = test.Test(
    security=shared.Security(
        bearer_auth="",
    ),
    server_idx=0
)

req = operations.PostEIngestEventsV2Request(
    request_body=operations.PostEIngestEventsV2RequestBody(),
)

res = s.default.post_e_ingest_events_v2(req)

if res.post_e_ingest_events_v2_200_application_json_object is not None:
    # handle response
    pass
```


## Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:


```python
import test
from test.models import operations, shared

s = test.Test(
    security=shared.Security(
        bearer_auth="",
    ),
    server_url="http://{{endpoint}}"
)

req = operations.PostEIngestEventsV2Request(
    request_body=operations.PostEIngestEventsV2RequestBody(),
)

res = s.default.post_e_ingest_events_v2(req)

if res.post_e_ingest_events_v2_200_application_json_object is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
# Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.


For example, you could specify a header for every request that your sdk makes as follows:

```python
import test
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = test.Test(client: http_client)
```


<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
