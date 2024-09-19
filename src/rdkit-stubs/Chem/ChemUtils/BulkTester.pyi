from rdkit import Chem as Chem
from rdkit.Chem import Randomize as Randomize

def TestMolecule(mol): ...
def TestSupplier(
    suppl,
    stopAfter: int = ...,
    reportInterval: int = ...,
    reportTo=...,
    nameProp: str = ...,
): ...
