import streamlit as st
import pandas as pd

df =pd.DataFrame({
    "A":[32,99,11],
    "B":[94,87,6666]
}) 

st.write(df)

import matplotlib.pyplot as plot
import numpy as np 

st.title('matplotbib 畫圖')
st.markdown(r'畫一個 $\dfrac{\sin(x)/x}$')

x = np.linspace(-10,10,200)
y = np.sinc(x)
plt.plot(x,y)
plt.show()

st.pyplot()

city=st.selectbox('居住地'<["台北市","台中市","高雄市"])
st.write(f"\你選擇了")

coffee=st.slider('咖啡粉量')