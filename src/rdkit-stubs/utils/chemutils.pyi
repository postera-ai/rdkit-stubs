from _typeshed import Incomplete
from rdkit import RDConfig as RDConfig

_atomDbName: Incomplete

def GetAtomicData(
    atomDict,
    descriptorsDesired,
    dBase=...,
    table: str = ...,
    where: str = ...,
    user: str = ...,
    password: str = ...,
    includeElCounts: int = ...,
) -> None: ...
def SplitComposition(compStr): ...
def ConfigToNumElectrons(config, ignoreFullD: int = ..., ignoreFullF: int = ...): ...
