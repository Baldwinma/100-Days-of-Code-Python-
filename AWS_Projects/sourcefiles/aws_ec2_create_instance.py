# Lets create EC2 instances using Python BOTO3

import boto3

def create_ec2_instance():
    try:
        print("Creating EC2 Instance....")

        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
        ImageId = "ami-0022f774911c1d690",
        MinCount = 1,
        MaxCount = 1,
        InstanceType = "t2.micro",
        KeyName="main-key"
    )
    except Exception as e:
        print("e")

#Describing Ec2 instances
def describe_ec2_instance():
    try:
        print("Describing EC2 Instance....")

        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances()
    )
    except Exception as e:
        print("e")

#create_ec2_instance()
describe_ec2_instance()
