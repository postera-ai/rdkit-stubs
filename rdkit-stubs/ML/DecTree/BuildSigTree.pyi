from _typeshed import Incomplete
from rdkit.DataStructs.VectCollection import VectCollection as VectCollection
from rdkit.ML import InfoTheory as InfoTheory
from rdkit.ML.DecTree import SigTree as SigTree

def _GenerateRandomEnsemble(nToInclude, nBits): ...
def BuildSigTree(
    examples,
    nPossibleRes,
    ensemble: Incomplete | None = ...,
    random: int = ...,
    metric=...,
    biasList=...,
    depth: int = ...,
    maxDepth: int = ...,
    useCMIM: int = ...,
    allowCollections: bool = ...,
    verbose: int = ...,
    **kwargs
): ...
def SigTreeBuilder(
    examples,
    attrs,
    nPossibleVals,
    initialVar: Incomplete | None = ...,
    ensemble: Incomplete | None = ...,
    randomDescriptors: int = ...,
    **kwargs
): ...
