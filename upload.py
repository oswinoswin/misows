import boto3
import time
import sys

data = open('/home/oswin/Documents/misows/04_-_Flaming.mp3', 'rb')
file_size = sys.getsizeof('/home/oswin/Documents/misows/04_-_Flaming.mp3')
bucket_name = 'misows5'
file_key = 'flaming'

print("Uploading: {} size: {}".format("04_-_Flaming.mp3", file_size))
s3 = boto3.client('s3')

start_time = time.perf_counter()

s3.put_object(Bucket=bucket_name, Key=file_key, Body=data)
upload_time = time.perf_counter()
elapsed_time = upload_time - start_time

print("Upload time: {}".format(elapsed_time))
bucket_listing = s3.list_objects(Bucket=bucket_name)
print("Bucket listing:\n")
print(bucket_listing)


