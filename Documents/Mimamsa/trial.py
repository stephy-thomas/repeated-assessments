import streamlite as st
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
    st.write(df['adm_no'].value_counts())
