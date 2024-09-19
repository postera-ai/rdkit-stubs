from typing import Any

class EHTResults:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetAtomicCharges(cls, RDKit) -> Any: ...
    @classmethod
    def GetHamiltonian(cls, RDKit) -> Any: ...
    @classmethod
    def GetOrbitalEnergies(cls, RDKit) -> Any: ...
    @classmethod
    def GetOverlapMatrix(cls, RDKit) -> Any: ...
    @classmethod
    def GetReducedChargeMatrix(cls, RDKit) -> Any: ...
    @classmethod
    def GetReducedOverlapPopulationMatrix(cls, RDKit) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...
    @property
    def fermiEnergy(self) -> Any: ...
    @property
    def numElectrons(self) -> Any: ...
    @property
    def numOrbitals(self) -> Any: ...
    @property
    def totalEnergy(self) -> Any: ...

def RunMol(RDKit) -> Any: ...