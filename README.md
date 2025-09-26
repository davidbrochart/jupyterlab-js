# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output jupyterlab-4.4.8-py3-none-any.whl https://files.pythonhosted.org/packages/d1/3b/82d8c000648e77a112b2ae38e49722ffea808933377ea4a4867694384774/jupyterlab-4.4.8-py3-none-any.whl
unzip jupyterlab-4.4.8-py3-none-any.whl
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.4.8.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.4.8.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.4.8.data/data/share/jupyter/lab/schemas share/jupyter/lab/
hatch build
hatch publish
```
