from _typeshed import Incomplete
from rdkit.Chem import rdMolDescriptors as rdMolDescriptors
from rdkit.Chem.AtomPairs import Utils as Utils
from rdkit.Chem.rdMolDescriptors import (
    GetHashedTopologicalTorsionFingerprint as GetHashedTopologicalTorsionFingerprint,
    GetTopologicalTorsionFingerprint as GetTopologicalTorsionFingerprint,
)

GetTopologicalTorsionFingerprintAsIntVect: Incomplete

def pyScorePath(mol, path, size, atomCodes: Incomplete | None = ...): ...
def ExplainPathScore(score, size: int = ...): ...
def GetTopologicalTorsionFingerprintAsIds(mol, targetSize: int = ...): ...
def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
