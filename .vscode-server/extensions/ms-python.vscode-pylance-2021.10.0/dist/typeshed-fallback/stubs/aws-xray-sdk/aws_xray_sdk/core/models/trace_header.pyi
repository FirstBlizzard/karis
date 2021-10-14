from typing import Any

log: Any
ROOT: str
PARENT: str
SAMPLE: str
SELF: str
HEADER_DELIMITER: str

class TraceHeader:
    def __init__(
        self, root: str | None = ..., parent: str | None = ..., sampled: bool | None = ..., data: dict[str, Any] | None = ...
    ) -> None: ...
    @classmethod
    def from_header_str(cls, header): ...
    def to_header_str(self): ...
    @property
    def root(self): ...
    @property
    def parent(self): ...
    @property
    def sampled(self): ...
    @property
    def data(self): ...
