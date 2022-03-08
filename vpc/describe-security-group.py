import boto3
aws_client=boto3.client("ec2")
sg_list=aws_client.describe_security_groups()
print("number of sg : " +str(len(sg_list["SecurityGroups"])))
print("===========================")
for sg in sg_list["SecurityGroups"]:
    print("sg id : " + sg["GroupId"])
    print("sg name : " + sg["GroupName"])
    print("vpc id : " + sg["VpcId"])
    #try:
     #   print("tag : " + sg["Tags['Value']"])
    #except:
    #    print("no tags present")
    print("===========================")