from rdkit.Chem.rdfiltercatalog import *
from _typeshed import Incomplete
from rdkit import Chem as Chem

class FilterMatcher(PythonFilterMatcher):
    name: Incomplete
    def __init__(self, name: str = ...) -> None: ...
    def GetMatches(self, mol, matchVect): ...
    def GetName(self): ...