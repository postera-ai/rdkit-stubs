from _typeshed import Incomplete
from rdkit import Chem as Chem
from rdkit.Chem.Suppliers.MolSupplier import MolSupplier as MolSupplier

def warning(msg, dest=...) -> None: ...

class DbMolSupplier(MolSupplier):
    _data: Incomplete
    _colNames: Incomplete
    molCol: int
    transformFunc: Incomplete
    nameCol: Incomplete
    molFmt: Incomplete
    _numProcessed: int
    def __init__(
        self,
        dbResults,
        molColumnFormats=...,
        nameCol: str = ...,
        transformFunc: Incomplete | None = ...,
        **kwargs,
    ) -> None: ...
    def GetColumnNames(self): ...
    def _BuildMol(self, data): ...

class ForwardDbMolSupplier(DbMolSupplier):
    def __init__(self, dbResults, **kwargs) -> None: ...
    _dataIter: Incomplete
    def Reset(self) -> None: ...
    def NextMol(self): ...

class RandomAccessDbMolSupplier(DbMolSupplier):
    _pos: int
    def __init__(self, dbResults, **kwargs) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, idx): ...
    def Reset(self) -> None: ...
    def NextMol(self): ...