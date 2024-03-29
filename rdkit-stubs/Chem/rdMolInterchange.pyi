from typing import Any, ClassVar

class JSONParseParameters:
    __instance_size__: ClassVar[int] = ...
    parseConformers: Any
    parseProperties: Any
    setAromaticBonds: Any
    strictValenceCheck: Any
    useHCounts: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

def JSONToMols(*args, **kwargs) -> Any: ...
def MolToJSON(RDKit) -> Any: ...
def MolsToJSON(boost) -> Any: ...
