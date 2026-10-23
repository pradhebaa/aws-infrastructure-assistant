
from tools.ec2 import get_stopped_instances


def main():
    instances = get_stopped_instances()

    print("\nStopped EC2 Instances")
    print("-" * 50)

    if not instances:
        print("No stopped instances found.")
        return

    for instance in instances:
        print(f"Name:    {instance['name']}")
        print(f"ID:      {instance['id']}")
        print(f"Type:    {instance['instance_type']}")
        print("-" * 50)


if __name__ == "__main__":
    main()
