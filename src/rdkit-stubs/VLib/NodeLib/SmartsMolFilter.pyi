from _typeshed import Incomplete
from rdkit import Chem as Chem
from rdkit.VLib.Filter import FilterNode as FilterNode

class SmartsFilter(FilterNode):
    def __init__(self, patterns=..., counts=..., **kwargs) -> None: ...
    _patterns: Incomplete
    def _initPatterns(self, patterns, counts) -> None: ...
    def filter(self, cmpd): ...

def _runDoctests(verbose: Incomplete | None = ...) -> None: ...