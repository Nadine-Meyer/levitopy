---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Overview

This is an example notebook to go through the basics of Levitopy

```python

# import some basic libraries
import numpy as np
import matplotlib.pyplot as plt
import sys

# from tqdm import tqdm
from pathlib import Path

# to work with your local version of levitopy uncomment the following
local_path = str(Path('~/PycharmProjects/levitopy/').expanduser())
if local_path not in sys.path:
    sys.path = [local_path] +sys.path

%matplotlib inline

from pathlib import Path

%load_ext autoreload

%autoreload 2


import levitopy  # import levitopy

print('levitopy version is: ', levitopy.__version__)  # check the version
# print('levitopy located at: ', levitopy.__path__)

```

```python

```
