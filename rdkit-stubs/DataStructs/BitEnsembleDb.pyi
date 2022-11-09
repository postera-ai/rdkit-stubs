from _typeshed import Incomplete
from rdkit.DataStructs.BitEnsemble import BitEnsemble as BitEnsemble

def _InitScoreTable(
    self, dbConn, tableName, idInfo: str = ..., actInfo: str = ...
) -> None: ...
def _ScoreToDb(
    self,
    sig,
    dbConn,
    tableName: Incomplete | None = ...,
    id: Incomplete | None = ...,
    act: Incomplete | None = ...,
) -> None: ...
