from _typeshed import Incomplete

INCHI_AVAILABLE: bool

class InchiReadWriteError(Exception): ...

def MolFromInchi(
    inchi,
    sanitize: bool = ...,
    removeHs: bool = ...,
    logLevel: Incomplete | None = ...,
    treatWarningAsError: bool = ...,
): ...
def MolToInchiAndAuxInfo(
    mol,
    options: str = ...,
    logLevel: Incomplete | None = ...,
    treatWarningAsError: bool = ...,
): ...
def MolBlockToInchiAndAuxInfo(
    molblock,
    options: str = ...,
    logLevel: Incomplete | None = ...,
    treatWarningAsError: bool = ...,
): ...
def MolToInchi(
    mol,
    options: str = ...,
    logLevel: Incomplete | None = ...,
    treatWarningAsError: bool = ...,
): ...
def MolBlockToInchi(
    molblock,
    options: str = ...,
    logLevel: Incomplete | None = ...,
    treatWarningAsError: bool = ...,
): ...
def InchiToInchiKey(inchi): ...
def MolToInchiKey(mol, options: str = ...): ...
