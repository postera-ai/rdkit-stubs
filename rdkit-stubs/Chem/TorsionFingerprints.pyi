from _typeshed import Incomplete
from rdkit import (
    Chem as Chem,
    Geometry as Geometry,
    RDConfig as RDConfig,
    rdBase as rdBase,
)
from rdkit.Chem import rdMolDescriptors as rdMolDescriptors, rdchem as rdchem

def _doMatch(inv, atoms): ...
def _doNotMatch(inv, atoms): ...
def _doMatchExcept1(inv, atoms): ...
def _getAtomInvariantsWithRadius(mol, radius): ...
def _getHeavyAtomNeighbors(atom1, aid2: int = ...): ...
def _getIndexforTorsion(neighbors, inv): ...
def _getBondsForTorsions(mol, ignoreColinearBonds): ...
def CalculateTorsionLists(
    mol, maxDev: str = ..., symmRadius: int = ..., ignoreColinearBonds: bool = ...
): ...
def _getTorsionAtomPositions(atoms, conf): ...
def CalculateTorsionAngles(mol, tors_list, tors_list_rings, confId: int = ...): ...
def _findCentralBond(mol, distmat): ...
def _calculateBeta(mol, distmat, aid1): ...
def CalculateTorsionWeights(
    mol, aid1: int = ..., aid2: int = ..., ignoreColinearBonds: bool = ...
): ...
def CalculateTFD(torsions1, torsions2, weights: Incomplete | None = ...): ...
def _getSameAtomOrder(mol1, mol2): ...
def GetTFDBetweenConformers(
    mol,
    confIds1,
    confIds2,
    useWeights: bool = ...,
    maxDev: str = ...,
    symmRadius: int = ...,
    ignoreColinearBonds: bool = ...,
): ...
def GetTFDBetweenMolecules(
    mol1,
    mol2,
    confId1: int = ...,
    confId2: int = ...,
    useWeights: bool = ...,
    maxDev: str = ...,
    symmRadius: int = ...,
    ignoreColinearBonds: bool = ...,
): ...
def GetTFDMatrix(
    mol,
    useWeights: bool = ...,
    maxDev: str = ...,
    symmRadius: int = ...,
    ignoreColinearBonds: bool = ...,
): ...
