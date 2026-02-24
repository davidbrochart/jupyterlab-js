# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output jupyterlab-4.5.4-py3-none-any.whl https://files.pythonhosted.org/packages/f5/9f/a70972ece62ead2d81acc6223188f6d18a92f665ccce17796a0cdea4fcf5/jupyterlab-4.5.4-py3-none-any.whl
unzip jupyterlab-4.5.4-py3-none-any.whl
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.5.4.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.5.4.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.5.4.data/data/share/jupyter/lab/schemas share/jupyter/lab/
hatch build
hatch publish
```
