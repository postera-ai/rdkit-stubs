from _typeshed import Incomplete
from rdkit import Chem as Chem
from rdkit.Chem import inchi as inchi

def _is_achiral_by_symmetry(INCHI): ...

console: Incomplete
UPD_APP: Incomplete
version_re: Incomplete
reconnected_re: Incomplete
fixed_h_re: Incomplete
isotope_re: Incomplete
stereo_re: Incomplete
stereo_all_re: Incomplete
undef_stereo_re: Incomplete
all_stereo_re: Incomplete
defined_stereo_re: Incomplete
h_layer_re: Incomplete
mobile_h_group_re: Incomplete
mobile_h_atoms_re: Incomplete

class InchiInfo:
    parsed_inchi: Incomplete
    def __init__(self, inchi_str) -> None: ...
    def get_sp3_stereo(self): ...
    def get_mobile_h(self): ...
