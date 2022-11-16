import json
import boto3
import pandas as pd
s3Client=boto3.client('s3')
s3=boto3.resource("s3")
import io
import csv
import logging

def lambda_handler(event, context):
    try:
        response=s3Client.get_object(Bucket="pradeep-data-s3",Key="Product/pradeep-data.csv")
        
        data=response["Body"].read().decode('utf-8')
    
        reader=pd.read_csv(io.StringIO(data))
        
    
        
        reader.sort_values(reader.columns[3],ascending=False,axis=0,inplace=True)
    
        print(reader)
        
        productID=reader["productID"].tolist()
        product=reader["Product"].tolist()
        price=reader["Price"].tolist()
        count=reader["Count"].tolist()
        
        total_len=len(reader["productID"])
        data_list=[]
        
        
        for i in range(total_len):
            data_dict={}
            data_dict["productID"]=productID[i]
            data_dict["product"]=product[i]
            data_dict["price"]=price[i]
            data_dict["count"]=count[i]
            
            data_list.append(data_dict)
            
        
        
       
        fileName="Processed_data/result.json"
        
        bucket="pradeep-data-s3"
        
        data=data_list
        
        uploadStream=bytes(json.dumps(data).encode("UTF-8"))
        
      
        
        s3.Bucket(bucket).put_object(Key= fileName, Body=uploadStream)
        # # TODO implement
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
    
    
    except Exception as E:
        print(E)
        logging.info("Check the path")
