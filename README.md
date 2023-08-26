## Introduction

This repository contains my solution to the ["llama"](https://www.kaggle.com/competitions/llama/) challenge, hosted in Kaggle.

## Installation

First, download the code (and its submodules):

```bash
git clone --recurse-submodules git@github.com:IamGianluca/...
```

For reproducibility, we included a Docker image we used to develop and test the application. We defined the Machine Learning pipeline in [DVC](https://dvc.org/), a version control system for machine learning projects.

You must copy your personal `kaggle.json` file to the project's main directory. This file is used to authenticate to the Kaggle API, and download the competition data from inside the Docker container.

```bash
cp ~/.kaggle/kaggle.json .
```

Build the Docker image and start the Docker container.

```bash
make build && make start
```

Start an interactive bash shell in the container.

```bash
make attach
``` 

Reproduce the DVC pipeline.

```bash
dvc repro
```

## Contribute

Here is a brief description of what each folder contains:
* `ckpt`: model checkpoints
* `data`: input and pre-processed data
* `mtrc`: metrics
* `nbs`: notebooks for exploration analyses
* `pipe`: Python scripts for each step in the DVC pipeline
* `pred`: predictions
* `blazingai`: source code for companion library

Other important files are:
* `dvc.yaml`:  list input, output, and parameters used by each DVC step
* `params.yaml`: parameters used for DVC steps

The companion library (`blazingai`) is installed in editable mode. Which means you don't need to rebuild the Docker container every time you make a change to it.

#### Commit labels

When contributing to this repository, please consider using the following convention to label your commit messages.

* `BUG`: bug fixing
* `DEV`: development environment ― e.g., Docker, TensorBoard, system dependencies
* `DOC`: documentation
* `EDA`: exploratory data analysis
* `ML`: modeling, feature engineering
* `MAINT`: maintenance ― e.g., refactoring
* `OPS`: MLOps ― e.g., download, unzip, pre- and post-process data

## Tools

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)
- [NVIDIA NGC](https://ngc.nvidia.com/) 
- [DVC](https://github.com/iterative/dvc)
- [PyTorch](https://github.com/pytorch/pytorch)
- [PyTorch Lightning](https://github.com/PyTorchLightning/pytorch-lightning)
- [timm](https://github.com/rwightman/pytorch-image-models/tree/master/timm)
