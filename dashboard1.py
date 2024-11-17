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
    filename = f1.name
    st.write(filename)
    df = pd.read_excel(filename)
else:
    os.chdir(r"C:\Users\PUJA KUMARI\Desktop\dashboard")
    df = pd.read_excel("Superstore.xlsx")


#create a date picker ,user can choose specific period of the data
col1, col2 = st.columns((2)) # create two columns
df["Order Date"] = pd.to_datetime(df["Order Date"])



# Getting the min and max date
startDate = pd.to_datetime(df["Order Date"]).min()
endDate = pd.to_datetime(df["Order Date"]).max()

# taking the input  of the date
with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))


# based on data our dataframe data will be updated
df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()

st.sidebar.header("Choose your filter: ")
# Create for Region
region = st.sidebar.multiselect("Pick your Region", df["Region"].unique())

#if we are not selecting any region(E,W,N,S)
if not region:
    df2=df.copy() #df store in df2
else :
    df2=df[df["Region"].isin(region)]

# Create for state if we select any bthen we get only that part of states

