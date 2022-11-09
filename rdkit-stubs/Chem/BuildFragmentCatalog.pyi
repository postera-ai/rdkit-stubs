from _typeshed import Incomplete
from rdkit import RDConfig as RDConfig
from rdkit.Chem import FragmentCatalog as FragmentCatalog
from rdkit.Dbase.DbConnection import DbConnect as DbConnect
from rdkit.ML import InfoTheory as InfoTheory

def message(msg, dest=...) -> None: ...
def BuildCatalog(
    suppl,
    maxPts: int = ...,
    groupFileName: Incomplete | None = ...,
    minPath: int = ...,
    maxPath: int = ...,
    reportFreq: int = ...,
): ...
def ScoreMolecules(
    suppl,
    catalog,
    maxPts: int = ...,
    actName: str = ...,
    acts: Incomplete | None = ...,
    nActs: int = ...,
    reportFreq: int = ...,
): ...
def ScoreFromLists(
    bitLists,
    suppl,
    catalog,
    maxPts: int = ...,
    actName: str = ...,
    acts: Incomplete | None = ...,
    nActs: int = ...,
    reportFreq: int = ...,
): ...
def CalcGains(
    suppl,
    catalog,
    topN: int = ...,
    actName: str = ...,
    acts: Incomplete | None = ...,
    nActs: int = ...,
    reportFreq: int = ...,
    biasList: Incomplete | None = ...,
    collectFps: int = ...,
): ...
def CalcGainsFromFps(
    suppl,
    fps,
    topN: int = ...,
    actName: str = ...,
    acts: Incomplete | None = ...,
    nActs: int = ...,
    reportFreq: int = ...,
    biasList: Incomplete | None = ...,
): ...
def OutputGainsData(outF, gains, cat, nActs: int = ...) -> None: ...
def ProcessGainsData(inF, delim: str = ..., idCol: int = ..., gainCol: int = ...): ...
def ShowDetails(
    catalog,
    gains,
    nToDo: int = ...,
    outF=...,
    idCol: int = ...,
    gainCol: int = ...,
    outDelim: str = ...,
) -> None: ...
def SupplierFromDetails(details): ...
def Usage() -> None: ...

class RunDetails:
    numMols: int
    doBuild: int
    doSigs: int
    doScore: int
    doGains: int
    doDetails: int
    catalogName: Incomplete
    onBitsName: Incomplete
    scoresName: Incomplete
    gainsName: Incomplete
    dbName: str
    tableName: Incomplete
    detailsName: Incomplete
    inFileName: Incomplete
    fpName: Incomplete
    minPath: int
    maxPath: int
    smiCol: int
    actCol: int
    nameCol: int
    hasTitle: int
    nActs: int
    nBits: int
    delim: str
    biasList: Incomplete
    topN: int

def ParseArgs(details) -> None: ...
