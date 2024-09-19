from _typeshed import Incomplete
from rdkit import Chem as Chem
from rdkit.Chem import (
    AllChem as AllChem,
    Crippen as Crippen,
    Descriptors as Descriptors,
    Lipinski as Lipinski,
)

decBase: Incomplete

class Compound(decBase):
    __tablename__: str
    guid: Incomplete
    molpkl: Incomplete

def RegisterSchema(dbUrl, echo: bool = ...): ...

ConnectToSchema = RegisterSchema

def _ConnectToSchema(dbUrl, echo: bool = ...): ...

logger: Incomplete

def ProcessMol(
    session,
    mol,
    globalProps,
    nDone,
    nameProp: str = ...,
    nameCol: str = ...,
    redraw: bool = ...,
    keepHs: bool = ...,
    skipProps: bool = ...,
    addComputedProps: bool = ...,
    skipSmiles: bool = ...,
): ...
def LoadDb(
    suppl,
    dbName,
    nameProp: str = ...,
    nameCol: str = ...,
    silent: bool = ...,
    redraw: bool = ...,
    errorsTo: Incomplete | None = ...,
    keepHs: bool = ...,
    defaultVal: str = ...,
    skipProps: bool = ...,
    regName: str = ...,
    skipSmiles: bool = ...,
    maxRowsCached: int = ...,
    uniqNames: bool = ...,
    addComputedProps: bool = ...,
    lazySupplier: bool = ...,
    numForPropScan: int = ...,
    startAnew: bool = ...,
) -> None: ...
