from _typeshed import Incomplete
from rdkit import Chem as Chem

def Convert(
    suppl,
    outFile,
    keyCol: Incomplete | None = ...,
    stopAfter: int = ...,
    includeChirality: bool = ...,
    smilesFrom: str = ...,
) -> None: ...
def initParser(): ...
def existingFile(filename): ...
def main() -> None: ...
