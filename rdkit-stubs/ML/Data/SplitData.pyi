from _typeshed import Incomplete
from rdkit import RDRandom as RDRandom

SeqTypes: Incomplete

def SplitIndices(
    nPts, frac, silent: int = ..., legacy: int = ..., replacement: int = ...
): ...
def SplitDataSet(data, frac, silent: int = ...): ...
def SplitDbData(
    conn,
    fracs,
    table: str = ...,
    fields: str = ...,
    where: str = ...,
    join: str = ...,
    labelCol: str = ...,
    useActs: int = ...,
    nActs: int = ...,
    actCol: str = ...,
    actBounds=...,
    silent: int = ...,
): ...
def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
