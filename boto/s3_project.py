import boto3

s3_obj = boto3.resource('s3')

def show_buckets(s3_obj):
    for bucket in s3_obj.buckets.all():
        print(bucket.name)

def upload_bucket(file_name, bucket_name, s3_obj, file_path):
    data = open(file_path,'rb')
    s3_obj.Bucket(bucket_name).put_object(Key=file_name,Body=data)
    data.close()
    print("file uploaded successfully")

upload_bucket('awsPolicy.json','python-bucket-8765',s3_obj,'policy_reader/aws_policy.json')