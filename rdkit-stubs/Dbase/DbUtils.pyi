from _typeshed import Incomplete
from rdkit.Dbase import DbInfo as DbInfo, DbModule as DbModule
from rdkit.Dbase.DbResultSet import (
    DbResultSet as DbResultSet,
    RandomAccessDbResultSet as RandomAccessDbResultSet,
)

def _take(fromL, what): ...
def GetColumns(
    dBase,
    table,
    fieldString,
    user: str = ...,
    password: str = ...,
    join: str = ...,
    cn: Incomplete | None = ...,
): ...
def GetData(
    dBase,
    table,
    fieldString: str = ...,
    whereString: str = ...,
    user: str = ...,
    password: str = ...,
    removeDups: int = ...,
    join: str = ...,
    forceList: int = ...,
    transform: Incomplete | None = ...,
    randomAccess: int = ...,
    extras: Incomplete | None = ...,
    cn: Incomplete | None = ...,
): ...
def DatabaseToText(
    dBase,
    table,
    fields: str = ...,
    join: str = ...,
    where: str = ...,
    user: str = ...,
    password: str = ...,
    delim: str = ...,
    cn: Incomplete | None = ...,
): ...
def TypeFinder(data, nRows, nCols, nullMarker: Incomplete | None = ...): ...
def _AdjustColHeadings(colHeadings, maxColLabelLen): ...
def GetTypeStrings(colHeadings, colTypes, keyCol: Incomplete | None = ...): ...
def _insertBlock(conn, sqlStr, block, silent: bool = ...): ...
def _AddDataToDb(
    dBase,
    table,
    user,
    password,
    colDefs,
    colTypes,
    data,
    nullMarker: Incomplete | None = ...,
    blockSize: int = ...,
    cn: Incomplete | None = ...,
) -> None: ...
def TextFileToDatabase(
    dBase,
    table,
    inF,
    delim: str = ...,
    user: str = ...,
    password: str = ...,
    maxColLabelLen: int = ...,
    keyCol: Incomplete | None = ...,
    nullMarker: Incomplete | None = ...,
) -> None: ...
def DatabaseToDatabase(
    fromDb,
    fromTbl,
    toDb,
    toTbl,
    fields: str = ...,
    join: str = ...,
    where: str = ...,
    user: str = ...,
    password: str = ...,
    keyCol: Incomplete | None = ...,
    nullMarker: str = ...,
) -> None: ...
