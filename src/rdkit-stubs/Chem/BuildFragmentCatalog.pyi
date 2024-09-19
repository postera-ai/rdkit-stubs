from collections.abc import Sequence
from io import IOBase
import sys
from typing import Optional, TextIO
import numpy as np
import numpy.typing as npt
from rdkit import RDConfig as RDConfig
from rdkit.Chem import FragmentCatalog as FragmentCatalog
from rdkit.Dbase.DbConnection import DbConnect as DbConnect
from rdkit.ML import InfoTheory as InfoTheory

def message(msg, dest=sys.stdout) -> None: ...
def BuildCatalog(
    suppl,
    maxPts: int = -1,
    groupFileName: Optional[str] = None,
    minPath: int = 2,
    maxPath: int = 6,
    reportFreq: int = 10,
):
    """
    builds a fragment catalog from a set of molecules in a delimited text block

      **Arguments**

        - suppl: a mol supplier

        - maxPts: (optional) if provided, this will set an upper bound on the
          number of points to be considered

        - groupFileName: (optional) name of the file containing functional group
          information

        - minPath, maxPath: (optional) names of the minimum and maximum path lengths
          to be considered

        - reportFreq: (optional) how often to display status information

      **Returns**

        a FragmentCatalog

    """

def ScoreMolecules(
    suppl,
    catalog,
    maxPts: int = -1,
    actName: str = "",
    acts: Optional[Sequence[int]] = None,
    nActs: int = 2,
    reportFreq: int = 10,
) -> tuple[npt.NDArray[np.int32], Sequence[Sequence[int]]]:
    """
    scores the compounds in a supplier using a catalog

      **Arguments**

        - suppl: a mol supplier

        - catalog: the FragmentCatalog

        - maxPts: (optional) the maximum number of molecules to be
          considered

        - actName: (optional) the name of the molecule's activity property.
          If this is not provided, the molecule's last property will be used.

        - acts: (optional) a sequence of activity values (integers).
          If not provided, the activities will be read from the molecules.

        - nActs: (optional) number of possible activity values

        - reportFreq: (optional) how often to display status information

      **Returns**

        a 2-tuple:

          1) the results table (a 3D array of ints nBits x 2 x nActs)

          2) a list containing the on bit lists for each molecule

    """

def ScoreFromLists(
    bitLists: Sequence[Sequence[int]],
    suppl,
    catalog,
    maxPts: int = -1,
    actName: str = "",
    acts: Optional[Sequence[int]] = None,
    nActs: int = 2,
    reportFreq: int = 10,
) -> tuple[npt.NDArray[np.int32]]:
    """
    similar to _ScoreMolecules()_, but uses pre-calculated bit lists
    for the molecules (this speeds things up a lot)

      **Arguments**

        - bitLists: sequence of on bit sequences for the input molecules

        - suppl: the input supplier (we read activities from here)

        - catalog: the FragmentCatalog

        - maxPts: (optional) the maximum number of molecules to be
          considered

        - actName: (optional) the name of the molecule's activity property.
          If this is not provided, the molecule's last property will be used.

        - nActs: (optional) number of possible activity values

        - reportFreq: (optional) how often to display status information

      **Returns**

         the results table (a 3D array of ints nBits x 2 x nActs)

    """

def CalcGains(
    suppl,
    catalog,
    topN: int = -1,
    actName: str = "",
    acts: Optional[Sequence[int]] = None,
    nActs: int = 2,
    reportFreq: int = 10,
    biasList=None,
    collectFps: int = 0,
):
    """
    calculates info gains by constructing fingerprints
    *DOC*

    Returns a 2-tuple:
        1) gains matrix
        2) list of fingerprints
    """

def CalcGainsFromFps(
    suppl,
    fps,
    topN: int = -1,
    actName: str = "",
    acts: Optional[Sequence[int]] = None,
    nActs: int = 2,
    reportFreq: int = 10,
    biasList=None,
):
    """
    calculates info gains from a set of fingerprints

    *DOC*
    """

def OutputGainsData(outF: IOBase, gains, cat, nActs: int = 2) -> None: ...
def ProcessGainsData(inF: IOBase, delim: str = ",", idCol: int = 0, gainCol: int = 1):
    """reads a list of ids and info gains out of an input file"""

def ShowDetails(
    catalog,
    gains,
    nToDo: int = -1,
    outF: TextIO = sys.stdout,
    idCol: int = 0,
    gainCol: int = 1,
    outDelim: str = ",",
) -> None:
    """
    gains should be a sequence of sequences.  The idCol entry of each
    sub-sequence should be a catalog ID.  _ProcessGainsData()_ provides
    suitable input.
    """

def SupplierFromDetails(details): ...
def Usage() -> None: ...

class RunDetails:
    numMols: int = -1
    doBuild: int = 0
    doSigs: int = 0
    doScore: int = 0
    doGains: int = 0
    doDetails: int = 0
    catalogName: Optional[str] = None
    onBitsName: Optional[str] = None
    scoresName: Optional[str] = None
    gainsName: Optional[str] = None
    dbName: str = ""
    tableName: Optional[str] = None
    detailsName: Optional[str] = None
    inFileName: Optional[str] = None
    fpName: Optional[str] = None
    minPath: int = 2
    maxPath: int = 6
    smiCol: int = 1
    actCol: int = -1
    nameCol: int = -1
    hasTitle: int = 1
    nActs: int = 2
    nBits: int = -1
    delim: str = ","
    biasList: Optional[tuple] = None
    topN: int = -1

def ParseArgs(details: RunDetails) -> None: ...
