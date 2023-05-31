import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


title_pic = Image.open('pics/title.png')
st.image(title_pic)
st.text('2023.5.31 Build1')
price = st.slider('价格区间(万)', 0, 1000, 160)
st.write('当前价格区间为', price)