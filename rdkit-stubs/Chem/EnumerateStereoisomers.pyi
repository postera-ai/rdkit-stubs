from _typeshed import Incomplete
from collections.abc import Generator
from rdkit import Chem as Chem
from rdkit.Chem.rdDistGeom import EmbedMolecule as EmbedMolecule

class StereoEnumerationOptions:
    __slots__: Incomplete
    tryEmbedding: Incomplete
    onlyUnassigned: Incomplete
    onlyStereoGroups: Incomplete
    maxIsomers: Incomplete
    rand: Incomplete
    unique: Incomplete
    def __init__(
        self,
        tryEmbedding: bool = ...,
        onlyUnassigned: bool = ...,
        maxIsomers: int = ...,
        rand: Incomplete | None = ...,
        unique: bool = ...,
        onlyStereoGroups: bool = ...,
    ) -> None: ...

class _BondFlipper:
    bond: Incomplete
    def __init__(self, bond) -> None: ...
    def flip(self, flag) -> None: ...

class _AtomFlipper:
    atom: Incomplete
    def __init__(self, atom) -> None: ...
    def flip(self, flag) -> None: ...

class _StereoGroupFlipper:
    _original_parities: Incomplete
    def __init__(self, group) -> None: ...
    def flip(self, flag) -> None: ...

def _getFlippers(mol, options): ...

class _RangeBitsGenerator:
    nCenters: Incomplete
    def __init__(self, nCenters) -> None: ...
    def __iter__(self): ...

class _UniqueRandomBitsGenerator:
    nCenters: Incomplete
    maxIsomers: Incomplete
    rand: Incomplete
    already_seen: Incomplete
    def __init__(self, nCenters, maxIsomers, rand) -> None: ...
    def __iter__(self): ...

def GetStereoisomerCount(m, options=...): ...
def EnumerateStereoisomers(
    m, options=..., verbose: bool = ...
) -> Generator[Incomplete, None, None]: ...
