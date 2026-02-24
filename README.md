# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output jupyterlab-4.5.5-py3-none-any.whl https://files.pythonhosted.org/packages/b9/52/372d3494766d690dfdd286871bf5f7fb9a6c61f7566ccaa7153a163dd1df/jupyterlab-4.5.5-py3-none-any.whl
unzip jupyterlab-4.5.5-py3-none-any.whl
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.5.5.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.5.5.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.5.5.data/data/share/jupyter/lab/schemas share/jupyter/lab/
hatch build
hatch publish
```
