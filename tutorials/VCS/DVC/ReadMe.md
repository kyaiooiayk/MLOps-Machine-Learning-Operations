# DVC (Data Version Control)
***

## What is DVC?
- DVC stands for Data Version Control and is open-source.
- Interact perfectly with Git and the combination Git/DVC is one of the most popular choice for simple versioning.
- DVC works by supplementing each data file with a corresponding metadata file (.dvc), which is used to sync with a remote repository designed for large files (All the large files, datasets, models, etc. can be stored in remote storage servers (S3, Google Drive, etc). 
- DVC supports easy-to-use commands to configure, push, pull datasets to remote storage.). 
- Git tracks the metadata file, while DVC handles the remote repository.
***

## Installation
- Installation via pip with: `pip install dvc`
***

## DVC workflow
From a very high-level point of view, DVC works as follows:
  - Make sure you run the following command in the top level folder (where the hidden `.git` folder is). A Git project is initialised as a DVC project `dvc init` and a `.dvc` and `.dvcignore` folders are created to handle the configuration (similar to the `.git` folder). Inside it, a cache folder handles the local cache.
  - Adding a data file to the DVC version control system: `dvc add <file_path>` moves the file to the local cache, letting Git track only the corresponding `.dvc` file. Further, dvc add this file to `.gitignore` automatically so git will not upload the large file.
  - Add to git only the dvc file as: `git add <file_path.dvc>`. Please note the syntax `name.dvc`.
  - Files in the local cache can be synced with a remote repository `dvc push`.
  - At any time, files can be synced from the remote repository to the local cache `dvc fetch` or from the local cache to the working folder `dvc pull`.
  - As you can see, `dvc` follows `git` pattern to `commit`, `push` and `pull` data to remote storage.
***

## Configuring Google Drive as your remote storage
- Create a folder in your Google Drive called `My_Folder_on_GoogleDrive`.
- Get the ID of this folder and the address will look like something like this: `https://drive.google.com/drive/u/0/folders/1A0zgCLZ1YF` where the ID the last alphanumeric block if this URL.
- Add this storage: `dvc remote add -d storage gdrive://1A0zgCLZ1YF`
- Check the contents of the file `.dvc/config` whether the remote storage is configured correctly or not.
***

## References
- [Quick presentation on DVC](https://docs.google.com/presentation/d/1jUFz212lZvwqDibiCRoOcm-40ANPXI1dKlF8t7PD1Is/edit#slide=id.gc521574bc2_0_2)
- [MLOps Basics [Week 3]: Data Version Control - DVC](https://www.ravirajag.dev/blog/mlops-dvc)
***
