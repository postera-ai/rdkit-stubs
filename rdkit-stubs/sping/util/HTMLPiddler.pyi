from types import *
from _typeshed import Incomplete

TRACE: int

class HTMLPiddler:
    html: Incomplete
    start: Incomplete
    xLimits: Incomplete
    font: Incomplete
    color: Incomplete
    def __init__(
        self,
        html: str = ...,
        start=...,
        xLimits=...,
        font: Incomplete | None = ...,
        color: Incomplete | None = ...,
    ) -> None: ...
    def renderOn(self, aPiddleCanvas) -> None: ...

DEMO_HTML: str

def demoPDF(html) -> None: ...
def demoPIL(html) -> None: ...
def demoTK(html) -> None: ...
def demoWX(html) -> None: ...
def demo(html=...) -> None: ...
