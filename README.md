# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output jupyterlab-4.5.1-py3-none-any.whl https://files.pythonhosted.org/packages/af/c3/acced767eecc11a70c65c45295db5396c4f0c1937874937d5a76d7b177b6/jupyterlab-4.5.1-py3-none-any.whl
unzip jupyterlab-4.5.1-py3-none-any.whl
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.5.1.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.5.1.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.5.1.data/data/share/jupyter/lab/schemas share/jupyter/lab/
hatch build
hatch publish
```
