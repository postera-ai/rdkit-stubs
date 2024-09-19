from _typeshed import Incomplete
from rdkit import Chem as Chem
from rdkit.VLib.Output import OutputNode as BaseOutputNode

class OutputNode(BaseOutputNode):
    _dest: Incomplete
    _idField: Incomplete
    _delim: Incomplete
    _nDumped: int
    def __init__(
        self,
        dest: Incomplete | None = ...,
        delim: str = ...,
        idField: Incomplete | None = ...,
        **kwargs
    ) -> None: ...
    def reset(self) -> None: ...
    def smilesOut(self, mol): ...

def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
