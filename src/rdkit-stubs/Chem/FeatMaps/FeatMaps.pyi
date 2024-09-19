from _typeshed import Incomplete
from collections.abc import Generator
from rdkit.Chem.FeatMaps.FeatMapPoint import FeatMapPoint as FeatMapPoint

class FeatMapScoreMode:
    All: int
    Closest: int
    Best: int

class FeatDirScoreMode:
    Ignore: int
    DotFullRange: int
    DotPosRange: int

class FeatMapParams:
    radius: float
    width: float

    class FeatProfile:
        Gaussian: int
        Triangle: int
        Box: int
    featProfile: Incomplete

class FeatMap:
    dirScoreMode: Incomplete
    scoreMode: Incomplete
    params: Incomplete
    def __init__(
        self,
        params: Incomplete | None = ...,
        feats: Incomplete | None = ...,
        weights: Incomplete | None = ...,
    ) -> None: ...
    _feats: Incomplete
    def _initializeFeats(self, feats, weights) -> None: ...
    def AddFeature(self, feat, weight: Incomplete | None = ...) -> None: ...
    def AddFeatPoint(self, featPt) -> None: ...
    def GetFeatures(self): ...
    def GetNumFeatures(self): ...
    def GetFeature(self, i): ...
    def DropFeature(self, i) -> None: ...
    def _loopOverMatchingFeats(self, oFeat) -> Generator[Incomplete, None, None]: ...
    def GetFeatFeatScore(self, feat1, feat2, typeMatch: bool = ...): ...
    def ScoreFeats(
        self,
        featsToScore,
        mapScoreVect: Incomplete | None = ...,
        featsScoreVect: Incomplete | None = ...,
        featsToFeatMapIdx: Incomplete | None = ...,
    ): ...
    def __str__(self): ...
