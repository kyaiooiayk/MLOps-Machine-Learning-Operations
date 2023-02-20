# DVC (Data Version Control)
***

## What is DVC?
- DVC stands for Data Version Control and is open-source.
- Interact perfectly with Git and the combination Git/DVC is one of the most popular choice for simple versioning.
- DVC works by supplementing each data file with a corresponding metadata file (.dvc), which is used to sync with a remote repository designed for large files (e.g., AWS). Git tracks the metadata file, while DVC handles the remote repository.
***

## DVC workflow
From a very high-level point of view, DVC works as follows:
  - A Git project is initialized as a DVC project `dvc init` and a `.dvc` folder is created to handle the configuration (similar to the `.git` folder). Inside it, a cache folder handles the local cache.
  - Adding a data file to the DVC version control system: `dvc add <file_path>` moves the file to the local cache, letting Git track only the corresponding `.dvc` file. Further, dvc add this file to `.gitignore` automatically so git will not upload the large file.
  - Add to git only the dvc file as: `git add <file_path.dvc>`. Please note the syntax `name.dvc`.
  - Files in the local cache can be synced with a remote repository `dvc push`.
  - At any time, files can be synced from the remote repository to the local cache `dvc fetch` or from the local cache to the working folder `dvc pull`.
***

## References
- [Quick presentation on DVC](https://docs.google.com/presentation/d/1jUFz212lZvwqDibiCRoOcm-40ANPXI1dKlF8t7PD1Is/edit#slide=id.gc521574bc2_0_2)
- [MLOps Basics [Week 3]: Data Version Control - DVC](https://www.ravirajag.dev/blog/mlops-dvc)
***
