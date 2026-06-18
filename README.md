# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output jupyterlab-4.6.0-py3-none-any.whl https://files.pythonhosted.org/packages/0a/eb/aa48075d0aa3d0188db34ba2704f53791757743c0bb02e18c4eef989b6de/jupyterlab-4.6.0-py3-none-any.whl
unzip jupyterlab-4.6.0-py3-none-any.whl
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.6.0.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.6.0.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.6.0.data/data/share/jupyter/lab/schemas share/jupyter/lab/
# change version in `pyproject.toml`
hatch build
hatch publish
```
