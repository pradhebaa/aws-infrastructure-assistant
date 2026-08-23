import boto3

ec2 = boto3.client("ec2")

def get_instance_name(instance):
    for tag in instance.get("Tags", []):
        if tag["Key"] == "Name":
            return tag["Value"]

    return "Unnamed"


def get_ec2_instances():
    response = ec2.describe_instances()

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append({
                "id": instance["InstanceId"],
                "name": get_instance_name(instance),
                "state": instance["State"]["Name"],
                "instance_type": instance["InstanceType"],
            })
    return instances
