from _typeshed import Incomplete
from rdkit import Chem as Chem

reactionDefs: Incomplete
reactions: Incomplete

class RecapHierarchyNode:
    mol: Incomplete
    children: Incomplete
    parents: Incomplete
    smiles: Incomplete
    def __init__(self, mol) -> None: ...
    def GetAllChildren(self): ...
    def GetLeaves(self): ...
    def getUltimateParents(self): ...
    def _gacRecurse(self, res, terminalOnly: bool = ...) -> None: ...
    def __del__(self) -> None: ...

def RecapDecompose(
    mol,
    allNodes: Incomplete | None = ...,
    minFragmentSize: int = ...,
    onlyUseReactions: Incomplete | None = ...,
): ...
