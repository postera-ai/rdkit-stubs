from typing import Any, ClassVar

class MolCatalog:
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def AddEdge(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def AddEntry(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetBitDescription(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetBitEntryId(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetEntryBitId(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetEntryDescription(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetEntryDownIds(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetFPLength(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def GetNumEntries(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def Serialize(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def __getinitargs__(cls) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class MolCatalogEntry:
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetDescription(cls, RDKit) -> Any: ...
    @classmethod
    def GetMol(cls, RDKit) -> Any: ...
    @classmethod
    def GetOrder(cls, RDKit) -> Any: ...
    @classmethod
    def SetDescription(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def SetMol(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def SetOrder(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def __getinitargs__(cls, RDKit) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

def CreateMolCatalog() -> Any: ...
