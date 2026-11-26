import streamlit as st
import pandas as pd
import re
st.title('B.C.M. College Kottayam (Autonomous)')
uploaded_file=st.file_uploader('Upload the file of repeated scoresin csv format',type=['csv'])
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.success('File Uploded successfully')
    df=pd.DataFrame(df)
    df['adm_no']=df['Email address'].str.extract(r'(SF\d{4}|\d{5})@',flags=re.IGNORECASE)
    df['adm_no']=df['adm_no'].str.upper()
    st.write(df[['adm_no','First name']].value_counts())
    num_cases=st.number_input("Enter the number of tests to be considred",min_value=1,max_value=30,
    value=10,step=1)
    def calculate_average(group):
        best_marks=group.nlargest(num_cases,'Grade/12.00')
        avera=best_marks.sum()/num_cases
    result=df.groupby('adm_no').apply(calculate_average).reset_index(name='Average Mark')
    student_details = df[['adm_no', 'First name']].drop_duplicates('adm_no')
    result = result.merge(student_details, on='adm_no')
    st.write(result[['adm_no', 'First name', 'Average Score']])
    
