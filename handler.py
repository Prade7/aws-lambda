import json
import os
import sys
import boto3
import logging




s3=boto3.resource("s3")
bucket=s3.Bucket("pradeep-data-s3")
key="Product/pradeep-data.csv"

def hello(event, context):
    try :
        bucket.upload_file('Book.csv',key)
        return {
            "body":"Success!"
        }
    except NameError:
       logging.info(f"Check the name of the file")
        
    except FileNotFoundError:
        logging.info(f"check the name of the file")
   
