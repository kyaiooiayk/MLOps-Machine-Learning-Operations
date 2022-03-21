# How to deploy a ML app on an AWS EC2 instance

## What is an EC2 instance?
- EC2 (Amazon's Elastic Compute Cloud) instance is a virtual server for running applications on the Amazon Web Services (AWS) infrastructure. It provides secure, resizable compute capacity in the cloud.
- Depending on which hardware you request, it can cost you approximately up to $3USD/hour.

## Tips and Tricks on AWS
- Design a suite of experiments to run beforehand as you paying as soon as you reserve the instance.
- Do not ask for an EC2 instance that has 4 GPU but run a job only on 1 GPU. Do your homework before and plan the experience in a way that, once you reserve an EC2 instance you run a script for each GPU or a single script for all GPUs.
- Run scripts as a background process using `nohup`. This is defined specifically if you are working with server. An alternative to `screen` is `nohup` and you can read about what is difference [here](https://unix.stackexchange.com/questions/24658/nohup-vs-screen).
- If you want to kill a speicific job running under a `nohup` section use this: `ps -eaf | grep "nohup" | grep "your proc name/keyword".`


## Reference
- [The Fastest Way to Deploy Your ML App on AWS with Zero Best Practices](https://towardsdatascience.com/the-fastest-way-to-deploy-your-ml-app-on-aws-with-zero-best-practices-df15c09eead7)
- [Simple way to deploy machine learning models to cloud](https://towardsdatascience.com/simple-way-to-deploy-machine-learning-models-to-cloud-fd58b771fdcf)
- [How to Train Keras Deep Learning Models on AWS EC2 GPUs (step-by-step)](https://machinelearningmastery.com/develop-evaluate-large-deep-learning-models-keras-amazon-web-services/)
