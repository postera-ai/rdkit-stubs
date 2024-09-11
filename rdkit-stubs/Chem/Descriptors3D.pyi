from typing import Optional
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors as rdMolDescriptors

def PMI1(
    mol: Chem.Mol, confId: int = -1, useAtomicMasses: bool = True, force: bool = True
) -> float:
    """
    First (smallest) principal moment of inertia

    **Arguments**

      - inMol: a molecule

      - confId: (optional) the conformation ID to use

      - useAtomicMasses: (optional) toggles use of atomic masses in the
        calculation. Defaults to True
    """

def PMI2(
    mol: Chem.Mol, confId: int = -1, useAtomicMasses: bool = True, force: bool = True
) -> float:
    """
    Second principal moment of inertia

    **Arguments**

      - inMol: a molecule

      - confId: (optional) the conformation ID to use

      - useAtomicMasses: (optional) toggles use of atomic masses in the
        calculation. Defaults to True
    """

def PMI3(
    mol: Chem.Mol, confId: int = -1, useAtomicMasses: bool = True, force: bool = True
) -> float:
    """
    Third (largest) principal moment of inertia

    **Arguments**

      - inMol: a molecule

      - confId: (optional) the conformation ID to use

      - useAtomicMasses: (optional) toggles use of atomic masses in the
        calculation. Defaults to True
    """

def NPR1(
    mol: Chem.Mol, confId: int = -1, useAtomicMasses: bool = True, force: bool = True
) -> float:
    """
    Normalized principal moments ratio 1 (=I1/I3)

        from Sauer and Schwarz JCIM 43:987-1003 (2003)
        https://doi.org/10.1021/ci025599w


    **Arguments**

      - inMol: a molecule

      - confId: (optional) the conformation ID to use

      - useAtomicMasses: (optional) toggles use of atomic masses in the
        calculation. Defaults to True
    """

def NPR2(
    mol: Chem.Mol, confId: int = -1, useAtomicMasses: bool = True, force: bool = True
) -> float:
    """
    Normalized principal moments ratio 2 (=I2/I3)

        from Sauer and Schwarz JCIM 43:987-1003 (2003)
        https://doi.org/10.1021/ci025599w


    **Arguments**

      - inMol: a molecule

      - confId: (optional) the conformation ID to use

      - useAtomicMasses: (optional) toggles use of atomic masses in the
        calculation. Defaults to True
    """

def RadiusOfGyration(
    mol: Chem.Mol, confId: int = -1, useAtomicMasses: bool = True, force: bool = True
) -> float:
    """
    Radius of gyration

        from Todeschini and Consoni "Descriptors from Molecular Geometry"
        Handbook of Chemoinformatics
        https://doi.org/10.1002/9783527618279.ch37

        Definition:
          for planar molecules: sqrt( sqrt(pm3*pm2)/MW )
          for nonplanar molecules: sqrt( 2*pi*pow(pm3*pm2*pm1,1/3)/MW )

    **Arguments**

      - inMol: a molecule

      - confId: (optional) the conformation ID to use

      - useAtomicMasses: (optional) toggles use of atomic masses in the
        calculation. Defaults to True
    """

def InertialShapeFactor(
    mol: Chem.Mol, confId: int = -1, useAtomicMasses: bool = True, force: bool = True
) -> float:
    """
    Inertial shape factor

        from Todeschini and Consoni "Descriptors from Molecular Geometry"
        Handbook of Chemoinformatics
        https://doi.org/10.1002/9783527618279.ch37

        Definition:
          pm2 / (pm1*pm3)

    **Arguments**

      - inMol: a molecule

      - confId: (optional) the conformation ID to use

      - useAtomicMasses: (optional) toggles use of atomic masses in the
        calculation. Defaults to True
    """

def Eccentricity(
    mol: Chem.Mol, confId: int = -1, useAtomicMasses: bool = True, force: bool = True
) -> float:
    """
    molecular eccentricity

        from Todeschini and Consoni "Descriptors from Molecular Geometry"
        Handbook of Chemoinformatics
        https://doi.org/10.1002/9783527618279.ch37

        Definition:
          sqrt(pm3**2 -pm1**2) / pm3

    **Arguments**

      - inMol: a molecule

      - confId: (optional) the conformation ID to use

      - useAtomicMasses: (optional) toggles use of atomic masses in the
        calculation. Defaults to True
    """

def Asphericity(
    mol: Chem.Mol, confId: int = -1, useAtomicMasses: bool = True, force: bool = True
) -> float:
    """
    molecular asphericity

        from Todeschini and Consoni "Descriptors from Molecular Geometry"
        Handbook of Chemoinformatics
        https://doi.org/10.1002/9783527618279.ch37

        Definition:
          0.5 * ((pm3-pm2)**2 + (pm3-pm1)**2 + (pm2-pm1)**2)/(pm1**2+pm2**2+pm3**2)

    **Arguments**

      - inMol: a molecule

      - confId: (optional) the conformation ID to use

      - useAtomicMasses: (optional) toggles use of atomic masses in the
        calculation. Defaults to True
    """

def SpherocityIndex(mol: Chem.Mol, confId: int = -1, force: bool = True) -> float:
    """
    Molecular spherocityIndex

        from Todeschini and Consoni "Descriptors from Molecular Geometry"
        Handbook of Chemoinformatics
        https://doi.org/10.1002/9783527618279.ch37

        Definition:
          3 * pm1 / (pm1+pm2+pm3) where the moments are calculated without weights

    **Arguments**

      - inMol: a molecule

      - confId: (optional) the conformation ID to use

    """

def PBF(mol: Chem.Mol, confId: int = -1) -> float:
    """
    Plane of best fit
      from: https://doi.org/10.1021/ci300293f

    **Arguments**

      - inMol: a molecule

      - confId: (optional) the conformation ID to use

    """

def CalcMolDescriptors3D(mol: Chem.Mol, confId: Optional[int] = None):
    """
    Compute all 3D descriptors of a molecule

    Arguments:
    - mol: the molecule to work with
    - confId: conformer ID to work with. If not specified the default (-1) is used

    Return:

    dict
        A dictionary with decriptor names as keys and the descriptor values as values

    raises a ValueError
        If the molecule does not have conformers
    """
