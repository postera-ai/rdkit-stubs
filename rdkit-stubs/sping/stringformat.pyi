from _typeshed import Incomplete
from rdkit.sping.pid import Font as Font

sizedelta: int
subFraction: float
superFraction: float
greekchars: Incomplete

class StringSegment:
    super: int
    sub: int
    bold: int
    italic: int
    underline: int
    s: str
    width: int
    greek: int
    def __init__(self) -> None: ...
    def calcNewFont(self, font): ...
    def calcNewY(self, font, y): ...
    def dump(self) -> None: ...

class StringFormatter:
    bold: int
    def start_b(self, attributes) -> None: ...
    def end_b(self) -> None: ...
    italic: int
    def start_i(self, attributes) -> None: ...
    def end_i(self) -> None: ...
    underline: int
    def start_u(self, attributes) -> None: ...
    def end_u(self) -> None: ...
    super: int
    def start_super(self, attributes) -> None: ...
    def end_super(self) -> None: ...
    sub: int
    def start_sub(self, attributes) -> None: ...
    def end_sub(self) -> None: ...
    greek: int
    def start_greek(self, attributes, letter) -> None: ...
    def end_greek(self) -> None: ...
    segmentlist: Incomplete
    elements: Incomplete
    def __init__(self) -> None: ...
    def handle_data(self, data) -> None: ...
    def parseSegments(self, s): ...

def fontHeight(canvas, font: Incomplete | None = ...): ...
def fontAscent(canvas, font: Incomplete | None = ...): ...
def fontDescent(canvas, font: Incomplete | None = ...): ...
def stringWidth(canvas, s, font: Incomplete | None = ...): ...
def rotateXY(x, y, theta): ...
def drawString(
    canvas,
    s,
    x,
    y,
    font: Incomplete | None = ...,
    color: Incomplete | None = ...,
    angle: int = ...,
) -> None: ...
def test1() -> None: ...
def test2() -> None: ...
def allTagCombos(
    canvas,
    x,
    y,
    font: Incomplete | None = ...,
    color: Incomplete | None = ...,
    angle: int = ...,
): ...
def stringformatTest() -> None: ...
