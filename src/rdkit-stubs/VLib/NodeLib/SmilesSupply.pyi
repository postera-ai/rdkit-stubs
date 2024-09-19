from _typeshed import Incomplete
from rdkit import Chem as Chem
from rdkit.VLib.Supply import SupplyNode as SupplyNode

class SmilesSupplyNode(SupplyNode):
    _fileName: Incomplete
    _supplier: Incomplete
    def __init__(
        self,
        fileName,
        delim: str = ...,
        nameColumn: int = ...,
        smilesColumn: int = ...,
        titleLine: int = ...,
        **kwargs
    ) -> None: ...
    def reset(self) -> None: ...
    def next(self): ...

def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
