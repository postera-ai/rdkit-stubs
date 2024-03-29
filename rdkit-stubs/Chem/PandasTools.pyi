from _typeshed import Incomplete
from rdkit import Chem as Chem, DataStructs as DataStructs
from rdkit.Chem import (
    AllChem as AllChem,
    Draw as Draw,
    SDWriter as SDWriter,
    rdchem as rdchem,
)
from rdkit.Chem.Draw.IPythonConsole import InteractiveRenderer as InteractiveRenderer
from rdkit.Chem.Scaffolds import MurckoScaffold as MurckoScaffold

log: Incomplete

def _getPandasVersion(): ...

pandasVersion: Incomplete
defPandasRendering: Incomplete
defPandasRepr: Incomplete
highlightSubstructures: bool
molRepresentation: str
molSize: Incomplete

def getAdjustmentAttr(): ...
def _patched_HTMLFormatter_write_cell(self, s, *args, **kwargs): ...
def _patched_get_adjustment(): ...
def patchPandasrepr(self, **kwargs): ...
def patchPandasHTMLrepr(self, **kwargs): ...
def is_molecule_image(s): ...

class RenderMoleculeAdjustment:
    inner_adjustment: Incomplete
    def __init__(self, inner_adjustment) -> None: ...
    def len(self, text): ...
    def justify(self, texts, max_len, mode: str = ...): ...
    def adjoin(self, space, *lists, **kwargs): ...

def _get_image(x): ...
def _fingerprinter(x, y): ...
def _molge(x, y): ...
def PrintAsBase64PNGString(x, renderer: Incomplete | None = ...): ...
def PrintDefaultMolRep(x): ...
def _MolPlusFingerprint(m): ...
def RenderImagesInAllDataFrames(images: bool = ...) -> None: ...
def AddMoleculeColumnToFrame(
    frame, smilesCol: str = ..., molCol: str = ..., includeFingerprints: bool = ...
): ...
def ChangeMoleculeRendering(
    frame: Incomplete | None = ..., renderer: str = ...
) -> None: ...
def LoadSDF(
    filename,
    idName: str = ...,
    molColName: str = ...,
    includeFingerprints: bool = ...,
    isomericSmiles: bool = ...,
    smilesName: Incomplete | None = ...,
    embedProps: bool = ...,
    removeHs: bool = ...,
    strictParsing: bool = ...,
): ...
def WriteSDF(
    df,
    out,
    molColName: str = ...,
    idName: Incomplete | None = ...,
    properties: Incomplete | None = ...,
    allNumeric: bool = ...,
) -> None: ...

_saltRemover: Incomplete

def RemoveSaltsFromFrame(frame, molCol: str = ...): ...
def SaveSMILESFromFrame(
    frame, outFile, molCol: str = ..., NamesCol: str = ..., isomericSmiles: bool = ...
) -> None: ...
def SaveXlsxFromFrame(frame, outFile, molCol: str = ..., size=...) -> None: ...
def FrameToGridImage(
    frame, column: str = ..., legendsCol: Incomplete | None = ..., **kwargs
): ...
def AddMurckoToFrame(
    frame, molCol: str = ..., MurckoCol: str = ..., Generic: bool = ...
): ...
def AlignMol(mol, scaffold): ...
def AlignToScaffold(frame, molCol: str = ..., scaffoldCol: str = ...): ...
def RGroupDecompositionToFrame(
    groups, mols, include_core: bool = ..., redraw_sidechains: bool = ...
): ...
def InstallPandasTools() -> None: ...
def UninstallPandasTools() -> None: ...

_originalSettings: Incomplete

def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
