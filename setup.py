import os
from collections.abc import Iterable
from pathlib import Path
from typing import List

from setuptools import setup


def walk_files(root_dir: Path) -> Iterable[Path]:
    for root, dirs, files in os.walk(root_dir):
        _ = dirs
        for filename in files:
            yield Path(root) / filename


def list_package_files() -> List[str]:
    root = Path("rdkit-stubs")
    return sorted(
        str(filepath.relative_to(root))
        for filepath in walk_files(root)
        if filepath.suffix == ".pyi"
    )


long_description = (Path(__file__).parent.resolve() / "README.md").read_text(
    encoding="utf-8"
)


setup(
    name="rdkit-stubs",
    version="0.4",
    description="type stubs for rdkit",
    author="Andrew Dirksen, Ryan Rightmer",
    author_email="andrew@dirksen.com, rrightmer@gmail.com",
    license="MIT OR Apache-2.0",
    url="https://github.com/postera-ai/rdkit-stubs",
    packages=["rdkit-stubs"],
    package_data={"rdkit-stubs": list_package_files()},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Typing :: Stubs Only",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=["rdkit"],
    long_description=long_description,
)
