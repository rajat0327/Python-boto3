import boto3
aws_client=boto3.client("s3")
bucket_list=aws_client.list_buckets()["Buckets"]
firstBucket=bucket_list[0]["Name"]
aws_client.delete_bucket_policy(Bucket=firstBucket)