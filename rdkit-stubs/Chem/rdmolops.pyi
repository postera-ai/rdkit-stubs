from typing import Any, ClassVar, Sequence, overload

from rdkit.Chem.rdchem import Mol
from rdkit.Chem.rdMolDescriptors import AtomPairsParameters
from rdkit.DataStructs.cDataStructs import ExplicitBitVect

ADJUST_IGNOREALL: AdjustQueryWhichFlags
ADJUST_IGNORECHAINS: AdjustQueryWhichFlags
ADJUST_IGNOREDUMMIES: AdjustQueryWhichFlags
ADJUST_IGNORENONDUMMIES: AdjustQueryWhichFlags
ADJUST_IGNORENONE: AdjustQueryWhichFlags
ADJUST_IGNORERINGS: AdjustQueryWhichFlags
AROMATICITY_CUSTOM: AromaticityModel
AROMATICITY_DEFAULT: AromaticityModel
AROMATICITY_MDL: AromaticityModel
AROMATICITY_RDKIT: AromaticityModel
AROMATICITY_SIMPLE: AromaticityModel
LayeredFingerprint_substructLayers: int
SANITIZE_ADJUSTHS: SanitizeFlags
SANITIZE_ALL: SanitizeFlags
SANITIZE_CLEANUP: SanitizeFlags
SANITIZE_CLEANUPCHIRALITY: SanitizeFlags
SANITIZE_FINDRADICALS: SanitizeFlags
SANITIZE_KEKULIZE: SanitizeFlags
SANITIZE_NONE: SanitizeFlags
SANITIZE_PROPERTIES: SanitizeFlags
SANITIZE_SETAROMATICITY: SanitizeFlags
SANITIZE_SETCONJUGATION: SanitizeFlags
SANITIZE_SETHYBRIDIZATION: SanitizeFlags
SANITIZE_SYMMRINGS: SanitizeFlags
_LayeredFingerprint_version: str
_PatternFingerprint_version: str
_RDKFingerprint_version: str

class AdjustQueryParameters:
    __instance_size__: ClassVar[int] = ...
    adjustConjugatedFiveRings: Any
    adjustDegree: Any
    adjustDegreeFlags: Any
    adjustHeavyDegree: Any
    adjustHeavyDegreeFlags: Any
    adjustRingChain: Any
    adjustRingChainFlags: Any
    adjustRingCount: Any
    adjustRingCountFlags: Any
    adjustSingleBondsBetweenAromaticAtoms: Any
    adjustSingleBondsToDegreeOneNeighbors: Any
    aromatizeIfPossible: Any
    makeAtomsGeneric: Any
    makeAtomsGenericFlags: Any
    makeBondsGeneric: Any
    makeBondsGenericFlags: Any
    makeDummiesQueries: Any
    setMDLFiveRingAromaticity: Any
    useStereoCareForBonds: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def NoAdjustments(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class AdjustQueryWhichFlags:
    ADJUST_IGNOREALL: ClassVar[AdjustQueryWhichFlags] = ...
    ADJUST_IGNORECHAINS: ClassVar[AdjustQueryWhichFlags] = ...
    ADJUST_IGNOREDUMMIES: ClassVar[AdjustQueryWhichFlags] = ...
    ADJUST_IGNORENONDUMMIES: ClassVar[AdjustQueryWhichFlags] = ...
    ADJUST_IGNORENONE: ClassVar[AdjustQueryWhichFlags] = ...
    ADJUST_IGNORERINGS: ClassVar[AdjustQueryWhichFlags] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...

class AromaticityModel:
    AROMATICITY_CUSTOM: ClassVar[AromaticityModel] = ...
    AROMATICITY_DEFAULT: ClassVar[AromaticityModel] = ...
    AROMATICITY_MDL: ClassVar[AromaticityModel] = ...
    AROMATICITY_RDKIT: ClassVar[AromaticityModel] = ...
    AROMATICITY_SIMPLE: ClassVar[AromaticityModel] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...

class MolzipLabel:
    AtomMapNumber: ClassVar[MolzipLabel] = ...
    AtomType: ClassVar[MolzipLabel] = ...
    FragmentOnBonds: ClassVar[MolzipLabel] = ...
    Isotope: ClassVar[MolzipLabel] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...

class MolzipParams:
    __instance_size__: ClassVar[int] = ...
    enforceValenceRules: Any
    label: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def setAtomSymbols(cls, RDKit, boost) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class RemoveHsParameters:
    __instance_size__: ClassVar[int] = ...
    removeAndTrackIsotopes: Any
    removeDefiningBondStereo: Any
    removeDegreeZero: Any
    removeDummyNeighbors: Any
    removeHigherDegrees: Any
    removeHydrides: Any
    removeInSGroups: Any
    removeIsotopes: Any
    removeMapped: Any
    removeNonimplicit: Any
    removeOnlyHNeighbors: Any
    removeWithQuery: Any
    removeWithWedgedBond: Any
    showWarnings: Any
    updateExplicitCount: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class SanitizeFlags:
    SANITIZE_ADJUSTHS: ClassVar[SanitizeFlags] = ...
    SANITIZE_ALL: ClassVar[SanitizeFlags] = ...
    SANITIZE_CLEANUP: ClassVar[SanitizeFlags] = ...
    SANITIZE_CLEANUPCHIRALITY: ClassVar[SanitizeFlags] = ...
    SANITIZE_FINDRADICALS: ClassVar[SanitizeFlags] = ...
    SANITIZE_KEKULIZE: ClassVar[SanitizeFlags] = ...
    SANITIZE_NONE: ClassVar[SanitizeFlags] = ...
    SANITIZE_PROPERTIES: ClassVar[SanitizeFlags] = ...
    SANITIZE_SETAROMATICITY: ClassVar[SanitizeFlags] = ...
    SANITIZE_SETCONJUGATION: ClassVar[SanitizeFlags] = ...
    SANITIZE_SETHYBRIDIZATION: ClassVar[SanitizeFlags] = ...
    SANITIZE_SYMMRINGS: ClassVar[SanitizeFlags] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...

class StereoBondThresholds:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(cls) -> Any: ...
    @property
    def CHIRAL_ATOM(self) -> Any: ...
    @property
    def DBL_BOND_NO_STEREO(self) -> Any: ...
    @property
    def DBL_BOND_SPECIFIED_STEREO(self) -> Any: ...
    @property
    def DIRECTION_SET(self) -> Any: ...

class _vectN5RDKit9Chirality10StereoInfoE:
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def append(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def extend(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def __contains__(cls, other) -> Any: ...
    @classmethod
    def __delitem__(cls, other) -> Any: ...
    @classmethod
    def __getitem__(cls, index) -> Any: ...
    @classmethod
    def __iter__(cls, boost, std) -> Any: ...
    @classmethod
    def __len__(cls) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...
    @classmethod
    def __setitem__(cls, index, object) -> Any: ...

def AddHs(
    mol: Mol,
    explicitOnly: bool = False,
    addCoords: bool = False,
    onlyOnAtoms: AtomPairsParameters | None = None,
    addResidueInfo: bool = False,
) -> Mol: ...
def AddRecursiveQuery(*args, **kwargs) -> Any: ...
def AddWavyBondsForStereoAny(RDKit) -> Any: ...
def AdjustQueryProperties(RDKit) -> Any: ...
def AssignAtomChiralTagsFromMolParity(RDKit) -> Any: ...
def AssignAtomChiralTagsFromStructure(RDKit) -> Any: ...
def AssignChiralTypesFromBondDirs(RDKit) -> Any: ...
def AssignRadicals(RDKit) -> Any: ...
def AssignStereochemistry(*args, **kwargs) -> Any: ...
def AssignStereochemistryFrom3D(*args, **kwargs) -> Any: ...
def Cleanup(RDKit) -> Any: ...
def CombineMols(*args, **kwargs) -> Any: ...
def ConvertGenericQueriesToSubstanceGroups(RDKit) -> Any: ...
def DeleteSubstructs(*args, **kwargs) -> Any: ...
def DetectBondStereoChemistry(*args, **kwargs) -> Any: ...
def DetectBondStereochemistry(RDKit) -> Any: ...
def DetectChemistryProblems(RDKit) -> Any: ...
def FastFindRings(RDKit) -> Any: ...
def FindAllPathsOfLengthN(*args, **kwargs) -> Any: ...
def FindAllSubgraphsOfLengthMToN(*args, **kwargs) -> Any: ...
def FindAllSubgraphsOfLengthN(*args, **kwargs) -> Any: ...
def FindAtomEnvironmentOfRadiusN(*args, **kwargs) -> Any: ...
def FindPotentialStereo(RDKit) -> Any: ...
def FindPotentialStereoBonds(*args, **kwargs) -> Any: ...
def FindRingFamilies(RDKit) -> Any: ...
def FindUniqueSubgraphsOfLengthN(*args, **kwargs) -> Any: ...
def FragmentOnBRICSBonds(RDKit) -> Any: ...
def FragmentOnBonds(RDKit, boost) -> Any: ...
def FragmentOnSomeBonds(RDKit, boost) -> Any: ...
def Get3DDistanceMatrix(RDKit) -> Any: ...
def GetAdjacencyMatrix(RDKit) -> Any: ...
def GetDistanceMatrix(RDKit) -> Any: ...
def GetFormalCharge(RDKit) -> Any: ...
def GetMolFrags(
    mol: Mol,
    asMols: bool = False,
    sanitizeFrags: bool = True,
    frags: Sequence[int] | None = None,
    fragsMolAtomMapping: Sequence[Sequence[int]] | None = None,
) -> tuple[Mol] | tuple[tuple[int]]: ...
def GetMostSubstitutedCoreMatch(*args, **kwargs) -> Any: ...
def GetSSSR(RDKit) -> Any: ...
def GetShortestPath(*args, **kwargs) -> Any: ...
def GetSymmSSSR(RDKit) -> Any: ...
def Kekulize(RDKit) -> Any: ...
def KekulizeIfPossible(RDKit) -> Any: ...
def LayeredFingerprint(
    mol: Mol,
    layerFlags: int = 4294967295,
    minPath: int = 1,
    maxPath: int = 7,
    fpSize: int = 2048,
    atomCounts: list[int] = [],
    setOnlyBits: ExplicitBitVect | None = None,
    branchedPaths: bool = True,
    fromAtoms: Sequence[int] | None = None,
) -> ExplicitBitVect: ...
def MergeQueryHs(RDKit) -> Any: ...
def MolAddRecursiveQueries(*args, **kwargs) -> Any: ...
def MurckoDecompose(RDKit) -> Any: ...
def ParseMolQueryDefFile(boost) -> Any: ...
def PathToSubmol(RDKit, boost) -> Any: ...
def PatternFingerprint(RDKit) -> Any: ...
def RDKFingerprint(*args, **kwargs) -> Any: ...
def RemoveAllHs(RDKit) -> Any: ...
@overload
def RemoveHs(
    mol: Mol,
    implicitOnly: bool = False,
    updateExplicitCount: bool = False,
    sanitize: bool = True,
) -> Mol: ...
@overload
def RemoveHs(
    mol: Mol,
    params: RemoveHsParameters,
    sanitize: bool = True,
) -> Mol: ...
def RemoveStereochemistry(RDKit) -> Any: ...
def RenumberAtoms(RDKit, boost) -> Any: ...
def ReplaceCore(mol, core, match) -> Any: ...
def ReplaceSidechains(*args, **kwargs) -> Any: ...
def ReplaceSubstructs(*args, **kwargs) -> Any: ...
def SanitizeMol(*args, **kwargs) -> Any: ...
def SetAromaticity(RDKit) -> Any: ...
def SetBondStereoFromDirections(RDKit) -> Any: ...
def SetConjugation(RDKit) -> Any: ...
def SetDoubleBondNeighborDirections(RDKit) -> Any: ...
def SetGenericQueriesFromProperties(RDKit) -> Any: ...
def SetHybridization(RDKit) -> Any: ...
def SetTerminalAtomCoords(*args, **kwargs) -> Any: ...
def SortMatchesByDegreeOfCoreSubstitution(*args, **kwargs) -> Any: ...
def SplitMolByPDBChainId(RDKit) -> Any: ...
def SplitMolByPDBResidues(RDKit) -> Any: ...
def UnfoldedRDKFingerprintCountBased(RDKit) -> Any: ...
def WedgeBond(*args, **kwargs) -> Any: ...
def WedgeMolBonds(*args, **kwargs) -> Any: ...
def molzip(RDKit) -> Any: ...
