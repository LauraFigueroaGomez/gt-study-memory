import boto3

session = boto3.Session(
    profile_name="gt-study",
    region_name="us-east-2",
)

s3 = session.client("s3")

response = s3.list_objects_v2(
    Bucket="gt-cs-study-memory-2026",
    MaxKeys=1,
)

print(response.get("KeyCount"))

local_path = "data/raw/HTS-Introduction.pdf"
object_key = "raw/cs6601/HTS-Introduction.pdf"

s3.upload_file(
    Filename=local_path,
    Bucket="gt-cs-study-memory-2026",
    Key=object_key,
)

print(f"Uploaded: {object_key}")








