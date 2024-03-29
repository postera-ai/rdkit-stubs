from _typeshed import Incomplete
from rdkit import DataStructs as DataStructs
from rdkit.DataStructs import TopNContainer as TopNContainer

class SimilarityScreener:
    metric: Incomplete
    dataSource: Incomplete
    fingerprinter: Incomplete
    probe: Incomplete
    def __init__(
        self,
        probe: Incomplete | None = ...,
        metric: Incomplete | None = ...,
        dataSource: Incomplete | None = ...,
        fingerprinter: Incomplete | None = ...,
    ) -> None: ...
    def Reset(self) -> None: ...
    def SetProbe(self, probeFingerprint) -> None: ...
    def GetSingleFingerprint(self, probe): ...

class ThresholdScreener(SimilarityScreener):
    threshold: Incomplete
    dataIter: Incomplete
    def __init__(self, threshold, **kwargs) -> None: ...
    def _nextMatch(self): ...
    def Reset(self) -> None: ...
    def __iter__(self): ...
    def next(self): ...
    __next__: Incomplete

class TopNScreener(SimilarityScreener):
    numToGet: Incomplete
    topN: Incomplete
    _pos: int
    def __init__(self, num, **kwargs) -> None: ...
    def Reset(self) -> None: ...
    def __iter__(self): ...
    def next(self): ...
    __next__: Incomplete
    def _initTopN(self) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, idx): ...
