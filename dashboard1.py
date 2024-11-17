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
state= st.sidebar.multiselect("Pick the State",df2["State"].unique())
if not state:
    df3=df2.copy()

else :
    df3= df2[df2["State"].isin(state)]


# create the city
city= st.sidebar.multiselect("Pick the city",df3["City"].unique())

# Filter the data based on Region, State and City
# here we apply permutation and combination of the filters

if not region and not state and not city:
    filtered_df=df
elif not state and not city:
    filtered_df=df[df["Region"].isin(region)]
elif not region and not city:
    filtered_df=df[df["State"].isin(state)]
elif state and city:
    filtered_df=df3[df["State"].isin(state) & df3["City"].isin(city)]
elif region and city:
    filtered_df=df3[df["Region"].isin(region) & df3["City"].isin(city)]
elif region and state:
    filtered_df=df3[df["Region"].isin(region) & df3["State"].isin(state)]

elif city:
    filtered_df=df3[df3["City"].isin(city)]
else :
    filtered_df=df3[df3["Region"].isin(region) & df3["State"].isin(state)& df3["City"].isin(city)]



# column chart for category and region
category_df= filtered_df.groupby(by=["Category"],as_index=False)["Sales"].sum()


with col1:
    st.subheader("Category wise Sales")
    fig=px.bar(category_df,x="Category",y="Sales",text=['${:,.2f}'.format(x) for x in category_df["Sales"]],template="seaborn")
    st.plotly_chart(fig,use_container_width=True,height=200)


with col2:
    st.subheader("Region wise Sales")
    fig=px.pie(filtered_df,values="Sales",names="Region",hole=0.5)
    fig.update_traces(text=filtered_df["Region"],textposition="outside")
    st.plotly_chart(fig,use_container_width=True)

# showing the data and download
cl1,cl2=st.columns((2))
with cl1:
    with st.expander("Category_ViewDate"):
        st.write(category_df.style.background_gradient(cmap="Blues"))
        csv=category_df.to_csv(index=False).encode('utf=8')
        st.download_button("Download Data",data=csv,file_name="Category.csv",mime="text/csv",help='Click here to download the data as a CSV file')


with cl2:
    with st.expander("Region_ViewData"):
        region=filtered_df.groupby(by="Region",as_index=False)["Sales"].sum()
        st.write(region.style.background_gradient(cmap="Oranges"))
        csv=region.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data",data=csv,file_name="Region.csv",mime="text/csv",help='Click here to download the data as a CSV file')



# Visibilizing the data using time series
