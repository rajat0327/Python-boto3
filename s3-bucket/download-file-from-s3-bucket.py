import boto3
import os
aws_client=boto3.client("s3")
bucket_list=aws_client.list_buckets()["Buckets"]
firstBucket=bucket_list[0]["Name"]
objects=aws_client.list_objects(Bucket=firstBucket)["Contents"]
cwd=os.getcwd()
cwd=cwd+"/../files/"
for object in objects:
    name=object["Key"]
    filename=cwd+name
    aws_client.download_file(Bucket=firstBucket,Key=name,Filename=filename)