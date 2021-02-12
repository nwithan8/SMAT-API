# generated by datamodel-codegen:
#   filename:  sample.json
#   timestamp: 2021-02-12T19:52:55+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class _Shards(BaseModel):
    total: int
    successful: int
    skipped: int
    failed: int


class Total(BaseModel):
    value: int
    relation: str


class _Source(BaseModel):
    board: str
    chan: int
    id: str
    urls: List[str]
    v: float
    bumplocked: str
    com: str
    cyclical: str
    htmlparsedcom: str
    lastmodified: int
    locked: int
    name: str
    no: int
    resto: int
    sticky: int
    time: int
    txlink: bool
    ext: Optional[str] = None
    filename: Optional[str] = None
    fpath: Optional[int] = None
    fsize: Optional[int] = None
    h: Optional[int] = None
    md5: Optional[str] = None
    spoiler: Optional[int] = None
    tim: Optional[str] = None
    tnh: Optional[int] = None
    tnw: Optional[int] = None
    w: Optional[int] = None


class Hit(BaseModel):
    _index: str
    _type: str
    _id: str
    _score: float
    _source: _Source


class Hits(BaseModel):
    total: Total
    max_score: float
    hits: List[Hit]


class EightKunContent(BaseModel):
    created_key: str
    content_key: str
    took: int
    timed_out: bool
    _shards: _Shards
    hits: Hits