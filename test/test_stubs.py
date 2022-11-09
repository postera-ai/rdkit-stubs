from rdkit import Chem


def sample_mol() -> Chem.Mol:
    return Chem.MolFromSmiles("O=C(O)CCCCO/N=C(\\c1ccnnc1)c1cccc(C(F)(F)F)c1")


def frob(mol: Chem.Mol):
    for atom in mol.GetAtoms():
        a: Chem.Atom = atom
        _ = a
        n: int = atom.GetAtomicNum()
        assert type(n) == int


def test_frob():
    frob(sample_mol())
