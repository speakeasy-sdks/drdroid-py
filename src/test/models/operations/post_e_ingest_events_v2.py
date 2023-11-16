"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Dict, List, Optional


@dataclasses.dataclass
class PostEIngestEventsV2RequestBody:
    pass


@dataclasses.dataclass
class PostEIngestEventsV2Request:
    request_body: Optional[PostEIngestEventsV2RequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    x_request_org: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-REQUEST-ORG', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class PostEIngestEventsV2ResponseBody:
    r"""OK"""
    



@dataclasses.dataclass
class PostEIngestEventsV2Response:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]] = dataclasses.field()
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[PostEIngestEventsV2ResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    

