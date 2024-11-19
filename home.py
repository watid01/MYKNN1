import streamlit as st
import pandas as pd

st.title("🥨🥨WedSite Developing using Python🥨🥨")
st.header("🥪WedSite Developing using Python🥪")

st.subheader("WAtid MTV")
st.image('./img/download.jfif')

dt = pd.read_scv('./data/iris.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))