import boto3

aws_access_key_id = "REDACTED"
aws_secret_access_key = "REDACTED"

bucket_name = "nightfall-artifacts"
filename = "flag.txt"

client = boto3.client('s3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key)

client.upload_file(filename, bucket_name, filename)
