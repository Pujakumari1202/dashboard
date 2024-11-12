# import some libraries
import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')


# set the title of the page
st.set_page_config(page_title="Superstore!!!!", page_icon=":bar_chart:",layout="wide")


st.title(" :bar_chart: Sample SuperStore EDA")

# add some padding to move this title up
st.markdown('<style>dive.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)


#load the file
f1=st.file_uploader(":file_folder: Upload a file",type=(["csv","txt","xlsx","xls"]))
if f1 is not None:
    filename=f1.name
    st.write(filename)
    df= pd.read_csv(filename,encoding="ISO-8859-1")

else:
    os.chdir(r"C:\Users\PUJA KUMARI\Desktop\dashboard")
    df=pd.read_csv("Superstore.csv",encoding="ISO-8859-1")  

    