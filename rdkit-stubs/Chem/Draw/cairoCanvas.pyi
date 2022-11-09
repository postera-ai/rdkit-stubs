from _typeshed import Incomplete
from rdkit.Chem.Draw.canvasbase import CanvasBase as CanvasBase

have_cairocffi: bool
have_pango: bool
ffi: Incomplete
defaultLibs: Incomplete
envVar: Incomplete
envVarSet: bool
libName: Incomplete
libPath: Incomplete
importError: bool
scriptPattern: Incomplete

class Canvas(CanvasBase):
    image: Incomplete
    imageType: Incomplete
    ctx: Incomplete
    size: Incomplete
    surface: Incomplete
    fileName: Incomplete
    def __init__(
        self,
        image: Incomplete | None = ...,
        size: Incomplete | None = ...,
        ctx: Incomplete | None = ...,
        imageType: Incomplete | None = ...,
        fileName: Incomplete | None = ...,
    ) -> None: ...
    def flush(self): ...
    def _doLine(self, p1, p2, **kwargs) -> None: ...
    def addCanvasLine(
        self, p1, p2, color=..., color2: Incomplete | None = ..., **kwargs
    ) -> None: ...
    def _addCanvasText1(self, text, pos, font, color=..., **kwargs): ...
    def _addCanvasText2(self, text, pos, font, color=..., **kwargs): ...
    def addCanvasText(self, text, pos, font, color=..., **kwargs): ...
    def addCanvasPolygon(
        self, ps, color=..., fill: bool = ..., stroke: bool = ..., **kwargs
    ) -> None: ...
    def addCanvasDashedWedge(
        self, p1, p2, p3, dash=..., color=..., color2: Incomplete | None = ..., **kwargs
    ) -> None: ...
    def addCircle(
        self,
        center,
        radius,
        color=...,
        fill: bool = ...,
        stroke: bool = ...,
        alpha: float = ...,
        **kwargs
    ) -> None: ...
