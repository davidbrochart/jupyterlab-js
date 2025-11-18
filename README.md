# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output jupyterlab-4.5.0-py3-none-any.whl https://files.pythonhosted.org/packages/6c/1e/5a4d5498eba382fee667ed797cf64ae5d1b13b04356df62f067f48bb0f61/jupyterlab-4.5.0-py3-none-any.whl
unzip jupyterlab-4.5.0-py3-none-any.whl
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.5.0.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.5.0.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.5.0.data/data/share/jupyter/lab/schemas share/jupyter/lab/
hatch build
hatch publish
```
