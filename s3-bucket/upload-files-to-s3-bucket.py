import boto3
import os
import glob
aws_client=boto3.client("s3")
bucket_list=aws_client.list_buckets()["Buckets"]
firstBucket=bucket_list[0]["Name"]
#how to upload single files
cmd=os.getcwd()
filepath=cmd+"/../files/image2.jpeg"
aws_client.upload_file(Bucket=firstBucket,Filename=filepath,Key="uploaded-image2.jpeg")
#how to upload multiple files
cwd=os.getcwd()
cwd=cwd+"/../files/"
files=glob.glob(cwd+"*")
for file in files:
    aws_client.upload_file(Bucket=firstBucket,Filename=file,Key=file.split("/")[-1])