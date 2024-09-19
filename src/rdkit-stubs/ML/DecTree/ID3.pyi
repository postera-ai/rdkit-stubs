from _typeshed import Incomplete
from rdkit.ML.DecTree import DecTree as DecTree
from rdkit.ML.InfoTheory import entropy as entropy

def CalcTotalEntropy(examples, nPossibleVals): ...
def GenVarTable(examples, nPossibleVals, vars): ...
def ID3(
    examples,
    target,
    attrs,
    nPossibleVals,
    depth: int = ...,
    maxDepth: int = ...,
    **kwargs
): ...
def ID3Boot(
    examples,
    attrs,
    nPossibleVals,
    initialVar: Incomplete | None = ...,
    depth: int = ...,
    maxDepth: int = ...,
    **kwargs
): ...
