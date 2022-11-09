from _typeshed import Incomplete
from rdkit import Chem as Chem

log: Incomplete

class MetalDisconnector:
    _metal_nof: Incomplete
    _metal_non: Incomplete
    def __init__(self) -> None: ...
    def __call__(self, mol): ...
    def disconnect(self, mol): ...
