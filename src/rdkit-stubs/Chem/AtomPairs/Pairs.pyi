from _typeshed import Incomplete
from rdkit import DataStructs as DataStructs
from rdkit.Chem import rdMolDescriptors as rdMolDescriptors
from rdkit.Chem.AtomPairs import Utils as Utils
from rdkit.Chem.rdMolDescriptors import (
    GetAtomPairFingerprint as GetAtomPairFingerprint,
    GetHashedAtomPairFingerprint as GetHashedAtomPairFingerprint,
)

GetAtomPairFingerprintAsIntVect: Incomplete
numPathBits: Incomplete
_maxPathLen: Incomplete
numFpBits: Incomplete
fpLen: Incomplete

def pyScorePair(
    at1, at2, dist, atomCodes: Incomplete | None = ..., includeChirality: bool = ...
): ...
def ExplainPairScore(score, includeChirality: bool = ...): ...
def GetAtomPairFingerprintAsBitVect(mol): ...
def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
