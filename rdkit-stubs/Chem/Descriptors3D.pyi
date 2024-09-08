from collections.abc import Callable
from typing import Optional
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors as rdMolDescriptors

PMI1: Callable
""" 
First (smallest) principal moment of inertia

**Arguments**

  - inMol: a molecule

  - confId: (optional) the conformation ID to use

  - useAtomicMasses: (optional) toggles use of atomic masses in the
    calculation. Defaults to True
"""
PMI2: Callable
""" 
Second principal moment of inertia

**Arguments**

  - inMol: a molecule

  - confId: (optional) the conformation ID to use

  - useAtomicMasses: (optional) toggles use of atomic masses in the
    calculation. Defaults to True
"""
PMI3: Callable
""" 
Third (largest) principal moment of inertia

**Arguments**

  - inMol: a molecule

  - confId: (optional) the conformation ID to use

  - useAtomicMasses: (optional) toggles use of atomic masses in the
    calculation. Defaults to True
"""
NPR1: Callable
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
NPR2: Callable
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
RadiusOfGyration: Callable
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
InertialShapeFactor: Callable
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
Eccentricity: Callable
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
Asphericity: Callable
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
SpherocityIndex: Callable
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
PBF: Callable
""" 
Plane of best fit
  from: https://doi.org/10.1021/ci300293f

**Arguments**

  - inMol: a molecule

  - confId: (optional) the conformation ID to use

"""
def CalcMolDescriptors3D(mol: Chem.Mol, confId: Optional[int]=None):
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