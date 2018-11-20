# Boto 3
import boto3
ec2 = boto3.resource('ec2')
import requests
import time

print("Starting...")
start_time = time.perf_counter()
start_time = time.perf_counter()
result = ec2.create_instances(ImageId='ami-071efb15d7b5473d2', MinCount=1, MaxCount=1,
                              InstanceType='t1.micro',
                              KeyName='aws_key',
                              SecurityGroupIds=['sg-0249cc101918e885a',]
                              )
print(result)
instance = result[0]
new_instance_id = instance.id


client = boto3.client('ec2')
# waiter = client.get_waiter('instance_status_ok')
waiter = client.get_waiter('instance_running')
waiter.wait(InstanceIds=[new_instance_id])

creation_time = time.perf_counter()
print("Instance {} started after: {} s".format(new_instance_id, creation_time - start_time))
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}],
    InstanceIds=[new_instance_id])

for instance in instances:
    ip_address = instance.public_ip_address
    print("connecting to {}".format(ip_address))
    url = "http://{}:8000".format(ip_address)
    r = requests.get(url)
    print("Index page of {}".format(url))
    print(r.text)

    print("Terminating {}".format(new_instance_id))
    instance.terminate()
    waiter = client.get_waiter('instance_terminated')
    waiter.wait(InstanceIds=[new_instance_id])
    print("Instance {} terminated.".format(new_instance_id))
