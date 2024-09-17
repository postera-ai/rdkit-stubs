from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, Optional
from rdkit import Chem as Chem
from rdkit.Chem import (
    rdMolDescriptors as rdMolDescriptors,
    rdPartialCharges as rdPartialCharges,
)
from rdkit.Chem.EState.EState import (
    MaxAbsEStateIndex as MaxAbsEStateIndex,
    MaxEStateIndex as MaxEStateIndex,
    MinAbsEStateIndex as MinAbsEStateIndex,
    MinEStateIndex as MinEStateIndex,
)
from rdkit.Chem.QED import qed as qed

def _isCallable(thing): ...

_descList: Incomplete

def _setupDescriptors(namespace) -> None: ...

MolWt: Callable[[Chem.Mol], float]
"""
The average molecular weight of the molecule

>>> MolWt(Chem.MolFromSmiles('CC'))
30.07
>>> MolWt(Chem.MolFromSmiles('[NH4+].[Cl-]'))
53.49...
"""

def HeavyAtomMolWt(x: Chem.Mol) -> float:
    """The average molecular weight of the molecule ignoring hydrogens

    >>> HeavyAtomMolWt(Chem.MolFromSmiles('CC'))
    24.02...
    >>> HeavyAtomMolWt(Chem.MolFromSmiles('[NH4+].[Cl-]'))
    49.46

    """

ExactMolWt: Callable[[Chem.Mol], float]
"""
The exact molecular weight of the molecule

>>> ExactMolWt(Chem.MolFromSmiles('CC'))
30.04...
>>> ExactMolWt(Chem.MolFromSmiles('[13CH3]C'))
31.05...
"""

def NumValenceElectrons(mol: Chem.Mol) -> int:
    """
    The number of valence electrons the molecule has

    >>> NumValenceElectrons(Chem.MolFromSmiles('CC'))
    14
    >>> NumValenceElectrons(Chem.MolFromSmiles('C(=O)O'))
    18
    >>> NumValenceElectrons(Chem.MolFromSmiles('C(=O)[O-]'))
    18
    >>> NumValenceElectrons(Chem.MolFromSmiles('C(=O)'))
    12
    """

def NumRadicalElectrons(mol: Chem.Mol) -> int:
    """
    The number of radical electrons the molecule has
    (says nothing about spin state)

    >>> NumRadicalElectrons(Chem.MolFromSmiles('CC'))
    0
    >>> NumRadicalElectrons(Chem.MolFromSmiles('C[CH3]'))
    0
    >>> NumRadicalElectrons(Chem.MolFromSmiles('C[CH2]'))
    1
    >>> NumRadicalElectrons(Chem.MolFromSmiles('C[CH]'))
    2
    >>> NumRadicalElectrons(Chem.MolFromSmiles('C[C]'))
    3
    """

def _ChargeDescriptors(mol: Chem.Mol, force: bool = False) -> tuple[float, float]: ...
def MaxPartialCharge(mol: Chem.Mol, force: bool = False) -> float: ...
def MinPartialCharge(mol: Chem.Mol, force: bool = False) -> float: ...
def MaxAbsPartialCharge(mol: Chem.Mol, force: bool = False) -> float: ...
def MinAbsPartialCharge(mol: Chem.Mol, force: bool = False) -> float: ...
def _FingerprintDensity(mol: Chem.Mol, func, *args, **kwargs) -> float: ...
def FpDensityMorgan1(x) -> float: ...
def FpDensityMorgan2(x) -> float: ...
def FpDensityMorgan3(x) -> float: ...
def setupAUTOCorrDescriptors() -> None:
    """Adds AUTOCORR descriptors to the default descriptor lists"""

class PropertyFunctor(rdMolDescriptors.PythonPropertyFunctor):
    """
    Creates a python based property function that can be added to the
    global property list.  To use, subclass this class and override the
    __call__ method.  Then create an instance and add it to the
    registry.  The __call__ method should return a numeric value.

    Example:

        class NumAtoms(Descriptors.PropertyFunctor):
            def __init__(self):
                Descriptors.PropertyFunctor.__init__(self, "NumAtoms", "1.0.0")
            def __call__(self, mol):
                return mol.GetNumAtoms()

        numAtoms = NumAtoms()
        rdMolDescriptors.Properties.RegisterProperty(numAtoms)
    """

    def __init__(self, name, version) -> None: ...
    def __call__(self, mol) -> Any: ...

def CalcMolDescriptors(
    mol: Chem.Mol, missingVal: Optional[float] = None, silent: bool = True
) -> dict[str, float | int]:
    """
    calculate the full set of descriptors for a molecule

    Parameters
    ----------
    mol : RDKit molecule
    missingVal : float, optional
                 This will be used if a particular descriptor cannot be calculated
    silent : bool, optional
             if True then exception messages from descriptors will be displayed

    Returns
    -------
    dict
         A dictionary with decriptor names as keys and the descriptor values as values
    """

def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
