import boto3
from datetime import datetime, timedelta

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
        instance_id = instance["InstanceId"]
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"State: {instance['State']['Name']}")
        if instance["State"]["Name"] == "running":
            print("OK: EC2 instance is running.")
        else:
            print("ALERT: EC2 instance is not running!")
            print("\nEC2 CPU Utilization")
print("--------------------")

cloudwatch = boto3.client("cloudwatch")

end_time = datetime.utcnow()
start_time = end_time - timedelta(minutes=10)

cpu_response = cloudwatch.get_metric_statistics(
    Namespace="AWS/EC2",
    MetricName="CPUUtilization",
    Dimensions=[
    {
        "Name": "InstanceId",
        "Value": instance_id
    }
],
    StartTime=start_time,
    EndTime=end_time,
    Period=300,
    Statistics=["Average"]
)

if cpu_response["Datapoints"]:
    latest = sorted(
        cpu_response["Datapoints"],
        key=lambda x: x["Timestamp"],
        reverse=True
    )[0]

    cpu = latest["Average"]
    print(f"CPU Utilization: {cpu:.2f}%")

    if cpu > 80:
        print("ALERT: CPU utilization is high!")
    else:
        print("OK: CPU utilization is normal.")
else:
    print("No recent CPU data available.")