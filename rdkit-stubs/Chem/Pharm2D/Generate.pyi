from _typeshed import Incomplete
from rdkit.Chem.Pharm2D import SigFactory as SigFactory, Utils as Utils
from rdkit.RDLogger import logger as logger

_verbose: int

def _ShortestPathsMatch(match, featureSet, sig, dMat, sigFactory): ...
def Gen2DFingerprint(
    mol,
    sigFactory,
    perms: Incomplete | None = ...,
    dMat: Incomplete | None = ...,
    bitInfo: Incomplete | None = ...,
): ...
