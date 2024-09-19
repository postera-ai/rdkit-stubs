publish:
    # https://realpython.com/pypi-publish-python-package/
    # assert there are no uncommitted changes
    git diff-index --quiet HEAD
    # assert we are on main
    git branch --show-current | grep '^main$'
    rm -rf dist rdkit-stubs.egg-info
    pyproject-build # pipx install build
    twine upload dist/* # pipx install twine

test:
    ./test/test.bash

fmt:
    black .

