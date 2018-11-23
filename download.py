import boto3
import time



bucket_name = 'misows5'
file_key = 'flaming'
print("Downloading: {}".format(file_key))
s3 = boto3.resource('s3')

start_time = time.perf_counter()

response = s3.meta.client.download_file(bucket_name, file_key, "{}_from_s3".format(file_key))


download_time = time.perf_counter()
elapsed_time = download_time - start_time

print("Download time: {}".format(elapsed_time))
print(response)
