# AWS Cloud Monitoring & Alert System

## Overview

This project is a Python-based AWS monitoring and alert system built using AWS CloudWatch, Amazon EC2, and the Boto3 SDK.

The system retrieves AWS monitoring data, checks EC2 instance status, evaluates CPU utilization, and generates alerts when configured thresholds are exceeded.

## Features

- Retrieves AWS CloudWatch metrics
- Counts available CloudWatch metrics
- Configurable metric thresholds
- Automatically discovers EC2 instances
- Checks EC2 instance state
- Alerts when an EC2 instance is not running
- Monitors EC2 CPU utilization
- Configurable CPU utilization threshold
- Generates an overall monitoring status
- Uses Python and Boto3 to interact with AWS services

## AWS Services Used

- Amazon CloudWatch
- Amazon EC2
- AWS Identity and Access Management (IAM)

## Technologies

- Python
- Boto3
- AWS CloudWatch
- Amazon EC2
- Git
- GitHub
- Visual Studio Code

## Monitoring Logic

The system uses configurable thresholds:

- Metric threshold: 5
- CPU utilization threshold: 80%

If a monitored condition exceeds a configured threshold or an EC2 instance is not running, the system generates an alert and changes the overall monitoring status to:

`ALERT`

If monitored conditions remain within the configured limits, the system reports:

`OK`

## Example Output

```text
Total metrics found: 300
ALERT: High number of metrics detected!

Instance ID: i-xxxxxxxxxxxxxxxxx
State: stopped
ALERT: EC2 instance is not running!

EC2 CPU Utilization
--------------------
No recent CPU data available.

Overall Monitoring Status
-------------------------
Status: ALERT

## Project Structure

```text
aws-cloud-monitoring-alert-system/
│
├── monitor.py
└── README.md

## How It Works

1. The Python script connects to AWS using Boto3.
2. CloudWatch metrics are retrieved and evaluated.
3. EC2 instances are discovered automatically.

## Security

AWS credentials should never be stored directly in the source code or committed to GitHub.

## Future Improvements

Planned improvements include:

- Email or SMS notifications
- Automated CloudWatch alarms
- Monitoring additional AWS services

## Author

Tekoa Bryant

Cloud & AWS Projects Portfolio