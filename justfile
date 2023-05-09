publish:
    # https://realpython.com/pypi-publish-python-package/
    # assert there are no uncommitted changes
    git diff-index --quiet HEAD
    # assert we are on main
    git branch --show-current | grep '^main$'
    # remove any previous builds
    rm -rf dist rdkit-stubs.egg-info
    # build
    pyproject-build # pipx install build
    # upload
    twine upload dist/* # pipx install twine
