# AWS Lambda

## What is a serverless lambda?
AWS Lambda is the only Amazon compute option that remains free after one year. It’s also arguably the best option for a service that will scale smoothly to handle thousands, millions, or billions of requests. Choosing Lambda from the beginning sets your application up for success in the future. Pay attention that this is AWS services in the free tier come with a limit, usually enforced each month. Some of these seem impossibly large like AWS Lambda’s grant of one million function calls. A million can come pretty soon if you’re not careful, so make sure you actually monitor this.

Lambda is a serverless compute service that lets your code without provisioning or managing servers. “Serverless” doesn’t mean there is no server, it just means that you don’t care about the underlying infrastructure for your code and you only pay for what you use. Just upload your code as a ZIP file or container image, and Lambda automatically and precisely allocates compute execution power and runs your code based on the incoming request or event, for any scale of traffic. This is how AWS Lambda works:

  - You upload your code to Lambda.
  - You set your code to trigger from an event source, such as AWS services, mobile applications, or HTTP endpoints.
  - Lambda runs your code only when triggered. The trigger part is key to understand how they work.
  - You pay only for the compute time that you use. In the previous example of resizing images, you would pay only for the compute time that you use when uploading new images. Uploading the images triggers Lambda to run code for the image resizing function.

**In conclusion**, since developers do not need to manage infrastructure, serverless implementation of code has the benefit of increasing productivity as developers can spend more time writing code. 

## Step-by-step procedure
- 

## References
- [Is the AWS Free Tier really free?](https://www.lastweekinaws.com/blog/is-the-aws-free-tier-really-free/)
