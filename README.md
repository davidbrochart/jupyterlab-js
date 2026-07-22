# jupyterlab-js

A Python package distributing JupyterLab's static assets only, with no Python dependency.

```bash
git clean -fdx
curl --output jupyterlab-4.6.1-py3-none-any.whl https://files.pythonhosted.org/packages/5a/81/90ac6cc31d248e83a0d1eab343a5e6e68bc783d3f74fbe61640f42a61da4/jupyterlab-4.6.1-py3-none-any.whl
unzip jupyterlab-4.6.1-py3-none-any.whl
mkdir -p share/jupyter/lab
cp -r jupyterlab-4.6.1.data/data/share/jupyter/lab/static share/jupyter/lab/
cp -r jupyterlab-4.6.1.data/data/share/jupyter/lab/themes share/jupyter/lab/
cp -r jupyterlab-4.6.1.data/data/share/jupyter/lab/schemas share/jupyter/lab/
# change version in `pyproject.toml`
hatch build
hatch publish
# git commit -am "Release v4.6.1"
# git push
```
