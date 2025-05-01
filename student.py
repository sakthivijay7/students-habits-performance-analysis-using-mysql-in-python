import mysql.connector
import streamlit as st
import pandas as pd

st.title("Students_performance analysis")

connect=mysql.connector.connect(host="localhost",user="root",password="sakthi7",database="students")
if connect:
    print("connect")
else:
    print("not connected") 
 
cursor=connect.cursor()
query= st.text_area(" Enter Query to Retrive Data")
cursor.execute(query)
data=cursor.fetchall()

if st.button("Data"):
   for  i in data:
     st.write(i)
     break
st.download_button("Download",data="data",file_name="Retrive_data.csv")


