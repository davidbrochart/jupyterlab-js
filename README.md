# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output jupyterlab-4.5.2-py3-none-any.whl https://files.pythonhosted.org/packages/a4/78/7e455920f104ef2aa94a4c0d2b40e5b44334ee7057eae1aa1fb97b9631ad/jupyterlab-4.5.2-py3-none-any.whl
unzip jupyterlab-4.5.2-py3-none-any.whl
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.5.2.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.5.2.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.5.2.data/data/share/jupyter/lab/schemas share/jupyter/lab/
hatch build
hatch publish
```
