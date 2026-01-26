# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output jupyterlab-4.5.3-py3-none-any.whl https://files.pythonhosted.org/packages/9e/9a/0bf9a7a45f0006d7ff4fdc4fc313de4255acab02bf4db1887c65f0472c01/jupyterlab-4.5.3-py3-none-any.whl
unzip jupyterlab-4.5.3-py3-none-any.whl
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.5.3.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.5.3.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.5.3.data/data/share/jupyter/lab/schemas share/jupyter/lab/
hatch build
hatch publish
```
