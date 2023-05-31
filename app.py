import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


title_pic = Image.open('pics/title.png')
st.image(title_pic)
st.text('2023.5.31 Build1 :sunglasses:')
price = st.slider('价格区间(万)', 0, 300, (140, 160))
st.write('当前价格区间为', price[0], '~', price[1])

