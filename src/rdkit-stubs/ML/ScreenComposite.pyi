from _typeshed import Incomplete
from rdkit import DataStructs as DataStructs
from rdkit.Dbase import DbModule as DbModule
from rdkit.Dbase.DbConnection import DbConnect as DbConnect
from rdkit.ML import CompositeRun as CompositeRun
from rdkit.ML.Data import DataUtils as DataUtils, SplitData as SplitData

hasPil: int
_details: Incomplete
__VERSION_STRING: str

def message(msg, noRet: int = ...) -> None: ...
def error(msg) -> None: ...
def CalcEnrichment(mat, tgt: int = ...): ...
def CollectResults(
    indices,
    dataSet,
    composite,
    callback: Incomplete | None = ...,
    appendExamples: int = ...,
    errorEstimate: int = ...,
): ...
def DetailedScreen(
    indices,
    data,
    composite,
    threshold: int = ...,
    screenResults: Incomplete | None = ...,
    goodVotes: Incomplete | None = ...,
    badVotes: Incomplete | None = ...,
    noVotes: Incomplete | None = ...,
    callback: Incomplete | None = ...,
    appendExamples: int = ...,
    errorEstimate: int = ...,
) -> None: ...
def ShowVoteResults(
    indices,
    data,
    composite,
    nResultCodes,
    threshold,
    verbose: int = ...,
    screenResults: Incomplete | None = ...,
    callback: Incomplete | None = ...,
    appendExamples: int = ...,
    goodVotes: Incomplete | None = ...,
    badVotes: Incomplete | None = ...,
    noVotes: Incomplete | None = ...,
    errorEstimate: int = ...,
): ...
def ScreenIt(
    composite,
    indices,
    data,
    partialVote: int = ...,
    voteTol: float = ...,
    verbose: int = ...,
    screenResults: Incomplete | None = ...,
    goodVotes: Incomplete | None = ...,
    badVotes: Incomplete | None = ...,
    noVotes: Incomplete | None = ...,
): ...
def _processVoteList(votes, data) -> None: ...
def PrepareDataFromDetails(model, details, data, verbose: int = ...): ...
def ScreenFromDetails(
    models,
    details,
    callback: Incomplete | None = ...,
    setup: Incomplete | None = ...,
    appendExamples: int = ...,
    goodVotes: Incomplete | None = ...,
    badVotes: Incomplete | None = ...,
    noVotes: Incomplete | None = ...,
    data: Incomplete | None = ...,
    enrichments: Incomplete | None = ...,
): ...
def GetScreenImage(nGood, nBad, nRej, size: Incomplete | None = ...): ...
def ScreenToHtml(
    nGood,
    nBad,
    nRej,
    avgGood,
    avgBad,
    avgSkip,
    voteTable,
    imgDir: str = ...,
    fullPage: int = ...,
    skipImg: int = ...,
    includeDefs: int = ...,
): ...
def MakePredPlot(
    details,
    indices,
    data,
    goodVotes,
    badVotes,
    nRes,
    idCol: int = ...,
    verbose: int = ...,
) -> None: ...
def Go(details) -> None: ...
def SetDefaults(details: Incomplete | None = ...): ...
def Usage() -> None: ...
def ShowVersion(includeArgs: int = ...) -> None: ...
def ParseArgs(details): ...
