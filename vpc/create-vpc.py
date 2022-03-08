import boto3
aws_client=boto3.client("ec2")
aws_client.create_vpc(CidrBlock='10.10.0.0/16')