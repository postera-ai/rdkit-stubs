from _typeshed import Incomplete
from rdkit import Chem as Chem, RDConfig as RDConfig
from rdkit.Chem import rdMolDescriptors as rdMolDescriptors

_smartsPatterns: Incomplete
_patternOrder: Incomplete
defaultPatternFileName: Incomplete

def _ReadPatts(fileName): ...

_GetAtomContribs: Incomplete

def _pyGetAtomContribs(
    mol,
    patts: Incomplete | None = ...,
    order: Incomplete | None = ...,
    verbose: int = ...,
    force: int = ...,
): ...
def _Init() -> None: ...
def _pyMolLogP(
    inMol,
    patts: Incomplete | None = ...,
    order: Incomplete | None = ...,
    verbose: int = ...,
    addHs: int = ...,
): ...
def _pyMolMR(
    inMol,
    patts: Incomplete | None = ...,
    order: Incomplete | None = ...,
    verbose: int = ...,
    addHs: int = ...,
): ...

MolLogP: Incomplete
MolMR: Incomplete
