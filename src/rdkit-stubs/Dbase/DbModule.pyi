from _typeshed import Incomplete
from rdkit import RDConfig as RDConfig

sqlTextTypes: Incomplete
sqlIntTypes: Incomplete
sqlFloatTypes: Incomplete
sqlBinTypes: Incomplete
getTablesSql: str
getTablesAndViewsSql: str
getDbSql: str
fileWildcard: Incomplete
placeHolder: str
binaryTypeName: str
RDTestDatabase: str
dbFileWildcard: str
fileWildcard = dbFileWildcard
binaryHolder = memoryview

def connect(x, *args): ...
