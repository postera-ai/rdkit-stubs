from _typeshed import Incomplete
from rdkit.ML.Data import SplitData as SplitData
from rdkit.ML.DecTree import ID3 as ID3, randomtest as randomtest

def ChooseOptimalRoot(
    examples,
    trainExamples,
    testExamples,
    attrs,
    nPossibleVals,
    treeBuilder,
    nQuantBounds=...,
    **kwargs
): ...
def CrossValidate(tree, testExamples, appendExamples: int = ...): ...
def CrossValidationDriver(
    examples,
    attrs,
    nPossibleVals,
    holdOutFrac: float = ...,
    silent: int = ...,
    calcTotalError: int = ...,
    treeBuilder=...,
    lessGreedy: int = ...,
    startAt: Incomplete | None = ...,
    nQuantBounds=...,
    maxDepth: int = ...,
    **kwargs
): ...
def TestRun() -> None: ...
