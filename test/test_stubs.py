from rdkit import Chem
import io

from rdkit.Chem import Mol, SDWriter


def sample_mol() -> Mol:
    ret = Chem.MolFromSmiles("O=C(O)CCCCO/N=C(\\c1ccnnc1)c1cccc(C(F)(F)F)c1")
    assert ret is not None
    return ret


def frob(mol: Mol):
    for atom in mol.GetAtoms():
        a: Chem.Atom = atom
        _ = a
        n: int = atom.GetAtomicNum()
        assert type(n) == int


def sdwriter():
    t: str = SDWriter.GetText(sample_mol())
    assert type(t) == str

    bs = io.StringIO()
    writer = SDWriter(bs)
    for mol in [sample_mol(), sample_mol(), sample_mol()]:
        writer.write(mol)
    writer.close()
    first = bs.getvalue()

    bs = io.StringIO()
    with SDWriter(bs) as writer:
        for mol in [sample_mol(), sample_mol(), sample_mol()]:
            writer.write(mol)
    second = bs.getvalue()
    assert second == first

    writer = SDWriter(io.StringIO())
    writer.SetProps(["asdf"])
    writer.SetProps(("asdf",))


def test_frob():
    frob(sample_mol())
    sdwriter()
