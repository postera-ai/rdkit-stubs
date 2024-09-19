from _typeshed import Incomplete
from rdkit.Dbase.DbConnection import DbConnect as DbConnect
from rdkit.ML import (
    BuildComposite as BuildComposite,
    CompositeRun as CompositeRun,
    ScreenComposite as ScreenComposite,
)
from rdkit.ML.Composite import AdjustComposite as AdjustComposite
from rdkit.ML.Data import DataUtils as DataUtils, SplitData as SplitData

_runDetails: Incomplete
__VERSION_STRING: str
_verbose: int

def message(msg) -> None: ...
def GrowIt(
    details,
    composite,
    progressCallback: Incomplete | None = ...,
    saveIt: int = ...,
    setDescNames: int = ...,
    data: Incomplete | None = ...,
): ...
def GetComposites(details): ...
def BalanceComposite(
    details, composite, data1: Incomplete | None = ..., data2: Incomplete | None = ...
): ...
def ShowVersion(includeArgs: int = ...) -> None: ...
def Usage() -> None: ...
def SetDefaults(runDetails: Incomplete | None = ...): ...
def ParseArgs(runDetails) -> None: ...
