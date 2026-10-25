import os
from datetime import date

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

bucket = "payshield-ai-raw-data-dev"
files = ["fraudTrain.csv", "fraudTest.csv"]
today = date.today().isoformat()

for name in files:
    local_size = os.path.getsize(f"data/raw/{name}")
    path_in_bucket = f"source=kaggle_sparkov/ingest_date={today}/{name}"
    bucket_size = s3.head_object(Bucket=bucket, Key=path_in_bucket)["ContentLength"]

    if local_size == bucket_size:
        print("OK     ", name, "-", bucket_size, "bytes, same size in both places")
    else:
        print("PROBLEM", name, "- laptop:", local_size, "bucket:", bucket_size)