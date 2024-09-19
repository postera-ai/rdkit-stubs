from rdkit.sping.pid import *
from _typeshed import Incomplete

f: Incomplete
_widthmaps: Incomplete
_ascents: Incomplete
_descents: Incomplete

def _closestSize(size): ...
def _pilFontPath(face, size, bold: int = ...): ...
def _matchingFontPath(font): ...
def _pilFont(font): ...

class PILCanvas(Canvas):
    _image: Incomplete
    _pen: Incomplete
    def __init__(self, size=..., name: str = ...) -> None: ...
    def __setattr__(self, attribute, value) -> None: ...
    _color: Incomplete
    def _setColor(self, c) -> None: ...
    _font: Incomplete
    def _setFont(self, font) -> None: ...
    def getImage(self): ...
    def save(
        self, file: Incomplete | None = ..., format: Incomplete | None = ...
    ) -> None: ...
    def clear(self) -> None: ...
    def stringWidth(self, s, font: Incomplete | None = ...): ...
    def fontAscent(self, font: Incomplete | None = ...): ...
    def fontDescent(self, font: Incomplete | None = ...): ...
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
        fillColor: Incomplete | None = ...,
        closed: int = ...,
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
    ): ...
    def drawImage(
        self,
        image,
        x1,
        y1,
        x2: Incomplete | None = ...,
        y2: Incomplete | None = ...,
        **kwargs
    ) -> None: ...

def test(): ...
def testit(canvas, s, x, y, font: Incomplete | None = ...) -> None: ...
def test2() -> None: ...
