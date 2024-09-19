from _typeshed import Incomplete
from rdkit import RDConfig as RDConfig
from rdkit.Chem.Draw.canvasbase import CanvasBase as CanvasBase

faceMap: Incomplete

def convertColor(color): ...

class Canvas(CanvasBase):
    fontScale: float
    image: Incomplete
    draw: Incomplete
    size: Incomplete
    drawType: Incomplete
    fileName: Incomplete
    def __init__(
        self,
        img: Incomplete | None = ...,
        imageType: Incomplete | None = ...,
        fileName: Incomplete | None = ...,
        size: Incomplete | None = ...,
    ) -> None: ...
    def _doLine(self, p1, p2, pen, **kwargs) -> None: ...
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
