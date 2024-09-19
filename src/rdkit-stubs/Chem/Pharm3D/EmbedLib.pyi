from _typeshed import Incomplete
from collections.abc import Generator
from rdkit import Chem as Chem
from rdkit.Chem import (
    ChemicalFeatures as ChemicalFeatures,
    ChemicalForceFields as ChemicalForceFields,
)
from rdkit.Chem.Pharm3D import ExcludedVolume as ExcludedVolume
from rdkit.ML.Data import Stats as Stats

_times: Incomplete
logger: Incomplete
defaultFeatLength: float

def GetAtomHeavyNeighbors(atom): ...
def ReplaceGroup(
    match, bounds, slop: float = ..., useDirs: bool = ..., dirLength=...
): ...
def EmbedMol(
    mol,
    bm,
    atomMatch: Incomplete | None = ...,
    weight: float = ...,
    randomSeed: int = ...,
    excludedVolumes: Incomplete | None = ...,
) -> None: ...
def AddExcludedVolumes(bm, excludedVolumes, smoothIt: bool = ...): ...
def UpdatePharmacophoreBounds(
    bm,
    atomMatch,
    pcophore,
    useDirs: bool = ...,
    dirLength=...,
    mol: Incomplete | None = ...,
): ...
def EmbedPharmacophore(
    mol,
    atomMatch,
    pcophore,
    randomSeed: int = ...,
    count: int = ...,
    smoothFirst: bool = ...,
    silent: bool = ...,
    bounds: Incomplete | None = ...,
    excludedVolumes: Incomplete | None = ...,
    targetNumber: int = ...,
    useDirs: bool = ...,
): ...
def isNaN(v): ...
def OptimizeMol(
    mol,
    bm,
    atomMatches: Incomplete | None = ...,
    excludedVolumes: Incomplete | None = ...,
    forceConstant: float = ...,
    maxPasses: int = ...,
    verbose: bool = ...,
): ...
def EmbedOne(
    mol, name, match, pcophore, count: int = ..., silent: int = ..., **kwargs
): ...
def MatchPharmacophoreToMol(mol, featFactory, pcophore): ...
def _getFeatDict(mol, featFactory, features): ...
def MatchFeatsToMol(mol, featFactory, features): ...
def CombiEnum(sequence) -> Generator[Incomplete, None, None]: ...
def DownsampleBoundsMatrix(bm, indices, maxThresh: float = ...): ...
def CoarseScreenPharmacophore(atomMatch, bounds, pcophore, verbose: bool = ...): ...
def Check2DBounds(atomMatch, mol, pcophore): ...
def _checkMatch(match, mol, bounds, pcophore, use2DLimits): ...
def ConstrainedEnum(
    matches, mol, pcophore, bounds, use2DLimits: bool = ..., index: int = ..., soFar=...
) -> Generator[Incomplete, None, None]: ...
def MatchPharmacophore(
    matches,
    bounds,
    pcophore,
    useDownsampling: bool = ...,
    use2DLimits: bool = ...,
    mol: Incomplete | None = ...,
    excludedVolumes: Incomplete | None = ...,
    useDirs: bool = ...,
): ...
def GetAllPharmacophoreMatches(
    matches,
    bounds,
    pcophore,
    useDownsampling: int = ...,
    progressCallback: Incomplete | None = ...,
    use2DLimits: bool = ...,
    mol: Incomplete | None = ...,
    verbose: bool = ...,
): ...
def ComputeChiralVolume(mol, centerIdx, confId: int = ...): ...
def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
