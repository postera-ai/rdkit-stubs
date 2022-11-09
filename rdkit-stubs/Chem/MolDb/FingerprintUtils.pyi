from _typeshed import Incomplete
from rdkit import Chem as Chem, DataStructs as DataStructs

similarityMethods: Incomplete
supportedSimilarityMethods: Incomplete

class LayeredOptions:
    loadLayerFlags: int
    searchLayerFlags: int
    minPath: int
    maxPath: int
    fpSize: int
    wordSize: int
    nWords: Incomplete
    @staticmethod
    def GetFingerprint(mol, query: bool = ...): ...
    @staticmethod
    def GetWords(mol, query: bool = ...): ...
    @staticmethod
    def GetQueryText(mol, query: bool = ...): ...

def BuildSigFactory(
    options: Incomplete | None = ...,
    fdefFile: Incomplete | None = ...,
    bins=...,
    skipFeats=...,
): ...
def BuildAtomPairFP(mol): ...
def BuildTorsionsFP(mol): ...
def BuildRDKitFP(mol): ...
def BuildPharm2DFP(mol): ...
def BuildMorganFP(mol): ...
def BuildAvalonFP(mol, smiles: Incomplete | None = ...): ...
def DepickleFP(pkl, similarityMethod): ...
