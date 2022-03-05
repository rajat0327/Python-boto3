import boto3
aws_resource=boto3.resource("s3")
list_bucket=list(aws_resource.buckets.all())
for bucket in list_bucket:
    print(bucket.name)