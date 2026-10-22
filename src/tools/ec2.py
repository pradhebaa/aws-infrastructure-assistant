
import boto3


def get_instance_name(instance):
    """Return the EC2 Name tag, or 'Unnamed' if it is missing."""
    for tag in instance.get("Tags", []):
        if tag.get("Key") == "Name":
            return tag.get("Value", "Unnamed")

    return "Unnamed"


def get_ec2_instances(ec2_client=None):
    """
    Return EC2 inventory across all pages.

    """
    if ec2_client is None:
        ec2_client = boto3.client("ec2")

    paginator = ec2_client.get_paginator("describe_instances")

    instances = []

    for page in paginator.paginate():
        for reservation in page.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                instances.append({
                    "id": instance["InstanceId"],
                    "name": get_instance_name(instance),
                    "state": instance["State"]["Name"],
                    "instance_type": instance["InstanceType"],
                })

    return instances

