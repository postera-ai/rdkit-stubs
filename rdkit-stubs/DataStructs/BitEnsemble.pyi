from _typeshed import Incomplete

class BitEnsemble:
    _bits: Incomplete
    def __init__(self, bits: Incomplete | None = ...) -> None: ...
    def SetBits(self, bits) -> None: ...
    def AddBit(self, bit) -> None: ...
    def GetBits(self): ...
    def GetNumBits(self): ...
    def ScoreWithOnBits(self, other): ...
    def ScoreWithIndex(self, other): ...
