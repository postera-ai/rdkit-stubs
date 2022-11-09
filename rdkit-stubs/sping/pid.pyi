from rdkit.sping.colors import *
from _typeshed import Incomplete

__version_maj_number__: str
__version_min_number__: str
__version__: Incomplete
inch: int
cm: Incomplete

class StateSaver:
    canvas: Incomplete
    defaultLineColor: Incomplete
    defaultFillColor: Incomplete
    defaultLineWidth: Incomplete
    defaultFont: Incomplete
    def __init__(self, canvas) -> None: ...
    def __del__(self) -> None: ...

class Font:
    def __init__(
        self,
        size: int = ...,
        bold: int = ...,
        italic: int = ...,
        underline: int = ...,
        face: Incomplete | None = ...,
    ) -> None: ...
    def __cmp__(self, other): ...
    def __repr__(self): ...
    def __setattr__(self, name, value) -> None: ...

figureLine: int
figureArc: int
figureCurve: int
keyBksp: str
keyDel: str
keyLeft: str
keyRight: str
keyUp: str
keyDown: str
keyPgUp: str
keyPgDn: str
keyHome: str
keyEnd: str
keyClear: str
keyTab: str
modShift: int
modControl: int

class Canvas:
    defaultLineColor: Incomplete
    defaultFillColor: Incomplete
    defaultLineWidth: int
    defaultFont: Incomplete
    onClick: Incomplete
    onOver: Incomplete
    onKey: Incomplete
    def __init__(self, size=..., name: str = ...) -> None: ...
    def getSize(self): ...
    def isInteractive(self): ...
    def canUpdate(self): ...
    def clear(self) -> None: ...
    def flush(self) -> None: ...
    def save(
        self, file: Incomplete | None = ..., format: Incomplete | None = ...
    ) -> None: ...
    def setInfoLine(self, s) -> None: ...
    def stringBox(self, s, font: Incomplete | None = ...): ...
    def stringWidth(self, s, font: Incomplete | None = ...) -> None: ...
    def fontHeight(self, font: Incomplete | None = ...): ...
    def fontAscent(self, font: Incomplete | None = ...) -> None: ...
    def fontDescent(self, font: Incomplete | None = ...) -> None: ...
    def arcPoints(self, x1, y1, x2, y2, startAng: int = ..., extent: int = ...): ...
    def curvePoints(self, x1, y1, x2, y2, x3, y3, x4, y4): ...
    def drawMultiLineString(
        self,
        s,
        x,
        y,
        font: Incomplete | None = ...,
        color: Incomplete | None = ...,
        angle: int = ...,
        **kwargs
    ) -> None: ...
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
    def drawLines(
        self,
        lineList,
        color: Incomplete | None = ...,
        width: Incomplete | None = ...,
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
    def drawCurve(
        self,
        x1,
        y1,
        x2,
        y2,
        x3,
        y3,
        x4,
        y4,
        edgeColor: Incomplete | None = ...,
        edgeWidth: Incomplete | None = ...,
        fillColor: Incomplete | None = ...,
        closed: int = ...,
        dash: Incomplete | None = ...,
        **kwargs
    ) -> None: ...
    def drawRect(
        self,
        x1,
        y1,
        x2,
        y2,
        edgeColor: Incomplete | None = ...,
        edgeWidth: Incomplete | None = ...,
        fillColor: Incomplete | None = ...,
        dash: Incomplete | None = ...,
        **kwargs
    ) -> None: ...
    def drawRoundRect(
        self,
        x1,
        y1,
        x2,
        y2,
        rx: int = ...,
        ry: int = ...,
        edgeColor: Incomplete | None = ...,
        edgeWidth: Incomplete | None = ...,
        fillColor: Incomplete | None = ...,
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
        fillColor: Incomplete | None = ...,
        dash: Incomplete | None = ...,
        **kwargs
    ) -> None: ...
    def drawArc(
        self,
        x1,
        y1,
        x2,
        y2,
        startAng: int = ...,
        extent: int = ...,
        edgeColor: Incomplete | None = ...,
        edgeWidth: Incomplete | None = ...,
        fillColor: Incomplete | None = ...,
        dash: Incomplete | None = ...,
        **kwargs
    ) -> None: ...
    def drawPolygon(
        self,
        pointlist,
        edgeColor: Incomplete | None = ...,
        edgeWidth: Incomplete | None = ...,
        fillColor: Incomplete | None = ...,
        closed: int = ...,
        dash: Incomplete | None = ...,
        **kwargs
    ) -> None: ...
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

def getFileObject(file, openFlags: str = ...): ...

class AffineMatrix:
    A: Incomplete
    def __init__(self, init: Incomplete | None = ...) -> None: ...
    def scale(self, sx, sy) -> None: ...
    def rotate(self, theta) -> None: ...
    def translate(self, tx, ty) -> None: ...
