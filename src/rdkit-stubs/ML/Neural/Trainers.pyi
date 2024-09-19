from _typeshed import Incomplete

class Trainer: ...

class BackProp(Trainer):
    oldDeltaW: Incomplete
    def StepUpdate(self, example, net, resVect: Incomplete | None = ...): ...
    def TrainOnLine(
        self,
        examples,
        net,
        maxIts: int = ...,
        errTol: float = ...,
        useAvgErr: int = ...,
        silent: int = ...,
    ) -> None: ...
    speed: Incomplete
    momentum: Incomplete
    def __init__(self, speed: float = ..., momentum: float = ...) -> None: ...
