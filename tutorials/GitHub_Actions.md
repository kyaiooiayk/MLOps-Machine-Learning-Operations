# GitHub Actions
***

## GitHub Actions
- **CI/CD** is a coding philosophy and set of practices with which you can continuously build, test, and deploy iterative code changes.
- **CI** is about how the project should be built and tested in various runtimes, automatically and continuously. 
- **CD** is needed so that every new bit of code that passes automated testing can be released into production with no extra effort.
- If you are using GitHub to version control your code, you can use GitHub Actions right off the bat without having the need to setup another tool.
- GitHub Actions are just a set instructions declared using `yaml` files.
- These files needs to be in a specific folder: `.github/workflows` and this has to be in the root directory (where `.git` hidden folder is present).
- There are 5 main concepts in GitHub Actions:
    - **Event** which is an event that triggers for workflow.
    - **Job** defines the steps to run when a workflow is triggered. A workflow can contain multiple jobs.
    - **Runner** defines where to run the code. By default, github will run the code in it's own servers.
    - **Step** contains actions to run. Each job can contains multiple steps to run.
    - **Action** contains actual commands to run like installing dependencies, testing code, etc.
 
![image](https://user-images.githubusercontent.com/89139139/220193508-774b645e-664d-49ee-89a8-8d83442ac879.png)
***

## References
- [Working example of how to trigger GitHub actions](https://github.com/kyaiooiayk/CI-CD-Pipeline-with-GitHub-Actions)
- [How to Build MLOps Pipelines with GitHub Actions - Step by Step Guide](https://neptune.ai/blog/build-mlops-pipelines-with-github-actions-guide)
- [MLOps Basics [Week 6]: CI/CD - GitHub Actions](https://www.ravirajag.dev/blog/mlops-github-actions)
- ***
