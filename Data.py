import csv
import pandas as pd

f=pd.read_csv('record.txt')
f.columns = ['Name','Status']
f.to_csv('RECORDCSV.csv')

import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="root",db="#")
cursor = db.cursor()

f=open('RECORDCSV.csv','r')
reader=csv.reader(f)
for row in reader:
    cursor.execute("INSERT INTO RECORD(SNO,USER,STATUS) VALUE(%s,%s,%s)",row)

db.commit()
cursor.close()
print("Written successfully ! ")
