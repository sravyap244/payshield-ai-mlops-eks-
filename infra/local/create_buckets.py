import os

import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("S3_ENDPOINT_URL"),
    aws_access_key_id=os.getenv("MINIO_ROOT_USER"),
    aws_secret_access_key=os.getenv("MINIO_ROOT_PASSWORD"),
    region_name="us-east-1",
)

BUCKETS = [
    "payshield-ai-raw-data-dev",
    "payshield-ai-processed-data-dev",
    "payshield-ai-features-dev",
    "payshield-ai-model-artifacts-dev",
    "payshield-ai-drift-reports-dev",
]

for name in BUCKETS:
    s3.create_bucket(Bucket=name)
    print("Created:", name)