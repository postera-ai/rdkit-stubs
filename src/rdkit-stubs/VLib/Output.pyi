from _typeshed import Incomplete
from rdkit.VLib.Node import VLibNode as VLibNode

class OutputNode(VLibNode):
    _dest: Incomplete
    _func: Incomplete
    def __init__(
        self, dest: Incomplete | None = ..., strFunc: Incomplete | None = ..., **kwargs
    ) -> None: ...
    def next(self): ...

def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
