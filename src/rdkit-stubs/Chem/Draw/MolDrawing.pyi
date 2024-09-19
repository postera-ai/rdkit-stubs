from _typeshed import Incomplete
from rdkit import Chem as Chem

def cmp(t1, t2): ...

periodicTable: Incomplete

class Font:
    face: Incomplete
    size: Incomplete
    weight: Incomplete
    name: Incomplete
    def __init__(
        self,
        face: Incomplete | None = ...,
        size: Incomplete | None = ...,
        name: Incomplete | None = ...,
        weight: Incomplete | None = ...,
    ) -> None: ...

class DrawingOptions:
    dotsPerAngstrom: int
    useFraction: float
    atomLabelFontFace: str
    atomLabelFontSize: int
    atomLabelMinFontSize: int
    atomLabelDeuteriumTritium: bool
    bondLineWidth: float
    dblBondOffset: float
    dblBondLengthFrac: float
    defaultColor: Incomplete
    selectColor: Incomplete
    bgColor: Incomplete
    colorBonds: bool
    noCarbonSymbols: bool
    includeAtomNumbers: bool
    atomNumberOffset: int
    radicalSymbol: str
    dash: Incomplete
    wedgeDashedBonds: bool
    showUnknownDoubleBonds: bool
    coordScale: float
    elemDict: Incomplete

class MolDrawing:
    canvas: Incomplete
    canvasSize: Incomplete
    drawingOptions: Incomplete
    atomPs: Incomplete
    boundingBoxes: Incomplete
    def __init__(
        self, canvas: Incomplete | None = ..., drawingOptions: Incomplete | None = ...
    ) -> None: ...
    def transformPoint(self, pos): ...
    def _getBondOffset(self, p1, p2): ...
    def _getOffsetBondPts(
        self, p1, p2, offsetX, offsetY, lenFrac: Incomplete | None = ...
    ): ...
    def _offsetDblBond(
        self,
        p1,
        p2,
        bond,
        a1,
        a2,
        conf,
        direction: int = ...,
        lenFrac: Incomplete | None = ...,
    ): ...
    def _getBondAttachmentCoordinates(self, p1, p2, labelSize): ...
    def _drawWedgedBond(
        self,
        bond,
        pos,
        nbrPos,
        width: Incomplete | None = ...,
        color: Incomplete | None = ...,
        dash: Incomplete | None = ...,
    ) -> None: ...
    def _drawBond(
        self,
        bond,
        atom,
        nbr,
        pos,
        nbrPos,
        conf,
        width: Incomplete | None = ...,
        color: Incomplete | None = ...,
        color2: Incomplete | None = ...,
        labelSize1: Incomplete | None = ...,
        labelSize2: Incomplete | None = ...,
    ) -> None: ...
    molTrans: Incomplete
    currAtomLabelFontSize: Incomplete
    drawingTrans: Incomplete
    def scaleAndCenter(
        self,
        mol,
        conf,
        coordCenter: bool = ...,
        canvasSize: Incomplete | None = ...,
        ignoreHs: bool = ...,
    ) -> None: ...
    def _drawLabel(
        self, label, pos, baseOffset, font, color: Incomplete | None = ..., **kwargs
    ): ...
    currDotsPerAngstrom: Incomplete
    activeMol: Incomplete
    bondRings: Incomplete
    def AddMol(
        self,
        mol,
        centerIt: bool = ...,
        molTrans: Incomplete | None = ...,
        drawingTrans: Incomplete | None = ...,
        highlightAtoms=...,
        confId: int = ...,
        flagCloseContactsDist: int = ...,
        highlightMap: Incomplete | None = ...,
        ignoreHs: bool = ...,
        highlightBonds=...,
        **kwargs
    ) -> None: ...
