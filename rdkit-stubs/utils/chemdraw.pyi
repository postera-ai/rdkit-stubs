from _typeshed import Incomplete

cdxModule: Incomplete
_cdxVersion: int
cdApp: Incomplete
theDoc: Incomplete
theObjs: Incomplete
selectItem: Incomplete
cleanItem: Incomplete
centerItem: Incomplete

def StartChemDraw(
    visible: bool = ..., openDoc: bool = ..., showDoc: bool = ...
) -> None: ...
def ReactivateChemDraw(openDoc: bool = ..., showDoc: bool = ...) -> None: ...
def CDXConvert(inData, inFormat, outFormat): ...
def CDXClean(inData, inFormat, outFormat): ...
def CDXDisplay(inData, inFormat: str = ..., clear: int = ...) -> None: ...
def CDXGrab(outFormat: str = ...): ...
def CloseChemdraw() -> None: ...
def Exit() -> None: ...
def SaveChemDrawDoc(fileName: str = ...) -> None: ...
def CloseChemDrawDoc() -> None: ...
def RaiseWindowNamed(nameRe): ...
def RaiseChemDraw() -> None: ...
def SmilesToPilImage(smilesStr): ...
def MolToPilImage(dataStr, inFormat: str = ..., outFormat: str = ...): ...

c3dApp: Incomplete

def StartChem3D(visible: int = ...) -> None: ...
def CloseChem3D() -> None: ...

availChem3DProps: Incomplete

def Add3DCoordsToMol(data, format, props=...): ...
def OptimizeSDFile(
    inFileName, outFileName, problemFileName: str = ..., restartEvery: int = ...
) -> None: ...
