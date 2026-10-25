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
    local_file = f"data/raw/{name}"
    path_in_bucket = f"source=kaggle_sparkov/ingest_date={today}/{name}"

    print("Sending", name, "... please wait")
    s3.upload_file(local_file, bucket, path_in_bucket)
    print("Done:", path_in_bucket)