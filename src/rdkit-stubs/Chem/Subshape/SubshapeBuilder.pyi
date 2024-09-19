from _typeshed import Incomplete
from rdkit import Chem as Chem, Geometry as Geometry
from rdkit.Chem import AllChem as AllChem
from rdkit.Chem.Subshape import (
    BuilderUtils as BuilderUtils,
    SubshapeObjects as SubshapeObjects,
)

class SubshapeCombineOperations:
    UNION: int
    SUM: int
    INTERSECT: int

class SubshapeBuilder:
    gridDims: Incomplete
    gridSpacing: float
    winRad: float
    nbrCount: int
    terminalPtRadScale: float
    fraction: float
    stepSize: float
    featFactory: Incomplete
    def SampleSubshape(self, subshape1, newSpacing): ...
    def GenerateSubshapeShape(
        self, cmpd, confId: int = ..., addSkeleton: bool = ..., **kwargs
    ): ...
    def __call__(self, cmpd, **kwargs): ...
    def GenerateSubshapeSkeleton(
        self,
        shape,
        conf: Incomplete | None = ...,
        terminalPtsOnly: bool = ...,
        skelFromConf: bool = ...,
    ) -> None: ...
    def CombineSubshapes(self, subshape1, subshape2, operation=...): ...
