import boto3
aws_client=boto3.client("s3")
bucket_list=aws_client.list_buckets()["Buckets"]
print("=========================")
for buckets in bucket_list:
    print("Name - " + buckets["Name"])
    print("Creation date - " + str(buckets["CreationDate"]))
    print("=========================")