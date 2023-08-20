import boto3
import requests
import json

def lambda_handler(event, context):
    instance_id = event['detail']['instance-id']
    event_type = event['detail-type']
    timestamp = event['time']
    
    jira_payload = {
        "fields": {
            "project": {"key": "YOUR_PROJECT_KEY"},
            "summary": f"EC2 Event: {event_type}",
            "description": f"Instance ID: {instance_id}\nEvent Type: {event_type}\nTimestamp: {timestamp}",
            "issuetype": {"name": "Task"}
        }
    }
    
    jira_url = "https://your-jira-instance.atlassian.net/rest/api/2/issue/"
    headers = {"Authorization": "Basic YOUR_BASE64_ENCODED_CREDENTIALS", "Content-Type": "application/json"}
    response = requests.post(jira_url, data=json.dumps(jira_payload), headers=headers)
    
    if response.status_code == 201:
        return "JIRA issue created successfully"
    else:
        return f"Failed to create JIRA issue: {response.text}"
