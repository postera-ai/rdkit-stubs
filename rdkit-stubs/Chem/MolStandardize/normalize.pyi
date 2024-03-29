from .utils import memoized_property as memoized_property
from _typeshed import Incomplete
from rdkit import Chem as Chem
from rdkit.Chem import AllChem as AllChem

log: Incomplete

class Normalization:
    name: Incomplete
    transform_str: Incomplete
    def __init__(self, name, transform) -> None: ...
    def transform(self): ...
    def __repr__(self): ...
    def __str__(self): ...

NORMALIZATIONS: Incomplete
MAX_RESTARTS: int

class Normalizer:
    normalizations: Incomplete
    max_restarts: Incomplete
    def __init__(self, normalizations=..., max_restarts=...) -> None: ...
    def __call__(self, mol): ...
    def normalize(self, mol): ...
    def _normalize_fragment(self, mol): ...
    def _apply_transform(self, mol, rule): ...
