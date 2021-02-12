# generated by datamodel-codegen:
#   filename:  sample.json
#   timestamp: 2021-02-12T20:20:58+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class _Shards(BaseModel):
    total: int
    successful: int
    skipped: int
    failed: int


class Total(BaseModel):
    value: int
    relation: str


class Hits(BaseModel):
    total: Total
    max_score: Any
    hits: List


class Bucket(BaseModel):
    key_as_string: str
    key: int
    doc_count: int


class Timestamp(BaseModel):
    buckets: List[Bucket]


class Aggregations(BaseModel):
    timestamp: Optional[Timestamp] = None


class TheDonaldTimeSeries(BaseModel):
    created_key: str
    took: int
    timed_out: bool
    _shards: _Shards
    hits: Hits
    aggregations: Optional[Aggregations] = None