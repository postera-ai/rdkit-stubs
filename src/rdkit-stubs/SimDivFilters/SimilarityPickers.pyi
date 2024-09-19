from _typeshed import Incomplete
from rdkit import DataStructs as DataStructs
from rdkit.DataStructs.TopNContainer import TopNContainer as TopNContainer

class GenericPicker:
    _picks: Incomplete
    def MakePicks(self, force: bool = ...) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, which): ...

class TopNOverallPicker(GenericPicker):
    numToPick: Incomplete
    probes: Incomplete
    data: Incomplete
    simMetric: Incomplete
    _picks: Incomplete
    def __init__(
        self,
        numToPick: int = ...,
        probeFps: Incomplete | None = ...,
        dataSet: Incomplete | None = ...,
        simMetric=...,
    ) -> None: ...
    def MakePicks(self, force: bool = ...) -> None: ...

class SpreadPicker(GenericPicker):
    numToPick: Incomplete
    probes: Incomplete
    data: Incomplete
    simMetric: Incomplete
    expectPickles: Incomplete
    onlyNames: Incomplete
    _picks: Incomplete
    def __init__(
        self,
        numToPick: int = ...,
        probeFps: Incomplete | None = ...,
        dataSet: Incomplete | None = ...,
        simMetric=...,
        expectPickles: bool = ...,
        onlyNames: bool = ...,
    ) -> None: ...
    def MakePicks(self, force: bool = ..., silent: bool = ...) -> None: ...

def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
