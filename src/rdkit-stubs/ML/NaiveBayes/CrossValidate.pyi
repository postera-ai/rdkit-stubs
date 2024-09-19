from _typeshed import Incomplete
from rdkit.ML.Data import SplitData as SplitData
from rdkit.ML.NaiveBayes.ClassificationModel import (
    NaiveBayesClassifier as NaiveBayesClassifier,
)

def makeNBClassificationModel(
    trainExamples,
    attrs,
    nPossibleValues,
    nQuantBounds,
    mEstimateVal=...,
    useSigs: bool = ...,
    ensemble: Incomplete | None = ...,
    useCMIM: int = ...,
    **kwargs
): ...
def CrossValidate(NBmodel, testExamples, appendExamples: int = ...): ...
def CrossValidationDriver(
    examples,
    attrs,
    nPossibleValues,
    nQuantBounds,
    mEstimateVal: float = ...,
    holdOutFrac: float = ...,
    modelBuilder=...,
    silent: int = ...,
    calcTotalError: int = ...,
    **kwargs
): ...
