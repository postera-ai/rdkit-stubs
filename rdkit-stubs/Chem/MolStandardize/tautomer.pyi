from .utils import memoized_property as memoized_property, pairwise as pairwise
from _typeshed import Incomplete
from rdkit import Chem as Chem
from rdkit.Chem.rdchem import (
    BondDir as BondDir,
    BondStereo as BondStereo,
    BondType as BondType,
)

log: Incomplete

class TautomerTransform:
    BONDMAP: Incomplete
    CHARGEMAP: Incomplete
    name: Incomplete
    tautomer_str: Incomplete
    bonds: Incomplete
    charges: Incomplete
    def __init__(self, name, smarts, bonds=..., charges=..., radicals=...) -> None: ...
    def tautomer(self): ...
    def __repr__(self): ...
    def __str__(self): ...

class TautomerScore:
    name: Incomplete
    smarts_str: Incomplete
    score: Incomplete
    def __init__(self, name, smarts, score) -> None: ...
    def smarts(self): ...
    def __repr__(self): ...
    def __str__(self): ...

TAUTOMER_TRANSFORMS: Incomplete
TAUTOMER_SCORES: Incomplete
MAX_TAUTOMERS: int

class TautomerCanonicalizer:
    transforms: Incomplete
    scores: Incomplete
    max_tautomers: Incomplete
    def __init__(self, transforms=..., scores=..., max_tautomers=...) -> None: ...
    def __call__(self, mol): ...
    def canonicalize(self, mol): ...
    def _enumerate_tautomers(self): ...

class TautomerEnumerator:
    transforms: Incomplete
    max_tautomers: Incomplete
    def __init__(self, transforms=..., max_tautomers=...) -> None: ...
    def __call__(self, mol): ...
    def enumerate(self, mol): ...
