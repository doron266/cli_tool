import boto3

s3 = boto3.client('s3')

bucket_name = 'dw-test-23'
bucket = s3.create_bucket(Bucket=bucket_name)

print("bucket created")
