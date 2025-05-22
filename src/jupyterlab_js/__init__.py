import importlib.metadata


try:
    __version__ = importlib.metadata.version("jupyterlab_js")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"

