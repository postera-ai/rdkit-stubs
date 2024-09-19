from .errors import StopValidateError as StopValidateError
from .fragment import REMOVE_FRAGMENTS as REMOVE_FRAGMENTS
from _typeshed import Incomplete
from rdkit import Chem as Chem

class Validation:
    log: Incomplete
    def __init__(self, log) -> None: ...
    def __call__(self, mol) -> None: ...
    def run(self, mol) -> None: ...

class SmartsValidation(Validation):
    level: Incomplete
    message: str
    entire_fragment: bool
    _smarts: Incomplete
    def __init__(self, log) -> None: ...
    @property
    def smarts(self) -> str: ...
    def _check_matches(self, mol) -> None: ...
    def _check_matches_fragment(self, mol) -> None: ...
    def run(self, mol) -> None: ...

class IsNoneValidation(Validation):
    def run(self, mol) -> None: ...

class NoAtomValidation(Validation):
    def run(self, mol) -> None: ...

class DichloroethaneValidation(SmartsValidation):
    level: Incomplete
    smarts: str
    entire_fragment: bool
    message: str

class FragmentValidation(Validation):
    fragments: Incomplete
    def run(self, mol) -> None: ...

class NeutralValidation(Validation):
    def run(self, mol) -> None: ...

class IsotopeValidation(Validation):
    def run(self, mol) -> None: ...

VALIDATIONS: Incomplete
