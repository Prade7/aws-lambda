# aws-lambda

handler.py uploads a file called book.csv in a s3 bucket called "pradeep-data-s3" in the name of pradeep-data.csv 
If the file name is wrong or file is not found it will throw an exception 

s-3-trigger.py will look into s3 and take the csv named pradeep-data.csv and will sort the csv based on the count and it will convert the data into json
If the file is not there or the file name is wrong it will throw an exception




