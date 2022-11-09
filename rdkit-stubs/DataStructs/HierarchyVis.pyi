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
    topMargin: int
    labelFont: Incomplete
    highlightColor: Incomplete
    highlightWidth: int

visOpts: Incomplete

def GetMinCanvasSize(adjList, levelList): ...
def DrawHierarchy(
    adjList,
    levelList,
    canvas,
    entryColors: Incomplete | None = ...,
    bitIds: Incomplete | None = ...,
    minLevel: int = ...,
    maxLevel: float = ...,
): ...
