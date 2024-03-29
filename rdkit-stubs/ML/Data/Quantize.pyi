from _typeshed import Incomplete
from rdkit.ML.Data import cQuantize as cQuantize
from rdkit.ML.InfoTheory import entropy as entropy

hascQuantize: int
_float_tol: float

def feq(v1, v2, tol=...): ...
def FindVarQuantBound(vals, results, nPossibleRes): ...
def _GenVarTable(vals, cuts, starts, results, nPossibleRes): ...
def _PyRecurseOnBounds(
    vals, cuts, which, starts, results, nPossibleRes, varTable: Incomplete | None = ...
): ...
def _NewPyRecurseOnBounds(
    vals, cuts, which, starts, results, nPossibleRes, varTable: Incomplete | None = ...
): ...
def _NewPyFindStartPoints(sortVals, sortResults, nData): ...
def FindVarMultQuantBounds(vals, nBounds, results, nPossibleRes): ...

_RecurseOnBounds: Incomplete
_FindStartPoints: Incomplete
_RecurseOnBounds = _NewPyRecurseOnBounds
_FindStartPoints = _NewPyFindStartPoints
