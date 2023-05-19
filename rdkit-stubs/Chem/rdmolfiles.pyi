from types import TracebackType
from typing import IO, Any, ClassVar, Iterable, List, Optional, TextIO, Tuple, Union, overload

from rdkit.Chem import Mol
from rdkit.Chem.rdMolDescriptors import AtomPairsParameters


class CXSmilesFields:
    CX_ALL: ClassVar[CXSmilesFields] = ...
    CX_ATOM_LABELS: ClassVar[CXSmilesFields] = ...
    CX_ATOM_PROPS: ClassVar[CXSmilesFields] = ...
    CX_COORDS: ClassVar[CXSmilesFields] = ...
    CX_ENHANCEDSTEREO: ClassVar[CXSmilesFields] = ...
    CX_LINKNODES: ClassVar[CXSmilesFields] = ...
    CX_MOLFILE_VALUES: ClassVar[CXSmilesFields] = ...
    CX_NONE: ClassVar[CXSmilesFields] = ...
    CX_POLYMER: ClassVar[CXSmilesFields] = ...
    CX_RADICALS: ClassVar[CXSmilesFields] = ...
    CX_SGROUPS: ClassVar[CXSmilesFields] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...

class ForwardSDMolSupplier:
    @overload
    def __init__(
        self,
        fileobj: IO,
        sanitize: bool = ...,
        removeHs: bool = ...,
        strictParsing: bool = ...,
    ): ...
    @overload
    def __init__(
        self,
        filename: str,
        sanitize: bool = ...,
        removeHs: bool = ...,
        strictParsing: bool = ...,
    ): ...
    def GetEOFHitOnRead(self) -> bool: ...
    def GetProcessPropertyLists(self) -> bool: ...
    def SetProcessPropertyLists(self, arg2: bool): ...
    def atEnd(self) -> bool: ...
    def __enter__(self) -> "ForwardSDMolSupplier": ...
    def __exit__(
        self,
        type: type[BaseException],
        value: BaseException,
        traceback: TracebackType,
    ) -> Optional[bool]: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Optional[Mol]: ...
    def __reduce__(self) -> Any: ...

class MaeMolSupplier:
    @overload
    def __init__(self, fileobj: IO, sanitize: bool = ..., removeHs: bool = ...): ...
    @overload
    def __init__(self, filename: str, sanitize: bool = ..., removeHs: bool = ...): ...
    def atEnd(self) -> bool: ...
    def __enter__(self) -> "MaeMolSupplier": ...
    def __exit__(
        self,
        type: type[BaseException],
        value: BaseException,
        traceback: TracebackType,
    ) -> Optional[bool]: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Optional[Mol]: ...
    def __reduce__(self) -> Any: ...

class MultithreadedSDMolSupplier:
    __instance_size__: ClassVar[int] = ...
    def __init__(
        self,
        fileName: str,
        sanitize: bool = ...,
        removeHs: bool = ...,
        strictParsing: bool = True,
        numWriterThreads: int = ...,
        sizeInputQueue: int = ...,
        sizeOutputQueue: int = ...,
    ): ...
    def GetLastItemText(self) -> str: ...
    def GetLastRecordId(self) -> int: ...
    def GetProcessPropertyLists(self) -> bool: ...
    def SetProcessPropertyLists(self, arg2: bool): ...
    def atEnd(self) -> bool: ...
    def __enter__(self) -> "MultithreadedSDMolSupplier": ...
    def __exit__(
        self,
        type: type[BaseException],
        value: BaseException,
        traceback: TracebackType,
    ) -> Optional[bool]: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Optional[Mol]: ...
    def __reduce__(self) -> Any: ...

class MultithreadedSmilesMolSupplier:
    __instance_size__: ClassVar[int] = ...
    def __init__(
        self,
        fileName: str,
        delimiter: str = ...,
        smilesColumn: int = ...,
        nameColumn: int = ...,
        titleLine: bool = ...,
        sanitize: bool = ...,
        numWriterThreads: int = ...,
        sizeInputQueue: int = ...,
        sizeOutputQueue: int = ...,
    ): ...
    def GetLastItemText(self) -> str: ...
    def GetLastRecordId(self) -> int: ...
    def atEnd(self) -> bool: ...
    def __enter__(self) -> "MultithreadedSmilesMolSupplier": ...
    def __exit__(
        self,
        type: type[BaseException],
        value: BaseException,
        traceback: TracebackType,
    ) -> Optional[bool]: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Optional[Mol]: ...
    def __reduce__(self) -> Any: ...

class PDBWriter:
    def __init__(self, fileName: str, flavor: int = ...): ...
    def NumMols(self) -> int: ...
    def close(self): ...
    def flush(self): ...
    def write(self, mol: Mol, confId: int = ...): ...
    def __enter__(self) -> "PDBWriter": ...
    def __exit__(
        self,
        type: type[BaseException],
        value: BaseException,
        traceback: TracebackType,
    ) -> Optional[bool]: ...
    def __reduce__(self) -> Any: ...

class SDMolSupplier:
    __instance_size__: ClassVar[int] = ...
    def __init__(
        self,
        fileName: str,
        sanitize: bool = ...,
        removeHs: bool = ...,
        strictParsing: bool = ...,
    ): ...
    def GetItemText(self, index: int) -> str: ...
    def GetProcessPropertyLists(self) -> bool: ...
    def SetData(
        self,
        data: str,
        sanitize: bool = ...,
        removeHs: bool = ...,
        strictParsing: bool = ...,
    ): ...
    def SetProcessPropertyLists(self, arg1: bool): ...
    def atEnd(self) -> bool: ...
    def reset(self) -> Any: ...
    def __enter__(self) -> "SDMolSupplier": ...
    def __exit__(
        self,
        type: type[BaseException],
        value: BaseException,
        traceback: TracebackType,
    ) -> Optional[bool]: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Optional[Mol]: ...
    def __reduce__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __getitem__(self, int) -> Mol: ...

class SDWriter:
    @overload
    def __init__(self, fileName: str): ...
    @overload
    def __init__(self, _: TextIO): ...
    def GetForceV3000(self) -> bool: ...
    def GetKekulize(self) -> bool: ...
    @staticmethod
    def GetText(
        mol: Mol,
        confId: int = ...,
        kekulize: bool = ...,
        force_v3000: bool = ...,
        molid: int = ...,
    ) -> str: ...
    def NumMols(self) -> int: ...
    def SetForceV3000(self, arg2: bool): ...
    def SetKekulize(self, arg2: bool): ...
    def SetProps(
        self,
        arg2: Union[List[str], Tuple[str, ...]],
    ) -> Any: ...
    def close(self) -> None: ...
    def flush(self) -> None: ...
    def write(self, mol: Mol, confId: int = ...) -> None: ...
    def __enter__(self) -> "SDWriter": ...
    def __exit__(
        self,
        type: type[BaseException],
        value: BaseException,
        traceback: TracebackType,
    ) -> Optional[bool]: ...
    def __reduce__(self) -> Any: ...

class SmartsParserParams:
    __instance_size__: ClassVar[int] = ...
    allowCXSMILES: Any
    debugParse: Any
    mergeHs: Any
    parseName: Any
    strictCXSMILES: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class SmilesMolSupplier:
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetItemText(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def SetData(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def reset(cls, RDKit) -> Any: ...
    @classmethod
    def __enter__(cls, RDKit) -> Any: ...
    @classmethod
    def __exit__(cls, type, value, traceback) -> Any: ...
    @classmethod
    def __getitem__(cls, RDKit, int) -> Any: ...
    @classmethod
    def __iter__(cls, RDKit) -> Any: ...
    @classmethod
    def __len__(cls, RDKit) -> Any: ...
    @classmethod
    def __next__(cls, RDKit) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class SmilesParserParams:
    __instance_size__: ClassVar[int] = ...
    allowCXSMILES: Any
    debugParse: Any
    parseName: Any
    removeHs: Any
    sanitize: Any
    strictCXSMILES: Any
    useLegacyStereo: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class SmilesWriteParams:
    __instance_size__: ClassVar[int] = ...
    allBondsExplicit: Any
    allHsExplicit: Any
    canonical: Any
    doIsomericSmiles: Any
    doKekule: Any
    doRandom: Any
    rootedAtAtom: Any
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class SmilesWriter:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def NumMols(cls, RDKit) -> Any: ...
    @classmethod
    def SetProps(cls, RDKit, boost) -> Any: ...
    @classmethod
    def close(cls, RDKit) -> Any: ...
    @classmethod
    def flush(cls, RDKit) -> Any: ...
    @classmethod
    def write(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def __enter__(cls, RDKit) -> Any: ...
    @classmethod
    def __exit__(cls, type, value, traceback) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class TDTMolSupplier:
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetItemText(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def SetData(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def reset(cls, RDKit) -> Any: ...
    @classmethod
    def __enter__(cls, RDKit) -> Any: ...
    @classmethod
    def __exit__(cls, type, value, traceback) -> Any: ...
    @classmethod
    def __getitem__(cls, RDKit, int) -> Any: ...
    @classmethod
    def __iter__(cls, RDKit) -> Any: ...
    @classmethod
    def __len__(cls, RDKit) -> Any: ...
    @classmethod
    def __next__(cls, RDKit) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

class TDTWriter:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def GetNumDigits(cls, RDKit) -> Any: ...
    @classmethod
    def GetWrite2D(cls, RDKit) -> Any: ...
    @classmethod
    def GetWriteNames(cls, RDKit) -> Any: ...
    @classmethod
    def NumMols(cls, RDKit) -> Any: ...
    @classmethod
    def SetNumDigits(cls, RDKit, unsignedint) -> Any: ...
    @classmethod
    def SetProps(cls, RDKit, boost) -> Any: ...
    @classmethod
    def SetWrite2D(cls, RDKit) -> Any: ...
    @classmethod
    def SetWriteNames(cls, RDKit) -> Any: ...
    @classmethod
    def close(cls, RDKit) -> Any: ...
    @classmethod
    def flush(cls, RDKit) -> Any: ...
    @classmethod
    def write(cls, *args, **kwargs) -> Any: ...
    @classmethod
    def __enter__(cls, RDKit) -> Any: ...
    @classmethod
    def __exit__(cls, type, value, traceback) -> Any: ...
    @classmethod
    def __reduce__(cls) -> Any: ...

def AddMetadataToPNGFile(*args, **kwargs) -> Any: ...
def AddMetadataToPNGString(*args, **kwargs) -> Any: ...
def AtomFromSmarts(*args, **kwargs) -> Any: ...
def AtomFromSmiles(*args, **kwargs) -> Any: ...
def BondFromSmarts(*args, **kwargs) -> Any: ...
def BondFromSmiles(*args, **kwargs) -> Any: ...
@overload
def CanonicalRankAtoms(mol, breakTies=...) -> Any: ...
@overload
def CanonicalRankAtoms(RDKit) -> Any: ...
@overload
def CanonicalRankAtomsInFragment(mol, atomsToUse=..., breakTies=...) -> Any: ...
@overload
def CanonicalRankAtomsInFragment(RDKit, boost) -> Any: ...
def CreateAtomBoolPropertyList(*args, **kwargs) -> Any: ...
def CreateAtomDoublePropertyList(*args, **kwargs) -> Any: ...
def CreateAtomIntPropertyList(*args, **kwargs) -> Any: ...
def CreateAtomStringPropertyList(*args, **kwargs) -> Any: ...
def MetadataFromPNGFile(boost) -> Any: ...
def MetadataFromPNGString(boost) -> Any: ...
def MolFragmentToCXSmarts(RDKit, boost) -> Any: ...
def MolFragmentToCXSmiles(RDKit, boost) -> Any: ...
def MolFragmentToSmarts(RDKit, boost) -> Any: ...
def MolFragmentToSmiles(
    mol: Mol,
    atomsToUse: Iterable[int],
    bondsToUse: Optional[Iterable[int]] = None,
    atomSymbols: Optional[Iterable[str]] = None,
    bondSymbols: Optional[Iterable[str]] = None,
    isomericSmiles: Optional[bool] = True,
    kekuleSmiles: Optional[bool] = False,
    rootedAtAtom: Optional[int] = -1,
    canonical: Optional[bool] = True,
    allBondsExplicit: Optional[bool] = False,
    allHsExplicit: Optional[bool] = False,
    doRandom: Optional[bool] = False,
) -> str: ...
def MolFromFASTA(*args, **kwargs) -> Any: ...
def MolFromHELM(boost) -> Any: ...
def MolFromMol2Block(*args, **kwargs) -> Any: ...
def MolFromMol2File(*args, **kwargs) -> Any: ...
def MolFromMolBlock(boost) -> Any: ...
def MolFromMolFile(*args, **kwargs) -> Any: ...
def MolFromPDBBlock(boost) -> Any: ...
def MolFromPDBFile(*args, **kwargs) -> Any: ...
def MolFromPNGFile(*args, **kwargs) -> Any: ...
def MolFromPNGString(boost) -> Any: ...
def MolFromRDKitSVG(boost) -> Any: ...
def MolFromSequence(boost) -> Any: ...
@overload
def MolFromSmarts(boost) -> Any: ...
@overload
def MolFromSmarts(boost, RDKit) -> Any: ...
def MolFromSmiles(
    SMILES: str, sanitize: bool = ..., replacements: dict[str, str] = ...
) -> Mol | None: ...
def MolFromTPLBlock(boost) -> Any: ...
def MolFromTPLFile(*args, **kwargs) -> Any: ...
def MolMetadataToPNGFile(RDKit, boost) -> Any: ...
def MolMetadataToPNGString(RDKit, boost) -> Any: ...
def MolToCMLBlock(RDKit) -> Any: ...
def MolToCMLFile(*args, **kwargs) -> Any: ...
def MolToCXSmarts(RDKit) -> Any: ...
def MolToCXSmiles(RDKit) -> Any: ...
def MolToFASTA(RDKit) -> Any: ...
def MolToHELM(RDKit) -> Any: ...
def MolToMolBlock(
    mol: Mol,
    includeStereo: bool = ...,
    confId: int = ...,
    kekulize: bool = ...,
    forceV3000: bool = ...,
) -> str: ...
def MolToMolFile(*args, **kwargs) -> Any: ...
def MolToPDBBlock(RDKit) -> Any: ...
def MolToPDBFile(*args, **kwargs) -> Any: ...
def MolToRandomSmilesVect(*args, **kwargs) -> Any: ...
def MolToSequence(RDKit) -> Any: ...
def MolToSmarts(RDKit) -> Any: ...
def MolToSmiles(
    mol: Mol,
    isomericSmiles: Optional[bool] = True,
    kekuleSmiles: Optional[bool] = False,
    rootedAtAtom: Optional[int] = -1,
    canonical: Optional[bool] = True,
    allBondsExplicit: Optional[bool] = False,
    allHsExplicit: Optional[bool] = False,
    doRandom: Optional[bool] = False,
) -> str: ...
def MolToTPLBlock(RDKit) -> Any: ...
def MolToTPLFile(*args, **kwargs) -> Any: ...
def MolToV3KMolBlock(RDKit) -> Any: ...
def MolToV3KMolFile(*args, **kwargs) -> Any: ...
def MolToXYZBlock(RDKit) -> Any: ...
def MolToXYZFile(*args, **kwargs) -> Any: ...
def MolsFromPNGFile(*args, **kwargs) -> Any: ...
def MolsFromPNGString(boost) -> Any: ...
def SmilesMolSupplierFromText(*args, **kwargs) -> Any: ...
