import boto3
aws_client=boto3.client("s3")
bucket_list=aws_client.list_buckets()["Buckets"]
firstBucket=bucket_list[0]["Name"]
response=aws_client.get_bucket_policy(Bucket=firstBucket)
bucket_policy=response["Policy"]
print(bucket_policy)