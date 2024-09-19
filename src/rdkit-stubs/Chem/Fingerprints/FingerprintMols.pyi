from _typeshed import Incomplete
from rdkit import Chem as Chem, DataStructs as DataStructs
from rdkit.Chem import MACCSkeys as MACCSkeys
from rdkit.ML.Cluster import Murtagh as Murtagh

def error(msg) -> None: ...
def message(msg) -> None: ...
def GetRDKFingerprint(mol): ...
def FoldFingerprintToTargetDensity(fp, **fpArgs): ...
def FingerprintMol(mol, fingerprinter=..., **fpArgs): ...
def FingerprintsFromSmiles(
    dataSource,
    idCol,
    smiCol,
    fingerprinter=...,
    reportFreq: int = ...,
    maxMols: int = ...,
    **fpArgs
): ...
def FingerprintsFromMols(
    mols, fingerprinter=..., reportFreq: int = ..., maxMols: int = ..., **fpArgs
): ...
def FingerprintsFromPickles(
    dataSource,
    idCol,
    pklCol,
    fingerprinter=...,
    reportFreq: int = ...,
    maxMols: int = ...,
    **fpArgs
): ...
def FingerprintsFromDetails(details, reportFreq: int = ...): ...

class FingerprinterDetails:
    def __init__(self) -> None: ...
    fingerprinter: Incomplete
    fpColName: str
    idName: str
    dbName: str
    outDbName: str
    tableName: str
    minSize: int
    fpSize: int
    tgtDensity: float
    minPath: int
    maxPath: int
    discrimHash: int
    useHs: int
    useValence: int
    bitsPerHash: int
    smilesName: str
    maxMols: int
    outFileName: str
    outTableName: str
    inFileName: str
    replaceTable: bool
    molPklName: str
    useSmiles: bool
    useSD: bool
    def _fingerprinterInit(self) -> None: ...
    metric: Incomplete
    doScreen: str
    topN: int
    screenThresh: float
    doThreshold: int
    smilesTableName: str
    probeSmiles: str
    probeMol: Incomplete
    noPickle: int
    def _screenerInit(self) -> None: ...
    clusterAlgo: Incomplete
    actTableName: str
    actName: str
    def _clusterInit(self) -> None: ...
    def GetMetricName(self): ...
    def SetMetricFromName(self, name) -> None: ...

def Usage() -> None: ...

_usageDoc: str

def ParseArgs(details: Incomplete | None = ...): ...
