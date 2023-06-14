import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import datetime


conn = st.experimental_connection('mysql', type="mysql")
df = conn.query("select * from carrankingsystemdatabase")
d0 = datetime.datetime(2023, 5, 31, 17, 31, 10)
d_now = datetime.datetime.now()
delta = d_now - d0
st.sidebar.title('目录')
tab1, tab2 = st.sidebar.tabs(['测试页面1', '测试页面2'])
with tab1:
    st.write('测试页面1')
    st.write(delta.days)
with tab2:
    st.write('测试页面2')
title_pic = Image.open('pics/title.png')
st.image(title_pic)
st.write('2023.5.31 Build1 :sunglasses:')
price = st.slider('价格区间(万)', 0, 300, (140, 160))
st.write('当前价格区间为', price[0], '~', price[1])
st.write('DATABASE')
st.dataframe(df)
st.write('ERROR')
