import sys
from subprocess import check_output

import toml


version = sys.argv[1]

check_output("git clean -fdx".split())
check_output(f"curl -L --output jupyterlab-{version}-py3-none-any.whl https://pypi.org/packages/py3/j/jupyterlab/jupyterlab-{version}-py3-none-any.whl".split())
check_output(f"unzip jupyterlab-{version}-py3-none-any.whl".split())
check_output("mkdir -p share/jupyter/lab".split())
check_output(f"cp -r jupyterlab-{version}.data/data/share/jupyter/lab/static share/jupyter/lab/".split())
check_output(f"cp -r jupyterlab-{version}.data/data/share/jupyter/lab/themes share/jupyter/lab/".split())
check_output(f"cp -r jupyterlab-{version}.data/data/share/jupyter/lab/schemas share/jupyter/lab/".split())

with open("pyproject.toml", "rt") as f:
    data = toml.load(f)

with open("pyproject.toml", "wt") as f:
    data["project"]["version"] = version
    toml.dump(data, f)

check_output("hatch build".split())
check_output("hatch publish".split())
check_output(["git", "commit", "-am", f"Release v{version}"])
check_output("git push".split())
