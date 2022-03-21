# How to deploy a ML app on an AWS EC2 instance

## What is an EC2 instance?
- EC2 (Amazon's Elastic Compute Cloud) instance is a virtual server for running applications on the Amazon Web Services (AWS) infrastructure. It provides secure, resizable compute capacity in the cloud.
- Depending on which hardware you request, it can cost you approximately something less than $1USD/hour up to $3USD/hour.

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

## Account setup
- Create an account at the [Amazon Web Services](https://aws.amazon.com/) portal. You will need to provide a valid credit card as this service is NOT free of charge.

## Step-by-step to launch an EC2 instance
- Click on EC2 for launching a new virtual server.
- Click the “Launch Instance” button.
- Click “Community AMIs”. An AMI is an Amazon Machine Image. It is a frozen instance of a server that you can select and instantiate on a new virtual server.
- Select “Deep Learning AMI” in the “Search community AMIs” search box and press enter. This instance is specifically designed and maintained by AWS for DL purpouses.
- Click “Select” to choose the AMI in the search result.
- Select the hardware on which to run the image. Scroll down and select the “p3.2xlarge” hardware. This includes a Tesla V100 GPU that we can use to significantly increase the training speed of our models. It also includes 8 CPU Cores, 61GB of RAM and 16GB of GPU RAM.
- Click “Review and Launch” to finalize the configuration of your server instance. Click the “Launch” button.
- Select Your Key Pair. Restrict the access permissions on your key pair file with `chmod 600 aws-keypair.pem`
- Click “View Instances” in your Amazon EC2 console and copy your `Public IP`.
- Open a Terminal and and Login to your server using SSH, for example: `ssh -i aws-keypair.pem ec2-<your_user_name>@<your_ip_address>`

## Reference
- [The Fastest Way to Deploy Your ML App on AWS with Zero Best Practices](https://towardsdatascience.com/the-fastest-way-to-deploy-your-ml-app-on-aws-with-zero-best-practices-df15c09eead7)
- [Simple way to deploy machine learning models to cloud](https://towardsdatascience.com/simple-way-to-deploy-machine-learning-models-to-cloud-fd58b771fdcf)
- [How to Train Keras Deep Learning Models on AWS EC2 GPUs (step-by-step)](https://machinelearningmastery.com/develop-evaluate-large-deep-learning-models-keras-amazon-web-services/)
- [https://machinelearningmastery.com/command-line-recipes-deep-learning-amazon-web-services/](https://machinelearningmastery.com/command-line-recipes-deep-learning-amazon-web-services/)
