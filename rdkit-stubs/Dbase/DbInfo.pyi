from _typeshed import Incomplete
from rdkit import RDConfig as RDConfig
from rdkit.Dbase import DbModule as DbModule

sqlTextTypes: Incomplete
sqlIntTypes: Incomplete
sqlFloatTypes: Incomplete
sqlBinTypes: Incomplete

def GetDbNames(
    user: str = ...,
    password: str = ...,
    dirName: str = ...,
    dBase: str = ...,
    cn: Incomplete | None = ...,
): ...
def GetTableNames(
    dBase,
    user: str = ...,
    password: str = ...,
    includeViews: int = ...,
    cn: Incomplete | None = ...,
): ...
def GetColumnInfoFromCursor(cursor): ...
def GetColumnNamesAndTypes(
    dBase,
    table,
    user: str = ...,
    password: str = ...,
    join: str = ...,
    what: str = ...,
    cn: Incomplete | None = ...,
): ...
def GetColumnNames(
    dBase,
    table,
    user: str = ...,
    password: str = ...,
    join: str = ...,
    what: str = ...,
    cn: Incomplete | None = ...,
): ...
