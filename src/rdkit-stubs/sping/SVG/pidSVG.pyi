from rdkit.sping.pid import *
from math import *
from _typeshed import Incomplete
from rdkit.sping.PDF import pdfmetrics as pdfmetrics

SVG_HEADER: str

def _ColorToSVG(color): ...
def _PointListToSVG(points, dupFirst: int = ...): ...

class SVGCanvas(Canvas):
    _nImages: int
    _imageFormat: str
    size: Incomplete
    def __init__(
        self,
        size=...,
        name: str = ...,
        includeXMLHeader: bool = ...,
        extraHeaderText: str = ...,
    ) -> None: ...
    _txt: Incomplete
    def _initOutput(
        self, includeXMLHeader: bool = ..., extraHeaderText: str = ...
    ) -> None: ...
    def _findExternalFontName(self, font): ...
    def _FormFontStr(self, font): ...
    def _FormArcStr(self, x1, y1, x2, y2, theta1, extent): ...
    def clear(self) -> None: ...
    def flush(self) -> None: ...
    def save(
        self, file: Incomplete | None = ..., format: Incomplete | None = ...
    ) -> None: ...
    def text(self): ...
    def drawLine(
        self,
        x1,
        y1,
        x2,
        y2,
        color: Incomplete | None = ...,
        width: Incomplete | None = ...,
        dash: Incomplete | None = ...,
        **kwargs
    ) -> None: ...
    def drawPolygon(
        self,
        pointlist,
        edgeColor: Incomplete | None = ...,
        edgeWidth: Incomplete | None = ...,
        fillColor=...,
        closed: int = ...,
        dash: Incomplete | None = ...,
        **kwargs
    ) -> None: ...
    def drawEllipse(
        self,
        x1,
        y1,
        x2,
        y2,
        edgeColor: Incomplete | None = ...,
        edgeWidth: Incomplete | None = ...,
        fillColor=...,
        dash: Incomplete | None = ...,
        **kwargs
    ) -> None: ...
    def drawString(
        self,
        s,
        x,
        y,
        font: Incomplete | None = ...,
        color: Incomplete | None = ...,
        angle: int = ...,
        **kwargs
    ) -> None: ...
    def _drawStringOneLine(self, line, x, y, fontStr, svgColor, **kwargs): ...
    def drawFigure(
        self,
        partList,
        edgeColor: Incomplete | None = ...,
        edgeWidth: Incomplete | None = ...,
        fillColor: Incomplete | None = ...,
        closed: int = ...,
        dash: Incomplete | None = ...,
        **kwargs
    ) -> None: ...
    def drawImage(
        self,
        image,
        x1,
        y1,
        x2: Incomplete | None = ...,
        y2: Incomplete | None = ...,
        **kwargs
    ) -> None: ...
    def stringWidth(self, s, font: Incomplete | None = ...): ...
    def fontAscent(self, font: Incomplete | None = ...): ...
    def fontDescent(self, font: Incomplete | None = ...): ...

def test(): ...
def dashtest(): ...
def testit(canvas, s, x, y, font: Incomplete | None = ...) -> None: ...
def test2() -> None: ...
