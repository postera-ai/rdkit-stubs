from _typeshed import Incomplete
from rdkit.VLib.Node import VLibNode as VLibNode

class TransformNode(VLibNode):
    _func: Incomplete
    def __init__(self, func: Incomplete | None = ..., **kwargs) -> None: ...
    def next(self): ...

def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
