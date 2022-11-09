from _typeshed import Incomplete
from rdkit import Chem as Chem

log: Incomplete
MAX_STRUCTURES: int

class ResonanceEnumerator:
    kekule_all: Incomplete
    allow_incomplete_octets: Incomplete
    unconstrained_cations: Incomplete
    unconstrained_anions: Incomplete
    allow_charge_separation: Incomplete
    max_structures: Incomplete
    def __init__(
        self,
        kekule_all: bool = ...,
        allow_incomplete_octets: bool = ...,
        unconstrained_cations: bool = ...,
        unconstrained_anions: bool = ...,
        allow_charge_separation: bool = ...,
        max_structures=...,
    ) -> None: ...
    def __call__(self, mol): ...
    def enumerate(self, mol): ...

def enumerate_resonance_smiles(smiles): ...
