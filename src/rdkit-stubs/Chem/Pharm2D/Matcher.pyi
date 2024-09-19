from _typeshed import Incomplete
from rdkit import Chem as Chem
from rdkit.Chem.Pharm2D import Utils as Utils

class MatchError(Exception): ...

_verbose: int

def GetAtomsMatchingBit(
    sigFactory,
    bitIdx,
    mol,
    dMat: Incomplete | None = ...,
    justOne: int = ...,
    matchingAtoms: Incomplete | None = ...,
): ...
def _exampleCode() -> None: ...
