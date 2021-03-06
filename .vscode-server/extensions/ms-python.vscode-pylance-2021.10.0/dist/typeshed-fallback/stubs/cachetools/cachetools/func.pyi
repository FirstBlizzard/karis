from _typeshed import IdentityFunction
from typing import Callable, Sequence, TypeVar

_T = TypeVar("_T")

def fifo_cache(maxsize: float = ..., typed: bool = ...) -> IdentityFunction: ...
def lfu_cache(maxsize: float = ..., typed: bool = ...) -> IdentityFunction: ...
def lru_cache(maxsize: float = ..., typed: bool = ...) -> IdentityFunction: ...
def mru_cache(maxsize: float = ..., typed: bool = ...) -> IdentityFunction: ...
def rr_cache(maxsize: float = ..., choice: Callable[[Sequence[_T]], _T] | None = ..., typed: bool = ...) -> IdentityFunction: ...
def ttl_cache(
    maxsize: float = ..., ttl: float = ..., timer: Callable[[], float] = ..., typed: bool = ...
) -> IdentityFunction: ...
