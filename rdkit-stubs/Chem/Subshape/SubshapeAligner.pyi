from _typeshed import Incomplete
from collections.abc import Generator
from rdkit import Chem as Chem, Geometry as Geometry, RDLogger as RDLogger
from rdkit.Chem.Subshape import SubshapeObjects as SubshapeObjects

logger: Incomplete

class SubshapeAlignment:
    transform: Incomplete
    triangleSSD: Incomplete
    targetTri: Incomplete
    queryTri: Incomplete
    alignedConfId: int
    dirMatch: float
    shapeDist: float

def _getAllTriangles(
    pts, orderedTraversal: bool = ...
) -> Generator[Incomplete, None, None]: ...

class SubshapeDistanceMetric:
    TANIMOTO: int
    PROTRUDE: int

def GetShapeShapeDistance(s1, s2, distMetric): ...
def ClusterAlignments(
    mol,
    alignments,
    builder,
    neighborTol: float = ...,
    distMetric=...,
    tempConfId: int = ...,
): ...
def TransformMol(mol, tform, confId: int = ..., newConfId: int = ...) -> None: ...

class SubshapeAligner:
    triangleRMSTol: float
    distMetric: Incomplete
    shapeDistTol: float
    numFeatThresh: int
    dirThresh: float
    edgeTol: float
    coarseGridToleranceMult: float
    medGridToleranceMult: float
    def GetTriangleMatches(
        self, target, query
    ) -> Generator[Incomplete, None, None]: ...
    def _checkMatchFeatures(self, targetPts, queryPts, alignment): ...
    def PruneMatchesUsingFeatures(
        self, target, query, alignments, pruneStats: Incomplete | None = ...
    ) -> None: ...
    def _checkMatchDirections(self, targetPts, queryPts, alignment): ...
    def PruneMatchesUsingDirection(
        self, target, query, alignments, pruneStats: Incomplete | None = ...
    ) -> None: ...
    def _addCoarseAndMediumGrids(self, mol, tgt, confId, builder) -> None: ...
    def _checkMatchShape(
        self,
        targetMol,
        target,
        queryMol,
        query,
        alignment,
        builder,
        targetConf,
        queryConf,
        pruneStats: Incomplete | None = ...,
        tConfId: int = ...,
    ): ...
    def PruneMatchesUsingShape(
        self,
        targetMol,
        target,
        queryMol,
        query,
        builder,
        alignments,
        tgtConf: int = ...,
        queryConf: int = ...,
        pruneStats: Incomplete | None = ...,
    ) -> None: ...
    def GetSubshapeAlignments(
        self,
        targetMol,
        target,
        queryMol,
        query,
        builder,
        tgtConf: int = ...,
        queryConf: int = ...,
        pruneStats: Incomplete | None = ...,
    ): ...
    def __call__(
        self,
        targetMol,
        target,
        queryMol,
        query,
        builder,
        tgtConf: int = ...,
        queryConf: int = ...,
        pruneStats: Incomplete | None = ...,
    ) -> Generator[Incomplete, None, None]: ...
