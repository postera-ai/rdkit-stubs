from math import *
from _typeshed import Incomplete
from rdkit.sping import pid as pid

def _ColorToQt(color): ...

class QCanvasRotText:
    _angle: Incomplete
    def __init__(self, txt, canvas, angle: int = ...) -> None: ...
    def draw(self, qP) -> None: ...

class QtCanvas(pid.Canvas):
    size: Incomplete
    _scene: Incomplete
    _brush: Incomplete
    _pen: Incomplete
    _font: Incomplete
    objs: Incomplete
    nObjs: int
    def __init__(
        self, scene, size: Incomplete | None = ..., name: str = ...
    ) -> None: ...
    def _initOutput(self) -> None: ...
    def _adjustFont(self, font) -> None: ...
    def clear(self) -> None: ...
    def flush(self) -> None: ...
    def save(
        self, file: Incomplete | None = ..., format: Incomplete | None = ...
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
    def stringBox(self, s, font: Incomplete | None = ...): ...
    def stringWidth(self, s, font: Incomplete | None = ...): ...
    def fontAscent(self, font: Incomplete | None = ...): ...
    def fontDescent(self, font: Incomplete | None = ...): ...

def test(canvas): ...
def dashtest(canvas): ...
