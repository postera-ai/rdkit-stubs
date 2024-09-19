from typing import Optional
from rdkit.Chem.rdchem import (
    ALLOW_CHARGE_SEPARATION as ALLOW_CHARGE_SEPARATION,
    ALLOW_INCOMPLETE_OCTETS as ALLOW_INCOMPLETE_OCTETS,
    AllProps as AllProps,
    AtomProps as AtomProps,
    BondProps as BondProps,
    CHI_OTHER as CHI_OTHER,
    CHI_TETRAHEDRAL_CCW as CHI_TETRAHEDRAL_CCW,
    CHI_TETRAHEDRAL_CW as CHI_TETRAHEDRAL_CW,
    CHI_UNSPECIFIED as CHI_UNSPECIFIED,
    COMPOSITE_AND as COMPOSITE_AND,
    COMPOSITE_OR as COMPOSITE_OR,
    COMPOSITE_XOR as COMPOSITE_XOR,
    ComputedProps as ComputedProps,
    CoordsAsDouble as CoordsAsDouble,
    KEKULE_ALL as KEKULE_ALL,
    MolProps as MolProps,
    NoConformers as NoConformers,
    NoProps as NoProps,
    PrivateProps as PrivateProps,
    QueryAtomData as QueryAtomData,
    STEREO_ABSOLUTE as STEREO_ABSOLUTE,
    STEREO_AND as STEREO_AND,
    STEREO_OR as STEREO_OR,
    UNCONSTRAINED_ANIONS as UNCONSTRAINED_ANIONS,
    UNCONSTRAINED_CATIONS as UNCONSTRAINED_CATIONS,
    Atom as Atom,
    AtomKekulizeException as AtomKekulizeException,
    AtomMonomerInfo as AtomMonomerInfo,
    AtomMonomerType as AtomMonomerType,
    AtomPDBResidueInfo as AtomPDBResidueInfo,
    AtomSanitizeException as AtomSanitizeException,
    AtomValenceException as AtomValenceException,
    Bond as Bond,
    BondDir as BondDir,
    BondStereo as BondStereo,
    BondType as BondType,
    ChiralType as ChiralType,
    CompositeQueryType as CompositeQueryType,
    Conformer as Conformer,
    EditableMol as EditableMol,
    FixedMolSizeMolBundle as FixedMolSizeMolBundle,
    HybridizationType as HybridizationType,
    KekulizeException as KekulizeException,
    Mol as Mol,
    MolBundle as MolBundle,
    MolSanitizeException as MolSanitizeException,
    PeriodicTable as PeriodicTable,
    PropertyPickleOptions as PropertyPickleOptions,
    QueryAtom as QueryAtom,
    QueryBond as QueryBond,
    RWMol as RWMol,
    ResonanceFlags as ResonanceFlags,
    ResonanceMolSupplier as ResonanceMolSupplier,
    ResonanceMolSupplierCallback as ResonanceMolSupplierCallback,
    RingInfo as RingInfo,
    StereoDescriptor as StereoDescriptor,
    StereoGroup as StereoGroup,
    StereoGroupType as StereoGroupType,
    StereoGroup_vect as StereoGroup_vect,
    StereoInfo as StereoInfo,
    StereoSpecified as StereoSpecified,
    StereoType as StereoType,
    SubstanceGroup as SubstanceGroup,
    SubstanceGroupAttach as SubstanceGroupAttach,
    SubstanceGroupCState as SubstanceGroupCState,
    SubstanceGroup_VECT as SubstanceGroup_VECT,
    SubstructMatchParameters as SubstructMatchParameters,
    AddMolSubstanceGroup as AddMolSubstanceGroup,
    ClearMolSubstanceGroups as ClearMolSubstanceGroups,
    CreateMolSubstanceGroup as CreateMolSubstanceGroup,
    CreateStereoGroup as CreateStereoGroup,
    GetAtomAlias as GetAtomAlias,
    GetAtomRLabel as GetAtomRLabel,
    GetAtomValue as GetAtomValue,
    GetDefaultPickleProperties as GetDefaultPickleProperties,
    GetMolSubstanceGroupWithIdx as GetMolSubstanceGroupWithIdx,
    GetMolSubstanceGroups as GetMolSubstanceGroups,
    GetPeriodicTable as GetPeriodicTable,
    GetSupplementalSmilesLabel as GetSupplementalSmilesLabel,
    SetAtomAlias as SetAtomAlias,
    SetAtomRLabel as SetAtomRLabel,
    SetAtomValue as SetAtomValue,
    SetDefaultPickleProperties as SetDefaultPickleProperties,
    SetSupplementalSmilesLabel as SetSupplementalSmilesLabel,
    tossit as tossit,
)

from rdkit.Chem.rdmolfiles import *
from rdkit.Chem.rdmolops import *
from rdkit.Chem.rdCIPLabeler import *
from rdkit.Chem.inchi import *
from rdkit.Chem.rdMolInterchange import *
from _typeshed import Incomplete
from rdkit import DataStructs as DataStructs, RDConfig as RDConfig, rdBase as rdBase
from rdkit.Chem import rdCoordGen as rdCoordGen, rdchem as rdchem
from rdkit.Geometry import rdGeometry as rdGeometry

_HasSubstructMatchStr: Incomplete
templDir: Incomplete

def QuickSmartsMatch(
    smi: str, sma: str, unique: bool = True, display: bool = False
) -> tuple[tuple[int, ...], ...]: ...
def CanonSmiles(smi: str, useChiral: int = 1) -> str: ...
def SupplierFromFilename(fileN: str, delim: str = "", **kwargs): ...
def FindMolChiralCenters(
    mol: Mol,
    force: bool = True,
    includeUnassigned: bool = False,
    includeCIP: bool = True,
    useLegacyImplementation: Optional[bool] = None,
) -> list[tuple[int, str]]:
    """
    >>> from rdkit import Chem
    >>> mol = Chem.MolFromSmiles('[C@H](Cl)(F)Br')
    >>> Chem.FindMolChiralCenters(mol)
    [(0, 'R')]
    >>> mol = Chem.MolFromSmiles('[C@@H](Cl)(F)Br')
    >>> Chem.FindMolChiralCenters(mol)
    [(0, 'S')]

    >>> Chem.FindMolChiralCenters(Chem.MolFromSmiles('CCC'))
    []

    By default unassigned stereo centers are not reported:

    >>> mol = Chem.MolFromSmiles('C[C@H](F)C(F)(Cl)Br')
    >>> Chem.FindMolChiralCenters(mol,force=True)
    [(1, 'S')]

    but this can be changed:

    >>> Chem.FindMolChiralCenters(mol,force=True,includeUnassigned=True)
    [(1, 'S'), (3, '?')]

    The handling of unassigned stereocenters for dependent stereochemistry is not correct
    using the legacy implementation:

    >>> Chem.FindMolChiralCenters(Chem.MolFromSmiles('C1CC(C)C(C)C(C)C1'),includeUnassigned=True)
    [(2, '?'), (6, '?')]
    >>> Chem.FindMolChiralCenters(Chem.MolFromSmiles('C1C[C@H](C)C(C)[C@H](C)C1'),includeUnassigned=True)
    [(2, 'S'), (4, '?'), (6, 'R')]

    But works with the new implementation:

    >>> Chem.FindMolChiralCenters(Chem.MolFromSmiles('C1CC(C)C(C)C(C)C1'),includeUnassigned=True, useLegacyImplementation=False)
    [(2, '?'), (4, '?'), (6, '?')]

    Note that the new implementation also gets the correct descriptors for para-stereochemistry:

    >>> Chem.FindMolChiralCenters(Chem.MolFromSmiles('C1C[C@H](C)[C@H](C)[C@H](C)C1'),useLegacyImplementation=False)
    [(2, 'S'), (4, 's'), (6, 'R')]

    With the new implementation, if you don't care about the CIP labels of stereocenters, you can save
    some time by disabling those:

    >>> Chem.FindMolChiralCenters(Chem.MolFromSmiles('C1C[C@H](C)[C@H](C)[C@H](C)C1'), includeCIP=False, useLegacyImplementation=False)
    [(2, 'Tet_CCW'), (4, 'Tet_CCW'), (6, 'Tet_CCW')]

    """

def WrapLogs() -> None: ...
def LogWarningMsg(msg: str) -> None: ...
def LogErrorMsg(msg: str) -> None: ...
def _test(): ...
