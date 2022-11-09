from rdkit.ML.Data import SplitData as SplitData
from rdkit.ML.KNN import DistFunctions as DistFunctions
from rdkit.ML.KNN.KNNClassificationModel import (
    KNNClassificationModel as KNNClassificationModel,
)
from rdkit.ML.KNN.KNNRegressionModel import KNNRegressionModel as KNNRegressionModel

def makeClassificationModel(numNeigh, attrs, distFunc): ...
def makeRegressionModel(numNeigh, attrs, distFunc): ...
def CrossValidate(knnMod, testExamples, appendExamples: int = ...): ...
def CrossValidationDriver(
    examples,
    attrs,
    nPossibleValues,
    numNeigh,
    modelBuilder=...,
    distFunc=...,
    holdOutFrac: float = ...,
    silent: int = ...,
    calcTotalError: int = ...,
    **kwargs
): ...
