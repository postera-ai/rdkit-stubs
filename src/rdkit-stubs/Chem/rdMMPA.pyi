from typing import Any

from typing import overload

@overload
def FragmentMol(RDKit) -> Any: ...
@overload
def FragmentMol(RDKit, boost) -> Any: ...
