from _typeshed import Incomplete
from rdkit.ML.DecTree import DecTree as DecTree, Tree as Tree

class QuantTreeNode(DecTree.DecTreeNode):
    qBounds: Incomplete
    nBounds: int
    def __init__(self, *args, **kwargs) -> None: ...
    def ClassifyExample(self, example, appendExamples: int = ...): ...
    def SetQuantBounds(self, qBounds) -> None: ...
    def GetQuantBounds(self): ...
    def __cmp__(self, other): ...
    def __lt__(self, other): ...
    def __eq__(self, other): ...
    def __str__(self): ...
