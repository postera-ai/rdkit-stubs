from _typeshed import Incomplete
from rdkit import Chem as Chem, RDConfig as RDConfig

class FGHierarchyNode:
    children: Incomplete
    name: str
    label: str
    pattern: Incomplete
    smarts: str
    rxnSmarts: str
    parent: Incomplete
    removalReaction: Incomplete
    def __init__(
        self,
        name,
        patt,
        smarts: str = ...,
        label: str = ...,
        rxnSmarts: str = ...,
        parent: Incomplete | None = ...,
    ) -> None: ...
    def __len__(self) -> int: ...

class FuncGroupFileParseError(ValueError): ...

groupDefns: Incomplete
hierarchy: Incomplete
lastData: Incomplete
lastFilename: Incomplete

def BuildFuncGroupHierarchy(
    fileNm: Incomplete | None = ..., data: Incomplete | None = ..., force: bool = ...
): ...
def _SetNodeBits(mol, node, res, idx): ...
def CreateMolFingerprint(mol, hierarchy): ...
