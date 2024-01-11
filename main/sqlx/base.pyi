import io
from .typed import column_t, data_t
from sqlalchemy.sql.visitors import TraversibleType
from typing import Any, Optional

class DCaptureSysOut:
    __buffer__: io.TextIOWrapper
    __stdout__: io.TextIOWrapper
    def __init__(self, *args, **kwargs) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def capture(self) -> Optional[str]: ...

class DRow(dict):
    __tablename__: str
    def __init__(self, table: str, data: data_t = ..., *args, **kwargs) -> None: ...
    def normalize(self) -> None: ...
    def __getattr__(self, key: str) -> Any: ...
    def __setattr__(self, key: str, value: Any): ...
    def __getitem__(self, key: column_t) -> Any: ...
    def __setitem__(self, key: column_t, value: Any): ...

class DType:
    typed: TraversibleType
    def __init__(self, typed: TraversibleType, **kwargs) -> None: ...
    def __str__(self): ...
    def __repr__(self): ...
    def alias(self) -> TraversibleType: ...
