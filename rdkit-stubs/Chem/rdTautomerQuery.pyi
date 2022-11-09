from typing import Any



class TautomerQuery:
    def __init__(self, RDKit): ...
    @classmethod
    def GetModifiedAtoms(cls, RDKit) -> Any: ...
    @classmethod
    def GetModifiedBonds(cls, RDKit) -> Any: ...
    @classmethod
    def GetSubstructMatch(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetSubstructMatches(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetSubstructMatchesWithTautomers(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetTautomers(cls, RDKit) -> Any: ...
    @classmethod
    def GetTemplateMolecule(cls, RDKit) -> Any: ...
    @classmethod
    def IsSubstructOf(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def PatternFingerprintTemplate(cls, RDKit) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

def PatternFingerprintTautomerTarget(RDKit) -> Any: ...
