import boto3
import json
from botocore.exceptions import NoCredentialsError, ClientError

try:
    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    print("Endpoint connected")

    response = client.invoke_model(
        modelId="anthropic.claude-v2",
        accept="application/json",
        contentType="application/json",
        body=json.dumps({
            "prompt": "Explain quantum computing in simple terms.",
            "max_tokens_to_sample": 200
        })
    )

    output = json.loads(response["body"].read())
    print(output)

except NoCredentialsError:
    print("❌ No AWS credentials found. Run `aws configure` or set environment variables.")
except ClientError as e:
    print(f"❌ AWS ClientError: {e}")
