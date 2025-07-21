# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output jupyterlab-4.4.5-py3-none-any.whl https://files.pythonhosted.org/packages/47/74/e144ce85b34414e44b14c1f6bf2e3bfe17964c8e5670ebdc7629f2e53672/jupyterlab-4.4.5-py3-none-any.whl
unzip jupyterlab-4.4.5-py3-none-any.whl
rm -rf share
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.4.5.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.4.5.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.4.5.data/data/share/jupyter/lab/schemas share/jupyter/lab/
hatch build
hatch publish
```
