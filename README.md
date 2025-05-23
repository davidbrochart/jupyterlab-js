# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
curl --output jupyterlab-4.4.2-py3-none-any.whl https://files.pythonhosted.org/packages/f6/ae/fbb93f4990b7648849b19112d8b3e7427bbfc9c5cc8fdc6bf14c0e86d104/jupyterlab-4.4.2-py3-none-any.whl
unzip jupyterlab-4.4.2-py3-none-any.whl
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.4.2.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.4.2.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.4.2.data/data/share/jupyter/lab/schemas share/jupyter/lab/
hatch build
hatch publish
```
