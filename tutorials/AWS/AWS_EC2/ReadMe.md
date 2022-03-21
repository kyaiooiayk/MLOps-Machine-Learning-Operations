# How to deploy a ML app on an AWS EC2 instance

## What is an EC2 instance?
- EC2 (Amazon's Elastic Compute Cloud) instance is a virtual server for running applications on the Amazon Web Services (AWS) infrastructure. It provides secure, resizable compute capacity in the cloud.
- Depending on which hardware you request, it can cost you approximately up to $3USD/hour.

## Tips and Tricks on AWS
- Design a suite of experiments to run beforehand as you paying as soon as you reserve the instance.
- Do not ask for an EC2 instance that has 4 GPU but run a job only on 1 GPU. Do your homework before and plan the experience in a way that, once you reserve an EC2 instance you run a script for each GPU or a single script for all GPUs.
- Run scripts as a background process using `nohup`. This is defined specifically if you are working with server. An alternative to `screen` is `nohup` and you can read about what is difference [here](https://unix.stackexchange.com/questions/24658/nohup-vs-screen).
- If you want to kill a speicific job running under a `nohup` section use this: `ps -eaf | grep "nohup" | grep "your proc name/keyword".`

## Command Line Recipes
- Log into your AWS server from your PC (Your SSH key must have the permissions 600): `ssh -i aws-keypair.pem ec2-<your_user_name>@<your_ip_address>`
- Copy files from your PC AWS server: `scp -i aws-keypair.pem my_script.py ec2-<your_user_name>@<your_ip_address>:~/`
- Download from AWS server to your PC: `scp -i aws-keypair.pem ec2-<your_user_name>@<your_ip_address>:~/*.png`
- Run script as background process: `nohup python /home/ec2-user/my_script.py >/home/ec2-<your_user_name>/,y_script.py.log </dev/null 2>&1 &`
- Run script on a specific GPU on the server (With CUDA, you can specify which GPU device to use with `CUDA_VISIBLE_DEVICES`): `CUDA_VISIBLE_DEVICES=0 python /home/ec2-<your)user_name>/my_script.py `
- Monitor system and process performance on the server: for all the server `top -M` or for a single script if you know the PID `top -p <PID> -M`
- Check what scripts are running on the server: `watch "ps -ef | grep python"`

## Reference
- [The Fastest Way to Deploy Your ML App on AWS with Zero Best Practices](https://towardsdatascience.com/the-fastest-way-to-deploy-your-ml-app-on-aws-with-zero-best-practices-df15c09eead7)
- [Simple way to deploy machine learning models to cloud](https://towardsdatascience.com/simple-way-to-deploy-machine-learning-models-to-cloud-fd58b771fdcf)
- [How to Train Keras Deep Learning Models on AWS EC2 GPUs (step-by-step)](https://machinelearningmastery.com/develop-evaluate-large-deep-learning-models-keras-amazon-web-services/)
- [https://machinelearningmastery.com/command-line-recipes-deep-learning-amazon-web-services/](https://machinelearningmastery.com/command-line-recipes-deep-learning-amazon-web-services/)
