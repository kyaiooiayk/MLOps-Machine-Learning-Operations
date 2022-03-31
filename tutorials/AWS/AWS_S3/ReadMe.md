# AWS S3
***
## What is AWS S3?
- S3 stands for Simple Storage Service.
-  Amazon S3 is a key-value, object-based storage service.
- Amazon S3 organizes objects into buckets; bucket names must be globally unique.
- Objects can be uploaded to Amazon S3 buckets using the AWS management console or the AWS CLI.
- You can control access to both buckets and the objects in buckets.
- Each object in Amazon S3 has a storage class associated with it. The storage class deter- mines how Amazon S3 stores the data for the object and if you will be charged additional costs to read the data.
- Amazon S3 versioning allows you to save multiple versions of an object. You are charged for the combined space occupied by all versions of a document.
***
## Accessign AWS S3 via AWS CLI
- List all the buckets in your S3 bucket: `aws s3 ls`
***
## S3-compatible alternative
- An alternative coudl  me [MINio](https://min.io/)
- MinIO offers high-performance, S3 compatible object storage. Native to Kubernetes, MinIO is the only object storage suite available on every public cloud, every Kubernetes distribution, the private cloud and the edge. MinIO is software-defined and is 100% open source under GNU AGPL v3.
***
## References
- Mishra, Abhishek. Machine Learning in the AWS Cloud: Add Intelligence to Applications with Amazon SageMaker and Amazon Rekognition. John Wiley & Sons, 2019.
- [Using high-level (s3) commands with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html)
- [YouTube video | Tutorial 1- Cloud Computing-AWS-Introduction To S3(Simple Storage Services)](https://www.youtube.com/watch?v=G3adspFQ59I)
- [YouTube video | Tutorial 3- Deployment Of ML Models In AWS EC2 Instance](https://www.youtube.com/watch?v=JKlOlDFwsao)
