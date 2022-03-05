import imp
import boto3
aws_client=boto3.client("s3")
bucket_list=aws_client.list_buckets()["Buckets"]
firstBucket=bucket_list[0]["Name"]
#delete single object
#aws_client.delete_object(Bucket=firstBucket,Key='image.png')
#delete multiple object
objects=aws_client.list_objects(Bucket=firstBucket)["Contents"]
for object in objects:
    name=object["Key"]
    aws_client.delete_object(Bucket=firstBucket,Key=name)