from _typeshed import Incomplete
from rdkit import Chem as Chem
from rdkit.VLib.Transform import TransformNode as TransformNode

class SmartsRemover(TransformNode):
    _wholeFragments: Incomplete
    def __init__(self, patterns=..., wholeFragments: int = ..., **kwargs) -> None: ...
    _patterns: Incomplete
    def _initPatterns(self, patterns) -> None: ...
    def transform(self, cmpd): ...

biggerTest: str
__test__: Incomplete

def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
