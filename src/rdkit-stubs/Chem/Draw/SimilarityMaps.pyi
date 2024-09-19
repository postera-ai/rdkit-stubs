from _typeshed import Incomplete
from rdkit import Chem as Chem, DataStructs as DataStructs, Geometry as Geometry
from rdkit.Chem import Draw as Draw, rdDepictor as rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D as rdMolDraw2D

def _DeleteFpInfoAttr(mol) -> None: ...
def GetAtomicWeightsForFingerprint(refMol, probeMol, fpFunction, metric=...): ...
def GetAtomicWeightsForModel(probeMol, fpFunction, predictionFunction): ...
def GetStandardizedWeights(weights): ...
def GetSimilarityMapFromWeights(
    mol,
    weights,
    colorMap: Incomplete | None = ...,
    scale: int = ...,
    size=...,
    sigma: Incomplete | None = ...,
    coordScale: float = ...,
    step: float = ...,
    colors: str = ...,
    contourLines: int = ...,
    alpha: float = ...,
    draw2d: Incomplete | None = ...,
    **kwargs
): ...
def GetSimilarityMapForFingerprint(
    refMol, probeMol, fpFunction, metric=..., **kwargs
): ...
def GetSimilarityMapForModel(probeMol, fpFunction, predictionFunction, **kwargs): ...

apDict: Incomplete

def GetAPFingerprint(
    mol,
    atomId: int = ...,
    fpType: str = ...,
    nBits: int = ...,
    minLength: int = ...,
    maxLength: int = ...,
    nBitsPerEntry: int = ...,
    **kwargs
): ...

ttDict: Incomplete

def GetTTFingerprint(
    mol,
    atomId: int = ...,
    fpType: str = ...,
    nBits: int = ...,
    targetSize: int = ...,
    nBitsPerEntry: int = ...,
    **kwargs
): ...
def GetMorganFingerprint(
    mol,
    atomId: int = ...,
    radius: int = ...,
    fpType: str = ...,
    nBits: int = ...,
    useFeatures: bool = ...,
    **kwargs
): ...
def GetRDKFingerprint(
    mol,
    atomId: int = ...,
    fpType: str = ...,
    nBits: int = ...,
    minPath: int = ...,
    maxPath: int = ...,
    nBitsPerHash: int = ...,
    **kwargs
): ...
