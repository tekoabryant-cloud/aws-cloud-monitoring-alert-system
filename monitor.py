import boto3

cloudwatch = boto3.client("cloudwatch")

response = cloudwatch.list_metrics()

print("AWS Cloud Monitoring Report")
print("----------------------------")


for metric in response["Metrics"]:
    print(f"Namespace: {metric['Namespace']}")
    print(f"Metric: {metric['MetricName']}")
    print()
    print(f"Total metrics found: {len(response['Metrics'])}")

if len(response["Metrics"]) > 5:
    print("ALERT: High number of metrics detected!")
else:
    print("Status: Monitoring is normal.")
    print("\nEC2 CPU Monitoring")
print("------------------")

ec2 = boto3.client("ec2")

instances = ec2.describe_instances()

for reservation in instances["Reservations"]:
    for instance in reservation["Instances"]:
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"State: {instance['State']['Name']}")
        if instance["State"]["Name"] == "running":
            print("OK: EC2 instance is running.")
        else:
            print("ALERT: EC2 instance is not running!")