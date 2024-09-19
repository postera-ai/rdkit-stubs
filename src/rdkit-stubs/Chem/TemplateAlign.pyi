from _typeshed import Incomplete
from rdkit import Chem as Chem, Geometry as Geometry
from rdkit.Chem import rdDepictor as rdDepictor

def AlignMolToTemplate2D(
    mol,
    template,
    match: Incomplete | None = ...,
    clearConfs: bool = ...,
    templateConfId: int = ...,
): ...
def _test(): ...
