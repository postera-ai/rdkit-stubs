from rdkit.Chem.rdChemicalFeatures import *
from rdkit.Chem.rdMolChemicalFeatures import *
from rdkit.Chem import Mol

def MCFF_GetFeaturesForMol(
    self, mol: Mol, includeOnly: str = "", confId: int = -1
) -> tuple[MolChemicalFeature, ...]: ...
