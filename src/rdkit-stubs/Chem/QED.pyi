from _typeshed import Incomplete
from rdkit import Chem as Chem
from rdkit.Chem import Crippen as Crippen, MolSurf as MolSurf
from rdkit.Chem.ChemUtils.DescriptorUtilities import (
    setDescriptorVersion as setDescriptorVersion,
)
from typing import NamedTuple

class QEDproperties(NamedTuple):
    MW: Incomplete
    ALOGP: Incomplete
    HBA: Incomplete
    HBD: Incomplete
    PSA: Incomplete
    ROTB: Incomplete
    AROM: Incomplete
    ALERTS: Incomplete

class ADSparameter(NamedTuple):
    A: Incomplete
    B: Incomplete
    C: Incomplete
    D: Incomplete
    E: Incomplete
    F: Incomplete
    DMAX: Incomplete

WEIGHT_MAX: Incomplete
WEIGHT_MEAN: Incomplete
WEIGHT_NONE: Incomplete
AliphaticRings: Incomplete
AcceptorSmarts: Incomplete
Acceptors: Incomplete
StructuralAlertSmarts: Incomplete
StructuralAlerts: Incomplete
adsParameters: Incomplete

def ads(x, adsParameter): ...
def properties(mol): ...
def qed(mol, w=..., qedProperties: Incomplete | None = ...): ...
def weights_max(mol): ...
def weights_mean(mol): ...
def weights_none(mol): ...
def default(mol): ...
def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
