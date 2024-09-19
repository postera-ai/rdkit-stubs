from _typeshed import Incomplete

class ChemdrawPanel:
    cdx: Incomplete
    offset: int
    label: Incomplete
    def __init__(
        self,
        parent: Incomplete | None = ...,
        name: str = ...,
        readOnly: int = ...,
        size=...,
    ) -> None: ...
    def pullData(self, fmt: str = ...): ...
    def setData(self, data, fmt: str = ...): ...
    def resizeEvent(self, evt) -> None: ...
    def __del__(self) -> None: ...
