from _typeshed import Incomplete
from rdkit.Dbase import DbInfo as DbInfo, DbModule as DbModule, DbUtils as DbUtils

class DbError(RuntimeError): ...

class DbConnect:
    dbName: Incomplete
    tableName: Incomplete
    user: Incomplete
    password: Incomplete
    cn: Incomplete
    cursor: Incomplete
    def __init__(
        self,
        dbName: str = ...,
        tableName: str = ...,
        user: str = ...,
        password: str = ...,
    ) -> None: ...
    def GetTableNames(self, includeViews: int = ...): ...
    def GetColumnNames(
        self,
        table: str = ...,
        join: str = ...,
        what: str = ...,
        where: str = ...,
        **kwargs
    ): ...
    def GetColumnNamesAndTypes(
        self,
        table: str = ...,
        join: str = ...,
        what: str = ...,
        where: str = ...,
        **kwargs
    ): ...
    def GetColumns(self, fields, table: str = ..., join: str = ..., **kwargs): ...
    def GetData(
        self,
        table: Incomplete | None = ...,
        fields: str = ...,
        where: str = ...,
        removeDups: int = ...,
        join: str = ...,
        transform: Incomplete | None = ...,
        randomAccess: int = ...,
        **kwargs
    ): ...
    def GetDataCount(
        self,
        table: Incomplete | None = ...,
        where: str = ...,
        join: str = ...,
        **kwargs
    ): ...
    def GetCursor(self): ...
    def KillCursor(self) -> None: ...
    def AddTable(self, tableName, colString) -> None: ...
    def InsertData(self, tableName, vals) -> None: ...
    def InsertColumnData(self, tableName, columnName, value, where) -> None: ...
    def AddColumn(self, tableName, colName, colType) -> None: ...
    def Commit(self) -> None: ...
