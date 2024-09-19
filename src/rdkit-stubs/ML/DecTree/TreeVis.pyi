from _typeshed import Incomplete

class VisOpts:
    circRad: int
    minCircRad: int
    maxCircRad: int
    circColor: Incomplete
    terminalEmptyColor: Incomplete
    terminalOnColor: Incomplete
    terminalOffColor: Incomplete
    outlineColor: Incomplete
    lineColor: Incomplete
    lineWidth: int
    horizOffset: int
    vertOffset: int
    labelFont: Incomplete
    highlightColor: Incomplete
    highlightWidth: int

visOpts: Incomplete

def CalcTreeNodeSizes(node) -> None: ...
def _ExampleCounter(node, min, max): ...
def _ApplyNodeScales(node, min, max) -> None: ...
def SetNodeScales(node) -> None: ...
def DrawTreeNode(
    node, loc, canvas, nRes: int = ..., scaleLeaves: bool = ..., showPurity: bool = ...
) -> None: ...
def CalcTreeWidth(tree): ...
def DrawTree(
    tree,
    canvas,
    nRes: int = ...,
    scaleLeaves: bool = ...,
    allowShrink: bool = ...,
    showPurity: bool = ...,
) -> None: ...
def ResetTree(tree) -> None: ...
def _simpleTest(canv) -> None: ...
