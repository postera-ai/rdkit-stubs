from _typeshed import Incomplete

class TopNContainer:
    _size: Incomplete
    best: Incomplete
    extras: Incomplete
    def __init__(self, size, mostNeg=...) -> None: ...
    def Insert(self, val, extra: Incomplete | None = ...) -> None: ...
    def GetPts(self): ...
    def GetExtras(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, which): ...
    def reverse(self) -> None: ...

def _exampleCode() -> None: ...
