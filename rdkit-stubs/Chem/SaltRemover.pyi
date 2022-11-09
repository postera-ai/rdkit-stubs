from _typeshed import Incomplete
from collections.abc import Generator
from rdkit import Chem as Chem, RDConfig as RDConfig
from rdkit.Chem.rdmolfiles import (
    SDMolSupplier as SDMolSupplier,
    SmilesMolSupplier as SmilesMolSupplier,
)

class InputFormat:
    SMARTS: str
    MOL: str
    SMILES: str

def _smartsFromSmartsLine(line): ...
def _getSmartsSaltsFromStream(stream) -> Generator[Incomplete, None, None]: ...
def _getSmartsSaltsFromFile(filename): ...

class SaltRemover:
    defnFilename: Incomplete
    defnData: Incomplete
    salts: Incomplete
    defnFormat: Incomplete
    def __init__(
        self,
        defnFilename: Incomplete | None = ...,
        defnData: Incomplete | None = ...,
        defnFormat=...,
    ) -> None: ...
    def _initPatterns(self) -> None: ...
    def StripMol(self, mol, dontRemoveEverything: bool = ..., sanitize: bool = ...): ...
    def StripMolWithDeleted(self, mol, dontRemoveEverything: bool = ...): ...
    def _StripMol(
        self, mol, dontRemoveEverything: bool = ..., sanitize: bool = ...
    ): ...
    def __call__(self, mol, dontRemoveEverything: bool = ...): ...

def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
