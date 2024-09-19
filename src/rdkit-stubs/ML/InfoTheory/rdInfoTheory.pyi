from typing import Any, ClassVar

BIASCHISQUARE: InfoType
BIASENTROPY: InfoType
CHISQUARE: InfoType
ENTROPY: InfoType

class BitCorrMatGenerator:
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def CollectVotes(cls, RDInfoTheory, boost) -> Any: ...
    @classmethod
    def GetCorrMatrix(cls, RDInfoTheory) -> Any: ...
    @classmethod
    def SetBitList(cls, RDInfoTheory, boost) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class InfoBitRanker:
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def AccumulateVotes(cls, RDInfoTheory, boost, int) -> Any: ...
    @classmethod
    def GetTopN(cls, RDInfoTheory, int) -> Any: ...
    @classmethod
    def SetBiasList(cls, RDInfoTheory, boost) -> Any: ...
    @classmethod
    def SetMaskBits(cls, RDInfoTheory, boost) -> Any: ...
    @classmethod
    def Tester(cls, RDInfoTheory, boost) -> Any: ...
    @classmethod
    def WriteTopBitsToFile(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class InfoType:
    BIASCHISQUARE: ClassVar[InfoType] = ...
    BIASENTROPY: ClassVar[InfoType] = ...
    CHISQUARE: ClassVar[InfoType] = ...
    ENTROPY: ClassVar[InfoType] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...

def ChiSquare(boost) -> Any: ...
def InfoEntropy(boost) -> Any: ...
def InfoGain(boost) -> Any: ...