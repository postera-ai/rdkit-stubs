from _typeshed import Incomplete
from rdkit import Chem as Chem, RDConfig as RDConfig
from rdkit.Chem import AllChem as AllChem, rdChemReactions as rdChemReactions

def PreprocessReaction(
    reaction, funcGroupFilename: Incomplete | None = ..., propName: str = ...
): ...
def EnumerateReaction(
    reaction,
    bbLists,
    uniqueProductsOnly: bool = ...,
    funcGroupFilename=...,
    propName: str = ...,
): ...
def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
