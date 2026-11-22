import boto3
import json
client= boto3.client("bedrock-runtime", region_name="us-east-1")
print("Endpoint")



response = client.invoke_model(
    modelId="anthropic.claude-v2",
    body=json.dumps({
        "prompt": "Explain quantum computing in simple terms.",
        "max_tokens_to_sample": 200
    })
)
response1 = client.invoke_model(
    modelId="Claude",
    body=json.dumps({
        "prompt": "Explain quantum computing in simple terms.",
        "max_tokens_to_sample": 200
    })
)

client1 = boto3.client("sagemaker-runtime", region_name="us-east-1")
# Invoke your deployed endpoint
response2= client1.invoke_endpoint(
    EndpointName="TestEndPointForDeployment",
    content_type="application/json",
    body=json.dumps({"input" : "Hello SageMaker!"})
)