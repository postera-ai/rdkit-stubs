from _typeshed import Incomplete
from rdkit.Chem.Draw.canvasbase import CanvasBase as CanvasBase

class Canvas(CanvasBase):
    size: Incomplete
    qsize: Incomplete
    pixmap: Incomplete
    painter: Incomplete
    def __init__(self, size) -> None: ...
    def addCanvasLine(
        self, p1, p2, color=..., color2: Incomplete | None = ..., **kwargs
    ) -> None: ...
    def addCanvasText(self, text, pos, font, color=..., **kwargs): ...
    def addCanvasPolygon(
        self, ps, color=..., fill: bool = ..., stroke: bool = ..., **kwargs
    ) -> None: ...
    def addCanvasDashedWedge(
        self, p1, p2, p3, dash=..., color=..., color2: Incomplete | None = ..., **kwargs
    ) -> None: ...
    def flush(self) -> None: ...
