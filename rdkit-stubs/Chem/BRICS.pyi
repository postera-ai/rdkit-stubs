from _typeshed import Incomplete
from collections.abc import Generator
from rdkit import Chem as Chem

environs: Incomplete
reactionDefs: Incomplete
smartsGps: Incomplete
g1: Incomplete
g2: Incomplete
bnd: Incomplete
r1: Incomplete
r2: Incomplete
sma: Incomplete
t: Incomplete
environMatchers: Incomplete
bondMatchers: Incomplete
tmp: Incomplete
e1: Incomplete
e2: Incomplete
patt: Incomplete
reactions: Incomplete
reverseReactions: Incomplete
rs: Incomplete
ps: Incomplete
rxn: Incomplete
labels: Incomplete

def FindBRICSBonds(
    mol, randomizeOrder: bool = ..., silent: bool = ...
) -> Generator[Incomplete, None, None]: ...
def BreakBRICSBonds(
    mol, bonds: Incomplete | None = ..., sanitize: bool = ..., silent: bool = ...
): ...
def BRICSDecompose(
    mol,
    allNodes: Incomplete | None = ...,
    minFragmentSize: int = ...,
    onlyUseReactions: Incomplete | None = ...,
    silent: bool = ...,
    keepNonLeafNodes: bool = ...,
    singlePass: bool = ...,
    returnMols: bool = ...,
): ...

dummyPattern: Incomplete

def BRICSBuild(
    fragments,
    onlyCompleteMols: bool = ...,
    seeds: Incomplete | None = ...,
    uniquify: bool = ...,
    scrambleReagents: bool = ...,
    maxDepth: int = ...,
) -> Generator[Incomplete, None, None]: ...
def _test(): ...
