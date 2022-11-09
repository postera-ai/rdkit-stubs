from _typeshed import Incomplete
from rdkit import Chem as Chem, RDConfig as RDConfig
from rdkit.Chem import rdMolDescriptors as rdMolDescriptors
from rdkit.Chem.rdMolDescriptors import (
    GetAtomPairFingerprint as GetAtomPairFingerprint,
    GetTopologicalTorsionFingerprint as GetTopologicalTorsionFingerprint,
)

numPathBits: Incomplete
_maxPathLen: Incomplete
numFpBits: Incomplete
fpLen: Incomplete

def _readPattyDefs(fname=...): ...

_pattyDefs: Incomplete

def AssignPattyTypes(mol, defns: Incomplete | None = ...): ...

typMap: Incomplete

def GetBPFingerprint(mol, fpfn=...): ...
def GetBTFingerprint(mol, fpfn=...): ...
def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
