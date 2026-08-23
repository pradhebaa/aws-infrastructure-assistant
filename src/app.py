from tools.ec2 import get_ec2_instances

def main():
    instances = get_ec2_instances()

    print("\nEC2 Instances")
    print("-" * 50)

    for instance in instances:
        print(f"Name:    {instance['name']}")
        print(f"ID:      {instance['id']}")
        print(f"State:   {instance['state']}")
        print(f"Type:    {instance['instance_type']}")
        print("-" * 50)


if __name__ == "__main__":
    main()