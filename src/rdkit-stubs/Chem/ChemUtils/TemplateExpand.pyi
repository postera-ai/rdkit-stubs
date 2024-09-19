from _typeshed import Incomplete
from collections.abc import Generator
from rdkit import Chem as Chem
from rdkit.Chem import AllChem as AllChem, Crippen as Crippen
from rdkit.Chem.ChemUtils.AlignDepict import AlignDepict as AlignDepict

logger: Incomplete
_version: str
_greet: Incomplete
_usage: str

def Usage() -> None: ...

nDumped: int

def _exploder(
    mol,
    depth,
    sidechains,
    core,
    chainIndices,
    autoNames: bool = ...,
    templateName: str = ...,
    resetCounter: bool = ...,
    do3D: bool = ...,
    useTethers: bool = ...,
) -> Generator[Incomplete, None, None]: ...
def Explode(
    template,
    sidechains,
    outF,
    autoNames: bool = ...,
    do3D: bool = ...,
    useTethers: bool = ...,
) -> None: ...
def MoveDummyNeighborsToBeginning(mol, useAll: bool = ...): ...
def ConstructSidechains(
    suppl, sma: Incomplete | None = ..., replace: bool = ..., useAll: bool = ...
): ...
