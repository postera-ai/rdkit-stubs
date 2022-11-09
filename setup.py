from collections.abc import Iterable
from setuptools import setup
import os
from typing import List
from pathlib import Path


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


setup(
    name="rdkit-stubs",
    version="0.1",
    description="type stubs for rdkit",
    author="Andrew Dirksen",
    author_email="andrew@dirksen.com",
    license="MIT OR Apache-2.0",
    url="https://github.com/postera-ai/rdkit-stubs",
    packages=["rdkit-stubs"],
    package_data={"rdkit-stubs": list_package_files()},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Typing :: Stubs Only",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=["rdkit==2022.03.3"],
)
