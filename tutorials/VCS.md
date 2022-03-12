# VCS (Version Control System)

## CI vs. CD
- **Continuous Integration (CI)**: The code is built and tested on a regular basis, i.e. daily, several times per day, or – even better – with every commit.
- **Continuous Delivery (CD)**: This is the next step, and its goal is to always have code available that can be released at any point. CD uses some automation (building and testing) but requires human intervention in the end when it comes to releasing to a productive environment.
- **Continuous Deployment (CD)**: All code changes are automatically built, tested, and released. It's similar to continuous delivery but also brings the new version to the production environment without human intervention.
- All three methods rely on a version control system – there is no way around it.

## GitHub vs. GitLab
- GIT stands for Global Information Tracker
- The most significant difference between the GitHub and Git Lab is that while GitHub is a collaboration platform that helps review and manage codes remotely, GitLab is majorly focused on DevOps and CI/CD.
- GitHub is more popular amongst the developers as it holds millions of repositories, but recently GitLab has been gaining popularity, as the company continues to add new features to make it more competitive and user-friendly.

## Semantic versioning of package
- Let's say we donwload a python package named `ML_Mine` version `0.19.2`. What do those numbers really mean?
  - `0.19.2` The first number in this chain is called the major version. when there's backwards incompatible changes, i.e. changes that break the old API are released. Usually, when major versions are released.
  - `(0.19.2)` The second number is called the minor version. When backwards compatible changes. Functionality is added (or speed improvements) that does not break any existing functionality, at least the public API that end- users would use
  - `(0.19.2)` The third number is called the patch version. backwards compatible bug fixes

## References
- [DS is software](https://nbviewer.org/github/ethen8181/machine-learning/blob/master/data_science_is_software/notebooks/data_science_is_software.ipynb)
