from _typeshed import Incomplete
from rdkit.ML.Data import Quantize as Quantize
from rdkit.ML.DecTree import ID3 as ID3, QuantTree as QuantTree
from rdkit.ML.InfoTheory import entropy as entropy

def FindBest(
    resCodes,
    examples,
    nBoundsPerVar,
    nPossibleRes,
    nPossibleVals,
    attrs,
    exIndices: Incomplete | None = ...,
    **kwargs
): ...
def BuildQuantTree(
    examples,
    target,
    attrs,
    nPossibleVals,
    nBoundsPerVar,
    depth: int = ...,
    maxDepth: int = ...,
    exIndices: Incomplete | None = ...,
    **kwargs
): ...
def QuantTreeBoot(
    examples,
    attrs,
    nPossibleVals,
    nBoundsPerVar,
    initialVar: Incomplete | None = ...,
    maxDepth: int = ...,
    **kwargs
): ...
def TestTree() -> None: ...
def TestQuantTree() -> None: ...
def TestQuantTree2() -> None: ...
