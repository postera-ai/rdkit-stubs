from _typeshed import Incomplete
from rdkit import Chem as Chem, RDLogger as RDLogger
from rdkit.Chem import ChemicalFeatures as ChemicalFeatures

logger: Incomplete
splitExpr: Incomplete

def GetAtomFeatInfo(factory, mol): ...
def initParser(): ...

_splashMessage: str

def existingFile(filename): ...
def processArgs(args, parser) -> None: ...
def main() -> None: ...
