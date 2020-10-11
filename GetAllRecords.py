import sys
import csv
import boto3
import pandas as pd
from io import StringIO

BUCKET_NAME = 'pls-iot'
KEY_NAME = 'Permission.csv'

s3 = boto3.resource('s3')
s3obj = s3.Object(BUCKET_NAME, KEY_NAME).get()

csv_string = s3obj['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv_string), index_col=0)
json = df.to_json(orient='index')

print('')