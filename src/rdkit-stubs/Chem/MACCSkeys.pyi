from _typeshed import Incomplete
from rdkit import Chem as Chem, DataStructs as DataStructs
from rdkit.Chem import rdMolDescriptors as rdMolDescriptors

smartsPatts: Incomplete
maccsKeys: Incomplete

def _InitKeys(keyList, keyDict) -> None: ...
def _pyGenMACCSKeys(mol, **kwargs): ...

GenMACCSKeys: Incomplete
FingerprintMol: Incomplete

def _test(): ...
