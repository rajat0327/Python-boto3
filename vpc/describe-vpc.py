import boto3
aws_client=boto3.client("ec2")
#Describe all the vpc present in the specific region
vpc=aws_client.describe_vpcs()
vpc_list=vpc["Vpcs"]
number_of_vpc=len(vpc_list)
print("number of vpcs " + str(number_of_vpc))
print("=================================")
for vpc in vpc_list:
    print("VPC ID : " + str(vpc["VpcId"]))
    print("Cidr Block : " + vpc["CidrBlock"])
    print("=================================")

# Describe vpc based on vpcid
vpc_1=aws_client.describe_vpcs(VpcIds=["vpc-9d0738e5"])
print(vpc_1)