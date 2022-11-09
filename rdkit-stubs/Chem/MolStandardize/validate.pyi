import logging
from .errors import StopValidateError as StopValidateError
from .validations import VALIDATIONS as VALIDATIONS
from _typeshed import Incomplete
from rdkit import Chem as Chem

SIMPLE_FORMAT: str
LONG_FORMAT: str

class LogHandler(logging.Handler):
    logs: Incomplete
    def __init__(self) -> None: ...
    @property
    def logmessages(self): ...
    def emit(self, record) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...

class Validator:
    raw: Incomplete
    log: Incomplete
    handler: Incomplete
    validations: Incomplete
    def __init__(
        self,
        validations=...,
        log_format=...,
        level=...,
        stdout: bool = ...,
        raw: bool = ...,
    ) -> None: ...
    def __call__(self, mol): ...
    def validate(self, mol): ...

def validate_smiles(smiles): ...
