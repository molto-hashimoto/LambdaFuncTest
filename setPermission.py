import sys
import csv
import boto3
import pandas as pd
from io import StringIO

BUCKET_NAME = 'pls-iot'
KEY_NAME = 'Permission.csv'
serialnumber = 'abc-005'

s3 = boto3.resource('s3')
s3obj = s3.Object(BUCKET_NAME, KEY_NAME).get()

csv_string = s3obj['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv_string), index_col=0)

# 変更
df.at[serialnumber, 'EntryPermission'] = 0
# 書き込みバッファ
csv_buffer = StringIO()
df.to_csv(csv_buffer)

s3.Object(BUCKET_NAME, KEY_NAME).put(Body=csv_buffer.getvalue())

s3obj = s3.Object(BUCKET_NAME, KEY_NAME).get()

csv_string = s3obj['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv_string), index_col=0)

print('')