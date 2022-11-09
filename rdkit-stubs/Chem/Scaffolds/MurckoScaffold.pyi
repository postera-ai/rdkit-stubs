from _typeshed import Incomplete
from rdkit import Chem as Chem
from rdkit.Chem import AllChem as AllChem

murckoTransforms: Incomplete

def MakeScaffoldGeneric(mol): ...

murckoPatts: Incomplete
murckoQ: Incomplete
aromaticNTransform: Incomplete

def GetScaffoldForMol(mol): ...
def _pyGetScaffoldForMol(mol): ...
def MurckoScaffoldSmiles(
    smiles: Incomplete | None = ...,
    mol: Incomplete | None = ...,
    includeChirality: bool = ...,
): ...
def MurckoScaffoldSmilesFromSmiles(smiles, includeChirality: bool = ...): ...
def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
