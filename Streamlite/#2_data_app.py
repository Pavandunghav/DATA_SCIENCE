##

import streamlit as st 
import pandas as pd 


##Title of the app 

st.title("Data.app")

##Context of the app 

st.write("We take your csv data and apply all the data analytics operation on it and give you the insights of the data")

##Building the file uploader 

upload=st.file_uploader("Please upload the file",type=['csv'])
if upload:
    data=pd.read_csv(upload)
    
    
    
    if st.checkbox("Show the data"):
        st.write(data)
        
    ##The shape of the data 

    st.write(f"The shape of your data is {data.shape}")
    st.write(pd.DataFrame(data.info()))
    
    
    
    



