from .charge import (
    ACID_BASE_PAIRS as ACID_BASE_PAIRS,
    CHARGE_CORRECTIONS as CHARGE_CORRECTIONS,
    Reionizer as Reionizer,
    Uncharger as Uncharger,
)
from .fragment import (
    FragmentRemover as FragmentRemover,
    LargestFragmentChooser as LargestFragmentChooser,
    PREFER_ORGANIC as PREFER_ORGANIC,
)
from .metal import MetalDisconnector as MetalDisconnector
from .normalize import (
    MAX_RESTARTS as MAX_RESTARTS,
    NORMALIZATIONS as NORMALIZATIONS,
    Normalizer as Normalizer,
)
from .tautomer import (
    MAX_TAUTOMERS as MAX_TAUTOMERS,
    TAUTOMER_SCORES as TAUTOMER_SCORES,
    TAUTOMER_TRANSFORMS as TAUTOMER_TRANSFORMS,
    TautomerCanonicalizer as TautomerCanonicalizer,
    TautomerEnumerator as TautomerEnumerator,
)
from .utils import memoized_property as memoized_property
from _typeshed import Incomplete
from rdkit import Chem as Chem

log: Incomplete

class Standardizer:
    normalizations: Incomplete
    acid_base_pairs: Incomplete
    charge_corrections: Incomplete
    tautomer_transforms: Incomplete
    tautomer_scores: Incomplete
    max_restarts: Incomplete
    max_tautomers: Incomplete
    prefer_organic: Incomplete
    def __init__(
        self,
        normalizations=...,
        acid_base_pairs=...,
        charge_corrections=...,
        tautomer_transforms=...,
        tautomer_scores=...,
        max_restarts=...,
        max_tautomers=...,
        prefer_organic=...,
    ) -> None: ...
    def __call__(self, mol): ...
    def standardize(self, mol): ...
    def tautomer_parent(self, mol, skip_standardize: bool = ...): ...
    def fragment_parent(self, mol, skip_standardize: bool = ...): ...
    def stereo_parent(self, mol, skip_standardize: bool = ...): ...
    def isotope_parent(self, mol, skip_standardize: bool = ...): ...
    def charge_parent(self, mol, skip_standardize: bool = ...): ...
    def super_parent(self, mol, skip_standardize: bool = ...): ...
    def standardize_with_parents(self, mol): ...
    def disconnect_metals(self): ...
    def normalize(self): ...
    def reionize(self): ...
    def uncharge(self): ...
    def remove_fragments(self): ...
    def largest_fragment(self): ...
    def enumerate_tautomers(self): ...
    def canonicalize_tautomer(self): ...

def standardize_smiles(smiles): ...
def enumerate_tautomers_smiles(smiles): ...
def canonicalize_tautomer_smiles(smiles): ...
