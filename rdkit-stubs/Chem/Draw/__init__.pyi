from rdkit.Chem.Draw.rdMolDraw2D import *
from _typeshed import Incomplete
from rdkit import Chem as Chem, RDConfig as RDConfig, rdBase as rdBase
from rdkit.Chem import rdDepictor as rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D as rdMolDraw2D
from rdkit.Chem.Draw.MolDrawing import (
    DrawingOptions as DrawingOptions,
    MolDrawing as MolDrawing,
)
from typing import NamedTuple

def _getCanvas(): ...
def _createCanvas(size): ...
def _legacyMolToImage(
    mol, size, kekulize, wedgeBonds, fitImage, options, canvas, **kwargs
): ...
def _sip_available(): ...
def MolDraw2DFromQPainter(
    qpainter,
    width: int = ...,
    height: int = ...,
    panelWidth: int = ...,
    panelHeight: int = ...,
): ...
def MolToImage(
    mol,
    size=...,
    kekulize: bool = ...,
    wedgeBonds: bool = ...,
    fitImage: bool = ...,
    options: Incomplete | None = ...,
    canvas: Incomplete | None = ...,
    **kwargs
): ...
def _legacyMolToFile(
    mol, fileName, size, kekulize, wedgeBonds, imageType, fitImage, options, **kwargs
) -> None: ...
def MolToFile(
    mol,
    filename,
    size=...,
    kekulize: bool = ...,
    wedgeBonds: bool = ...,
    imageType: Incomplete | None = ...,
    fitImage: bool = ...,
    options: Incomplete | None = ...,
    **kwargs
) -> None: ...
def MolToImageFile(
    mol, filename, size=..., kekulize: bool = ..., wedgeBonds: bool = ..., **kwargs
) -> None: ...
def ShowMol(
    mol,
    size=...,
    kekulize: bool = ...,
    wedgeBonds: bool = ...,
    title: str = ...,
    stayInFront: bool = ...,
    **kwargs
) -> None: ...
def MolToMPL(
    mol,
    size=...,
    kekulize: bool = ...,
    wedgeBonds: bool = ...,
    imageType: Incomplete | None = ...,
    fitImage: bool = ...,
    options: Incomplete | None = ...,
    **kwargs
): ...
def _bivariate_normal(
    X,
    Y,
    sigmax: float = ...,
    sigmay: float = ...,
    mux: float = ...,
    muy: float = ...,
    sigmaxy: float = ...,
): ...
def calcAtomGaussians(
    mol, a: float = ..., step: float = ..., weights: Incomplete | None = ...
): ...
def MolsToImage(mols, subImgSize=..., legends: Incomplete | None = ..., **kwargs): ...
def _drawerToImage(d2d): ...
def _okToKekulizeMol(mol, kekulize): ...
def _moltoimg(
    mol,
    sz,
    highlights,
    legend,
    returnPNG: bool = ...,
    drawOptions: Incomplete | None = ...,
    **kwargs
): ...
def _moltoSVG(
    mol,
    sz,
    highlights,
    legend,
    kekulize,
    drawOptions: Incomplete | None = ...,
    **kwargs
): ...
def _MolsToGridImage(
    mols,
    molsPerRow: int = ...,
    subImgSize=...,
    legends: Incomplete | None = ...,
    highlightAtomLists: Incomplete | None = ...,
    highlightBondLists: Incomplete | None = ...,
    drawOptions: Incomplete | None = ...,
    returnPNG: bool = ...,
    **kwargs
): ...
def _MolsToGridSVG(
    mols,
    molsPerRow: int = ...,
    subImgSize=...,
    legends: Incomplete | None = ...,
    highlightAtomLists: Incomplete | None = ...,
    highlightBondLists: Incomplete | None = ...,
    drawOptions: Incomplete | None = ...,
    **kwargs
): ...
def MolsToGridImage(
    mols,
    molsPerRow: int = ...,
    subImgSize=...,
    legends: Incomplete | None = ...,
    highlightAtomLists: Incomplete | None = ...,
    highlightBondLists: Incomplete | None = ...,
    useSVG: bool = ...,
    returnPNG: bool = ...,
    **kwargs
): ...
def _legacyReactionToImage(rxn, subImgSize=..., **kwargs): ...
def ReactionToImage(
    rxn,
    subImgSize=...,
    useSVG: bool = ...,
    drawOptions: Incomplete | None = ...,
    returnPNG: bool = ...,
    **kwargs
): ...
def MolToQPixmap(
    mol,
    size=...,
    kekulize: bool = ...,
    wedgeBonds: bool = ...,
    fitImage: bool = ...,
    options: Incomplete | None = ...,
    **kwargs
): ...
def DrawMorganBit(mol, bitId, bitInfo, whichExample: int = ..., **kwargs): ...
def DrawMorganBits(tpls, **kwargs): ...

class FingerprintEnv(NamedTuple):
    submol: Incomplete
    highlightAtoms: Incomplete
    atomColors: Incomplete
    highlightBonds: Incomplete
    bondColors: Incomplete
    highlightRadii: Incomplete

def _getMorganEnv(
    mol,
    atomId,
    radius,
    baseRad,
    aromaticColor,
    ringColor,
    centerColor,
    extraColor,
    **kwargs
): ...
def DrawMorganEnvs(
    envs,
    molsPerRow: int = ...,
    subImgSize=...,
    baseRad: float = ...,
    useSVG: bool = ...,
    aromaticColor=...,
    ringColor=...,
    centerColor=...,
    extraColor=...,
    legends: Incomplete | None = ...,
    drawOptions: Incomplete | None = ...,
    **kwargs
): ...
def DrawMorganEnv(
    mol,
    atomId,
    radius,
    molSize=...,
    baseRad: float = ...,
    useSVG: bool = ...,
    aromaticColor=...,
    ringColor=...,
    centerColor=...,
    extraColor=...,
    drawOptions: Incomplete | None = ...,
    **kwargs
): ...
def DrawRDKitBits(tpls, **kwargs): ...
def DrawRDKitBit(mol, bitId, bitInfo, whichExample: int = ..., **kwargs): ...
def _getRDKitEnv(
    mol, bondPath, baseRad, aromaticColor, extraColor, nonAromaticColor, **kwargs
): ...
def DrawRDKitEnvs(
    envs,
    molsPerRow: int = ...,
    subImgSize=...,
    baseRad: float = ...,
    useSVG: bool = ...,
    aromaticColor=...,
    extraColor=...,
    nonAromaticColor: Incomplete | None = ...,
    legends: Incomplete | None = ...,
    drawOptions: Incomplete | None = ...,
    **kwargs
): ...
def DrawRDKitEnv(
    mol,
    bondPath,
    molSize=...,
    baseRad: float = ...,
    useSVG: bool = ...,
    aromaticColor=...,
    extraColor=...,
    nonAromaticColor: Incomplete | None = ...,
    drawOptions: Incomplete | None = ...,
    **kwargs
): ...
def SetComicMode(opts) -> None: ...
