from _typeshed import Incomplete
from rdkit import rdBase as rdBase
from rdkit.DataStructs import cDataStructs as cDataStructs

similarityFunctions: Incomplete

def FingerprintSimilarity(fp1, fp2, metric=...): ...
def FoldToTargetDensity(fp, density: float = ..., minLength: int = ...): ...
