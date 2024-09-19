from _typeshed import Incomplete
from rdkit import DataStructs as DataStructs
from rdkit.Dbase import DbModule as DbModule
from rdkit.ML import CompositeRun as CompositeRun, ScreenComposite as ScreenComposite
from rdkit.ML.Composite import Composite as Composite
from rdkit.ML.Data import DataUtils as DataUtils, SplitData as SplitData
from rdkit.utils import listutils as listutils

_runDetails: Incomplete
__VERSION_STRING: str
_verbose: int

def message(msg) -> None: ...
def testall(composite, examples, badExamples=...): ...
def GetCommandLine(details): ...
def RunOnData(
    details,
    data,
    progressCallback: Incomplete | None = ...,
    saveIt: int = ...,
    setDescNames: int = ...,
): ...
def RunIt(
    details,
    progressCallback: Incomplete | None = ...,
    saveIt: int = ...,
    setDescNames: int = ...,
): ...
def ShowVersion(includeArgs: int = ...) -> None: ...
def Usage() -> None: ...
def SetDefaults(runDetails: Incomplete | None = ...): ...
def ParseArgs(runDetails) -> None: ...
