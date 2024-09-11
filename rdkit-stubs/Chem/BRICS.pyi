from _typeshed import Incomplete
from collections.abc import Generator, Iterable, ValuesView
from typing import Optional
from rdkit import Chem as Chem
from rdkit.Chem import Mol

environs: dict[str, str]
reactionDefs: list[tuple[str, str, str]]
smartsGps: Incomplete
environMatchers: dict[str, Mol]
bondMatchers: Incomplete
reactions: Incomplete
reverseReactions: Incomplete
rs: Incomplete
ps: Incomplete
rxn: Incomplete
labels: Incomplete

def FindBRICSBonds(
    mol: Mol, randomizeOrder: bool = False, silent: bool = True
) -> Generator[tuple[tuple[int, int], tuple[str, str]], None, None]:
    """
    returns the bonds in a molecule that BRICS would cleave

    >>> from rdkit import Chem
    >>> m = Chem.MolFromSmiles('CCCOCC')
    >>> res = list(FindBRICSBonds(m))
    >>> res
    [((3, 2), ('3', '4')), ((3, 4), ('3', '4'))]

    a more complicated case:

    >>> m = Chem.MolFromSmiles('CCCOCCC(=O)c1ccccc1')
    >>> res = list(FindBRICSBonds(m))
    >>> res
    [((3, 2), ('3', '4')), ((3, 4), ('3', '4')), ((6, 8), ('6', '16'))]

    we can also randomize the order of the results:

    >>> random.seed(23)
    >>> res = list(FindBRICSBonds(m,randomizeOrder=True))
    >>> sorted(res)
    [((3, 2), ('3', '4')), ((3, 4), ('3', '4')), ((6, 8), ('6', '16'))]

    Note that this is a generator function :

    >>> res = FindBRICSBonds(m)
    >>> res
    <generator object ...>
    >>> next(res)
    ((3, 2), ('3', '4'))

    >>> m = Chem.MolFromSmiles('CC=CC')
    >>> res = list(FindBRICSBonds(m))
    >>> sorted(res)
    [((1, 2), ('7', '7'))]

    make sure we don't match ring bonds:

    >>> m = Chem.MolFromSmiles('O=C1NCCC1')
    >>> list(FindBRICSBonds(m))
    []

    another nice one, make sure environment 8 doesn't match something connected
    to a ring atom:

    >>> m = Chem.MolFromSmiles('CC1(C)CCCCC1')
    >>> list(FindBRICSBonds(m))
    []

    """

def BreakBRICSBonds(
    mol: Mol,
    bonds: Optional[list[tuple[tuple[int, int], tuple[str, str]]]] = None,
    sanitize: bool = True,
    silent: bool = True,
) -> Mol:
    """
    breaks the BRICS bonds in a molecule and returns the results

    >>> from rdkit import Chem
    >>> m = Chem.MolFromSmiles('CCCOCC')
    >>> m2=BreakBRICSBonds(m)
    >>> Chem.MolToSmiles(m2,True)
    '[3*]O[3*].[4*]CC.[4*]CCC'

    a more complicated case:

    >>> m = Chem.MolFromSmiles('CCCOCCC(=O)c1ccccc1')
    >>> m2=BreakBRICSBonds(m)
    >>> Chem.MolToSmiles(m2,True)
    '[16*]c1ccccc1.[3*]O[3*].[4*]CCC.[4*]CCC([6*])=O'


    can also specify a limited set of bonds to work with:

    >>> m = Chem.MolFromSmiles('CCCOCC')
    >>> m2 = BreakBRICSBonds(m,[((3, 2), ('3', '4'))])
    >>> Chem.MolToSmiles(m2,True)
    '[3*]OCC.[4*]CCC'

    this can be used as an alternate approach for doing a BRICS decomposition by
    following BreakBRICSBonds with a call to Chem.GetMolFrags:

    >>> m = Chem.MolFromSmiles('CCCOCC')
    >>> m2=BreakBRICSBonds(m)
    >>> frags = Chem.GetMolFrags(m2,asMols=True)
    >>> [Chem.MolToSmiles(x,True) for x in frags]
    ['[4*]CCC', '[3*]O[3*]', '[4*]CC']

    """

def BRICSDecompose(
    mol: Mol,
    allNodes: Optional[set[str]] = None,
    minFragmentSize: int = 1,
    onlyUseReactions: Optional[tuple] = None,
    silent: bool = True,
    keepNonLeafNodes: bool = False,
    singlePass: bool = False,
    returnMols: bool = False,
) -> set[str] | ValuesView:
    """
    returns the BRICS decomposition for a molecule

    >>> from rdkit import Chem
    >>> m = Chem.MolFromSmiles('CCCOCc1cc(c2ncccc2)ccc1')
    >>> res = list(BRICSDecompose(m))
    >>> sorted(res)
    ['[14*]c1ccccn1', '[16*]c1cccc([16*])c1', '[3*]O[3*]', '[4*]CCC', '[4*]C[8*]']

    >>> res = list(BRICSDecompose(m,returnMols=True))
    >>> res[0]
    <rdkit.Chem.rdchem.Mol object ...>
    >>> smis = [Chem.MolToSmiles(x,True) for x in res]
    >>> sorted(smis)
    ['[14*]c1ccccn1', '[16*]c1cccc([16*])c1', '[3*]O[3*]', '[4*]CCC', '[4*]C[8*]']

    nexavar, an example from the paper (corrected):

    >>> m = Chem.MolFromSmiles('CNC(=O)C1=NC=CC(OC2=CC=C(NC(=O)NC3=CC(=C(Cl)C=C3)C(F)(F)F)C=C2)=C1')
    >>> res = list(BRICSDecompose(m))
    >>> sorted(res)
    ['[1*]C([1*])=O', '[1*]C([6*])=O', '[14*]c1cc([16*])ccn1', '[16*]c1ccc(Cl)c([16*])c1', '[16*]c1ccc([16*])cc1', '[3*]O[3*]', '[5*]NC', '[5*]N[5*]', '[8*]C(F)(F)F']

    it's also possible to keep pieces that haven't been fully decomposed:

    >>> m = Chem.MolFromSmiles('CCCOCC')
    >>> res = list(BRICSDecompose(m,keepNonLeafNodes=True))
    >>> sorted(res)
    ['CCCOCC', '[3*]OCC', '[3*]OCCC', '[3*]O[3*]', '[4*]CC', '[4*]CCC']

    >>> m = Chem.MolFromSmiles('CCCOCc1cc(c2ncccc2)ccc1')
    >>> res = list(BRICSDecompose(m,keepNonLeafNodes=True))
    >>> sorted(res)
    ['CCCOCc1cccc(-c2ccccn2)c1', '[14*]c1ccccn1', '[16*]c1cccc(-c2ccccn2)c1', '[16*]c1cccc(COCCC)c1', '[16*]c1cccc([16*])c1', '[3*]OCCC', '[3*]OC[8*]', '[3*]OCc1cccc(-c2ccccn2)c1', '[3*]OCc1cccc([16*])c1', '[3*]O[3*]', '[4*]CCC', '[4*]C[8*]', '[4*]Cc1cccc(-c2ccccn2)c1', '[4*]Cc1cccc([16*])c1', '[8*]COCCC']

    or to only do a single pass of decomposition:

    >>> m = Chem.MolFromSmiles('CCCOCc1cc(c2ncccc2)ccc1')
    >>> res = list(BRICSDecompose(m,singlePass=True))
    >>> sorted(res)
    ['CCCOCc1cccc(-c2ccccn2)c1', '[14*]c1ccccn1', '[16*]c1cccc(-c2ccccn2)c1', '[16*]c1cccc(COCCC)c1', '[3*]OCCC', '[3*]OCc1cccc(-c2ccccn2)c1', '[4*]CCC', '[4*]Cc1cccc(-c2ccccn2)c1', '[8*]COCCC']

    setting a minimum size for the fragments:

    >>> m = Chem.MolFromSmiles('CCCOCC')
    >>> res = list(BRICSDecompose(m,keepNonLeafNodes=True,minFragmentSize=2))
    >>> sorted(res)
    ['CCCOCC', '[3*]OCC', '[3*]OCCC', '[4*]CC', '[4*]CCC']
    >>> m = Chem.MolFromSmiles('CCCOCC')
    >>> res = list(BRICSDecompose(m,keepNonLeafNodes=True,minFragmentSize=3))
    >>> sorted(res)
    ['CCCOCC', '[3*]OCC', '[4*]CCC']
    >>> res = list(BRICSDecompose(m,minFragmentSize=2))
    >>> sorted(res)
    ['[3*]OCC', '[3*]OCCC', '[4*]CC', '[4*]CCC']


    """

def BRICSBuild(
    fragments,
    onlyCompleteMols: bool = True,
    seeds: Optional[Iterable] = None,
    uniquify: bool = True,
    scrambleReagents: bool = True,
    maxDepth: int = 3,
) -> Generator[Mol, None, None]: ...
def _test(): ...
