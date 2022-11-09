from _typeshed import Incomplete
from rdkit import Chem as Chem, RDConfig as RDConfig
from rdkit.Avalon import pyAvalonTools as pyAvalonTools
from rdkit.Chem.MolKey import InchiInfo as InchiInfo
from typing import NamedTuple

class MolIdentifierException(Exception): ...
class BadMoleculeException(Exception): ...

MOL_KEY_VERSION: str
ERROR_DICT: Incomplete
INCHI_COMPUTATION_ERROR: Incomplete
RDKIT_CONVERSION_ERROR: Incomplete
INCHI_READWRITE_ERROR: Incomplete
NULL_MOL: Incomplete
BAD_SET: Incomplete
GET_STEREO_RE: Incomplete
NULL_SMILES_RE: Incomplete
PATTERN_NULL_MOL: str
CHIRAL_POS: int
T_NULL_MOL: Incomplete
stereo_code_dict: Incomplete

def _fix_all(pat, sbt, my_string): ...
def _fix_line_ends(my_string): ...
def _fix_chemdraw_header(my_string): ...
def _ctab_has_atoms(ctab_lines): ...
def _ctab_remove_chiral_flag(ctab_lines): ...

__initCalled: bool

def initStruchk(
    configDir: Incomplete | None = ..., logFile: Incomplete | None = ...
) -> None: ...
def CheckCTAB(ctab, isSmiles: bool = ...): ...

class InchiResult(NamedTuple):
    error: Incomplete
    inchi: Incomplete
    fixed_ctab: Incomplete

def GetInchiForCTAB(ctab): ...
def _make_racemate_inchi(inchi): ...
def _get_identification_string(
    err,
    ctab,
    inchi,
    stereo_category: Incomplete | None = ...,
    extra_stereo: Incomplete | None = ...,
): ...
def _get_null_mol_identification_string(extra_stereo): ...
def _get_bad_mol_identification_string(ctab, stereo_category, extra_stereo): ...
def _identify(
    err, ctab, inchi, stereo_category, extra_structure_desc: Incomplete | None = ...
): ...
def _get_chiral_identification_string(n_def, n_udf): ...
def ErrorBitsToText(err): ...

class MolKeyResult(NamedTuple):
    mol_key: Incomplete
    error: Incomplete
    inchi: Incomplete
    fixed_ctab: Incomplete
    stereo_code: Incomplete
    stereo_comment: Incomplete

def GetKeyForCTAB(
    ctab,
    stereo_info: Incomplete | None = ...,
    stereo_comment: Incomplete | None = ...,
    logger: Incomplete | None = ...,
): ...
def _runDoctests(verbose: Incomplete | None = ...) -> None: ...
