from _typeshed import Incomplete
from rdkit.Chem.Pharm2D import Matcher as Matcher, SigFactory as SigFactory

class Generator:
    sigFactory: Incomplete
    mol: Incomplete
    dMat: Incomplete
    bits: Incomplete
    pattMatches: Incomplete
    def __init__(
        self, sigFactory, mol, dMat: Incomplete | None = ..., bitCache: bool = ...
    ) -> None: ...
    def GetBit(self, idx): ...
    def __len__(self) -> int: ...
    def __getitem__(self, itm): ...
