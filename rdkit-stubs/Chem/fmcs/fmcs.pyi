from _typeshed import Incomplete
from collections.abc import Generator
from rdkit import Chem as Chem
from typing import NamedTuple

__version__: str
__version_info: Incomplete

class Default:
    timeout: Incomplete
    timeoutString: str
    maximize: str
    atomCompare: str
    bondCompare: str
    matchValences: bool
    ringMatchesRingOnly: bool
    completeRingsOnly: bool

_get_symbol: Incomplete

class AtomSmartsNoAromaticity(dict):
    def __missing__(self, eleno): ...

_atom_smarts_no_aromaticity: Incomplete

def atom_typer_any(atoms): ...
def atom_typer_elements(atoms): ...
def atom_typer_isotopes(atoms): ...
def bond_typer_any(bonds): ...
def bond_typer_bondtypes(bonds): ...

atom_typers: Incomplete
bond_typers: Incomplete
default_atom_typer: Incomplete
default_bond_typer: Incomplete

def get_isotopes(mol): ...
def set_isotopes(mol, isotopes) -> None: ...

_isotope_dict: Incomplete
_atom_class_dict: Incomplete

def save_isotopes(mol, isotopes) -> None: ...
def save_atom_classes(mol, atom_classes) -> None: ...
def get_selected_atom_classes(mol, atom_indices): ...
def restore_isotopes(mol) -> None: ...
def assign_isotopes_from_class_tag(mol, atom_class_tag) -> None: ...

class TypedMolecule:
    rdmol: Incomplete
    rdmol_atoms: Incomplete
    rdmol_bonds: Incomplete
    atom_smarts_types: Incomplete
    bond_smarts_types: Incomplete
    canonical_bondtypes: Incomplete
    def __init__(
        self,
        rdmol,
        rdmol_atoms,
        rdmol_bonds,
        atom_smarts_types,
        bond_smarts_types,
        canonical_bondtypes,
    ) -> None: ...

class FragmentedTypedMolecule:
    rdmol: Incomplete
    rdmol_atoms: Incomplete
    orig_atoms: Incomplete
    orig_bonds: Incomplete
    atom_smarts_types: Incomplete
    bond_smarts_types: Incomplete
    canonical_bondtypes: Incomplete
    def __init__(
        self,
        rdmol,
        rdmol_atoms,
        orig_atoms,
        orig_bonds,
        atom_smarts_types,
        bond_smarts_types,
        canonical_bondtypes,
    ) -> None: ...

class TypedFragment:
    rdmol: Incomplete
    orig_atoms: Incomplete
    orig_bonds: Incomplete
    atom_smarts_types: Incomplete
    bond_smarts_types: Incomplete
    canonical_bondtypes: Incomplete
    def __init__(
        self,
        rdmol,
        orig_atoms,
        orig_bonds,
        atom_smarts_types,
        bond_smarts_types,
        canonical_bondtypes,
    ) -> None: ...

def get_canonical_bondtypes(rdmol, bonds, atom_smarts_types, bond_smarts_types): ...
def get_typed_molecule(
    rdmol, atom_typer, bond_typer, matchValences=..., ringMatchesRingOnly=...
): ...
def get_specified_types(rdmol, atom_types, ringMatchesRingOnly): ...
def convert_input_to_typed_molecules(
    mols, atom_typer, bond_typer, matchValences, ringMatchesRingOnly
): ...
def _check_atom_classes(molno, num_atoms, atom_classes) -> None: ...
def get_counts(it): ...
def intersect_counts(counts1, counts2): ...
def get_canonical_bondtype_counts(typed_mols): ...
def remove_unknown_bondtypes(typed_mol, supported_canonical_bondtypes): ...
def find_upper_fragment_size_limits(rdmol, atoms): ...

class EnumerationMolecule(NamedTuple):
    rdmol: Incomplete
    atoms: Incomplete
    bonds: Incomplete
    directed_edges: Incomplete

class Atom(NamedTuple):
    real_atom: Incomplete
    atom_smarts: Incomplete
    bond_indices: Incomplete
    is_in_ring: Incomplete

class Bond(NamedTuple):
    real_bond: Incomplete
    bond_smarts: Incomplete
    canonical_bondtype: Incomplete
    atom_indices: Incomplete
    is_in_ring: Incomplete

class DirectedEdge(NamedTuple):
    bond_index: Incomplete
    end_atom_index: Incomplete

class Subgraph(NamedTuple):
    atom_indices: Incomplete
    bond_indices: Incomplete

def get_typed_fragment(typed_mol, atom_indices): ...
def fragmented_mol_to_enumeration_mols(typed_mol, minNumAtoms: int = ...): ...
def gen_primes() -> Generator[Incomplete, None, None]: ...

_prime_stream: Incomplete
_primes: Incomplete

def _get_nth_prime(n): ...

class CangenNode:
    __slots__: Incomplete
    index: Incomplete
    atom_smarts: Incomplete
    value: int
    neighbors: Incomplete
    rank: int
    outgoing_edges: Incomplete
    def __init__(self, index, atom_smarts) -> None: ...

class OutgoingEdge(NamedTuple):
    from_atom_index: Incomplete
    bond_index: Incomplete
    bond_smarts: Incomplete
    other_node_idx: Incomplete
    other_node: Incomplete

def get_initial_cangen_nodes(
    subgraph, enumeration_mol, atom_assignment, do_initial_assignment: bool = ...
): ...
def rerank(cangen_nodes) -> None: ...
def find_duplicates(cangen_nodes, start, end): ...
def canon(cangen_nodes): ...
def get_closure_label(bond_smarts, closure): ...

_available_closures: Incomplete

def generate_smarts(cangen_nodes): ...
def make_canonical_smarts(subgraph, enumeration_mol, atom_assignment): ...
def make_arbitrary_smarts(subgraph, enumeration_mol, atom_assignment): ...
def powerset(iterable): ...
def nonempty_powerset(iterable): ...
def _Counter(): ...

tiebreaker: Incomplete

def find_extensions(atom_indices, visited_bond_indices, directed_edges): ...
def all_subgraph_extensions(
    enumeration_mol, subgraph, visited_bond_indices, internal_bonds, external_edges
) -> Generator[Incomplete, None, None]: ...
def find_extension_size(
    enumeration_mol, known_atoms, exclude_bonds, directed_edges
): ...

class CachingTargetsMatcher(dict):
    targets: Incomplete
    required_match_count: Incomplete
    _num_allowed_errors: Incomplete
    def __init__(
        self, targets, required_match_count: Incomplete | None = ...
    ) -> None: ...
    def shift_targets(self) -> None: ...
    def __missing__(self, smarts): ...

class VerboseCachingTargetsMatcher:
    targets: Incomplete
    cache: Incomplete
    required_match_count: Incomplete
    _num_allowed_errors: Incomplete
    num_lookups: int
    num_search_true: int
    def __init__(
        self, targets, required_match_count: Incomplete | None = ...
    ) -> None: ...
    def shift_targets(self) -> None: ...
    def __getitem__(self, smarts, missing=...): ...
    def report(self) -> None: ...

def prune_maximize_bonds(
    subgraph, mol, num_remaining_atoms, num_remaining_bonds, best_sizes
): ...
def prune_maximize_atoms(
    subgraph, mol, num_remaining_atoms, num_remaining_bonds, best_sizes
): ...

class _SingleBest:
    best_num_atoms: int
    best_smarts: Incomplete
    sizes: Incomplete
    timer: Incomplete
    verbose: Incomplete
    def __init__(self, timer, verbose) -> None: ...
    best_num_bonds: Incomplete
    def _new_best(self, num_atoms, num_bonds, smarts): ...
    def get_result(self, completed): ...

class MCSResult:
    num_atoms: Incomplete
    num_bonds: Incomplete
    smarts: Incomplete
    completed: Incomplete
    def __init__(self, num_atoms, num_bonds, smarts, completed) -> None: ...
    def __nonzero__(self): ...

class SingleBestAtoms(_SingleBest):
    def add_new_match(self, subgraph, mol, smarts): ...

class SingleBestBonds(_SingleBest):
    def add_new_match(self, subgraph, mol, smarts): ...

def check_completeRingsOnly(smarts, subgraph, enumeration_mol): ...

class SingleBestAtomsCompleteRingsOnly(_SingleBest):
    def add_new_match(self, subgraph, mol, smarts): ...

class SingleBestBondsCompleteRingsOnly(_SingleBest):
    def add_new_match(self, subgraph, mol, smarts): ...

_maximize_options: Incomplete

def enumerate_subgraphs(
    enumeration_mols,
    prune,
    atom_assignment,
    matches_all_targets,
    hits,
    timeout,
    heappush,
    heappop,
): ...

class Uniquer(dict):
    counter: Incomplete
    def __init__(self) -> None: ...
    def __missing__(self, key): ...

def MATCH(mol, pat): ...

class VerboseHeapOps:
    num_seeds_added: int
    num_seeds_processed: int
    verboseDelay: Incomplete
    _time_for_next_report: Incomplete
    trigger: Incomplete
    def __init__(self, trigger, verboseDelay) -> None: ...
    def heappush(self, seeds, item): ...
    def heappop(self, seeds): ...
    def trigger_report(self) -> None: ...
    def report(self) -> None: ...

def compute_mcs(
    fragmented_mols,
    typed_mols,
    minNumAtoms,
    threshold_count: Incomplete | None = ...,
    maximize=...,
    completeRingsOnly=...,
    timeout=...,
    timer: Incomplete | None = ...,
    verbose: bool = ...,
    verboseDelay: float = ...,
): ...

class Timer:
    mark_times: Incomplete
    def __init__(self) -> None: ...
    def mark(self, name) -> None: ...

def _update_times(timer, times) -> None: ...
def _get_threshold_count(num_mols, threshold): ...
def fmcs(
    mols,
    minNumAtoms: int = ...,
    maximize=...,
    atomCompare=...,
    bondCompare=...,
    threshold: float = ...,
    matchValences=...,
    ringMatchesRingOnly: bool = ...,
    completeRingsOnly: bool = ...,
    timeout=...,
    times: Incomplete | None = ...,
    verbose: bool = ...,
    verboseDelay: float = ...,
): ...
def subgraph_to_fragment(mol, subgraph): ...
def make_fragment_smiles(mcs, mol, subgraph, args: Incomplete | None = ...): ...
def _copy_sd_tags(mol, fragment) -> None: ...
def _MolToSDBlock(mol): ...
def _save_other_tags(mol, fragment, mcs, orig_mol, subgraph, args) -> None: ...
def make_fragment_sdf(mcs, mol, subgraph, args): ...
def make_complete_sdf(mcs, mol, subgraph, args): ...

structure_format_functions: Incomplete

def make_structure_format(format_name, mcs, mol, subgraph, args): ...
def parse_num_atoms(s): ...
def parse_threshold(s): ...
def parse_timeout(s): ...

class starting_from:
    left: Incomplete
    def __init__(self, left) -> None: ...
    def __contains__(self, value) -> bool: ...

range_pat: Incomplete
value_pat: Incomplete

def parse_select(s): ...

compare_shortcuts: Incomplete

def _get_match_bond_indices(pat, mol, match_atom_indices): ...
def main(args: Incomplete | None = ...) -> None: ...
