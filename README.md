# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output jupyterlab-4.4.9-py3-none-any.whl https://files.pythonhosted.org/packages/1f/fd/ac0979ebd1b1975c266c99b96930b0a66609c3f6e5d76979ca6eb3073896/jupyterlab-4.4.9-py3-none-any.whl
unzip jupyterlab-4.4.9-py3-none-any.whl
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.4.9.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.4.9.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.4.9.data/data/share/jupyter/lab/schemas share/jupyter/lab/
hatch build
hatch publish
```
