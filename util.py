import re
import argparse
import importlib
from io import BytesIO
from pathlib import Path
from typing import Optional
from zipfile import ZipFile
from urllib.request import urlopen

DOC = "https://github.com/hlovatt/PyBoardTypeshed/archive/master.zip"
MOD = "https://github.com/Josverl/micropython-stubs/archive/refs/heads/main.zip"


def get_archive(url: str) -> ZipFile:
    """Get and read a zip archive"""
    with urlopen(url) as response:
        data = ZipFile(BytesIO(response.read()))
    return data


def write_paths(root: str, paths: list[str], archive: ZipFile):
    """Write selected archive files"""
    for path in paths:
        if path not in archive.namelist():
            continue

        if endpoint := destination(Path(path).name):
            out = Path(root) / endpoint

            # ensure parent directory exists
            Path(out.parent).mkdir(parents=True, exist_ok=True)

            out.write_bytes(archive.read(path))


def get_doc_stubs(root: str):
    print("collecting stubs from 'hlovatt/PyBoardTypeshed'")

    archive = get_archive(DOC)
    paths = [path for path in archive.namelist() if path.endswith(".pyi")]

    write_paths(root, paths, archive)


def get_mod_stubs(root: str):
    print("collecting stubs from 'Josverl/micropython-stubs'")

    archive = get_archive(MOD)
    pattern = re.compile(r".*docstubs\/.*\.py$")
    paths = [path for path in archive.namelist() if pattern.match(path)]

    write_paths(root, paths, archive)


def add_missing(root: str):
    """"""
    # Josverl/micropython-stubs does not contain all,
    # complement hlovatt/PyBoardTypeshed added stubs
    for module in Path(root).iterdir():
        file = module / "__init__.py"

        if not file.exists():
            file.touch()


def destination(stub: str) -> Optional[Path]:
    """Determine stub path

    Only handle micropython stubs, ignoring
    any cPython stdlib equivalents.
    """
    prefix, _, suffix = stub.partition(".")

    if importlib.util.find_spec(prefix):  # type: ignore
        return  # in cPython stdlib, skip

    prefix = Path(prefix)

    if suffix in ("py", "pyi"):  # module
        return prefix / f"__init__.{suffix}"
    return prefix / suffix  # module member


def collect(root: str):
    """Get and populate stubs"""
    lockfile = Path(root) / "collect.lock"
    if lockfile.exists():
        print("stubs already collected")
    else:
        get_doc_stubs(root)
        get_mod_stubs(root)
        add_missing(root)
        lockfile.touch()


parser = argparse.ArgumentParser("Collect stubs")
parser.add_argument("--dest", type=str, default="src", help="Stub source directory")

args = parser.parse_args()
collect(args.dest)
