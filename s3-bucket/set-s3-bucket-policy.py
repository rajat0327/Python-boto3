from email.policy import Policy
import boto3
import json
aws_client=boto3.client("s3")
bucket_list=aws_client.list_buckets()["Buckets"]
firstBucket=bucket_list[0]["Name"]
bucket_policy={
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Statement1",
			"Principal": "*",
			"Effect": "Allow",
			"Action": [
			    "s3:GetObject"
			    ],
			"Resource": [
			    "arn:aws:s3:::rajat11111111/*"
			    ]
		}
	]
}
bucket_policy=json.dumps(bucket_policy)
aws_client.put_bucket_policy(Bucket=firstBucket,Policy=bucket_policy)