from rdkit.Chem.FeatMaps import FeatMaps as FeatMaps

class MergeMethod:
    WeightedAverage: int
    Average: int
    UseLarger: int
    @classmethod
    def valid(cls, mergeMethod) -> None: ...

class MergeMetric:
    NoMerge: int
    Distance: int
    Overlap: int
    @classmethod
    def valid(cls, mergeMetric) -> None: ...

class DirMergeMode:
    NoMerge: int
    Sum: int
    @classmethod
    def valid(cls, dirMergeMode) -> None: ...

def __copyAll(res, fm1, fm2) -> None: ...
def GetFeatFeatDistMatrix(fm, mergeMetric, mergeTol, dirMergeMode, compatFunc): ...
def familiesMatch(f1, f2): ...
def feq(v1, v2, tol: float = ...): ...
def MergeFeatPoints(
    fm,
    mergeMetric=...,
    mergeTol: float = ...,
    dirMergeMode=...,
    mergeMethod=...,
    compatFunc=...,
): ...
def CombineFeatMaps(
    fm1, fm2, mergeMetric=..., mergeTol: float = ..., dirMergeMode=...
): ...
