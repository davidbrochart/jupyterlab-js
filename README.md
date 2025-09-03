# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output jupyterlab-4.4.7-py3-none-any.whl https://files.pythonhosted.org/packages/7e/01/44f35124896dd5c73b26705c25bb8af2089895b32f057a1e4a3488847333/jupyterlab-4.4.7-py3-none-any.whl
unzip jupyterlab-4.4.7-py3-none-any.whl
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.4.7.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.4.7.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.4.7.data/data/share/jupyter/lab/schemas share/jupyter/lab/
hatch build
hatch publish
```
