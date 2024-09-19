from rdkit import DataStructs as DataStructs
from rdkit.Chem.Fingerprints import (
    FingerprintMols as FingerprintMols,
    MolSimilarity as MolSimilarity,
)
from rdkit.ML.Cluster import Murtagh as Murtagh

message = FingerprintMols.message
error = FingerprintMols.error

def GetDistanceMatrix(data, metric, isSimilarity: int = ...): ...
def ClusterPoints(
    data,
    metric,
    algorithmId,
    haveLabels: bool = ...,
    haveActs: bool = ...,
    returnDistances: bool = ...,
): ...
def ClusterFromDetails(details): ...

_usageDoc: str
