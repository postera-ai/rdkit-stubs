from . import ActFuncs as ActFuncs
from _typeshed import Incomplete

class NetNode:
    def Eval(self, valVect): ...
    inputNodes: Incomplete
    def SetInputs(self, inputNodes) -> None: ...
    def GetInputs(self): ...
    weights: Incomplete
    def SetWeights(self, weights) -> None: ...
    def GetWeights(self): ...
    nodeIndex: Incomplete
    nodeList: Incomplete
    actFunc: Incomplete
    def __init__(
        self,
        nodeIndex,
        nodeList,
        inputNodes: Incomplete | None = ...,
        weights: Incomplete | None = ...,
        actFunc=...,
        actFuncParms=...,
    ) -> None: ...
