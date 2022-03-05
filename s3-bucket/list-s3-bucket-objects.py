import boto3
aws_client=boto3.client("s3")
bucket_list=aws_client.list_buckets()["Buckets"]
firstBucket=bucket_list[0]["Name"]
objects=aws_client.list_objects(Bucket=firstBucket)["Contents"]
print("================================")
for object in objects:
    print("Name : " + object["Key"])
    print("Size : " + str(object["Size"]))
    print("Last Modified : " + str(object["LastModified"]))
    print("================================")