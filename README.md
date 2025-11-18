# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output jupyterlab-4.4.10-py3-none-any.whl https://files.pythonhosted.org/packages/f7/46/1eaa5db8d54a594bdade67afbcae42e9a2da676628be3eb39f36dcff6390/jupyterlab-4.4.10-py3-none-any.whl
unzip jupyterlab-4.4.10-py3-none-any.whl
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.4.10.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.4.10.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.4.10.data/data/share/jupyter/lab/schemas share/jupyter/lab/
hatch build
hatch publish
```
