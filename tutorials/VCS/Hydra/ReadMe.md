# Hydra
***

## Introduction
- Hydra operates on top of OmegaConf, which is a YAML based hierarchical configuration system, with support for merging configurations from multiple sources (files, CLI argument, environment variables) providing a consistent API regardless of how the configuration was created.
- The fact it can merge different sources, and overwrite some of them is what makes hydra different from a simple yaml file.
***

## Installation
- Get the a list of virtual environments: `conda env list`
- Chose one virutal env: `conda activate <my_virtual_env>`
- Install hydra: `pip instll hydra-core`
- Install the hydra colour plugin: `pip install hydra_colorlog`
***

## References
- [Hydra applied to a DL model](https://github.com/sscardapane/reprodl2021/tree/exercise2_hydra)
- [MLOps Basics [Week 2]: Configurations - Hydra](https://www.ravirajag.dev/blog/mlops-hydra-config)
***
