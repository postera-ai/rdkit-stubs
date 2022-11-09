from _typeshed import Incomplete
from rdkit import RDConfig as RDConfig

TEST_FAILED: int
TEST_PASSED: int
BUILD_TYPE_ENVVAR: str

def isDebugBuild(): ...
def RunTest(exeName, args, extras): ...
def RunScript(script, doLongTests, verbose): ...
def ReportResults(script, failedTests, nTests, runTime, verbose, dest) -> None: ...

class _RedirectStream:
    _stream: Incomplete
    _new_target: Incomplete
    _old_targets: Incomplete
    def __init__(self, new_target) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exctype, excinst, exctb) -> None: ...

class redirect_stdout(_RedirectStream):
    _stream: str

class redirect_stderr(_RedirectStream):
    _stream: str

class OutputRedirectC:
    outfiles: Incomplete
    combine: Incomplete
    mode: Incomplete
    saved_streams: Incomplete
    fds: Incomplete
    saved_fds: Incomplete
    null_fds: Incomplete
    null_streams: Incomplete
    def __init__(self, stdout=..., stderr=..., mode: str = ...) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args): ...
