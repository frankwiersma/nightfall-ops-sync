import boto3

aws_access_key_id = "AKIAVVN5YBKUEGFXSGNF"
aws_secret_access_key = "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"

bucket_name = "nightfall-artifacts"
filename = "flag.txt"

client = boto3.client('s3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key)

client.upload_file(filename, bucket_name, filename)
