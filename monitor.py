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