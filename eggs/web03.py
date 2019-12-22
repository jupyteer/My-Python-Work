import streamlit as st
import pandas as pd

df =pd.DataFrame({
    "A":[32,99,11],
    "B":[94,87,6666]
}) 

st.write(df)

import matplotlib.pyplot as plot
import numpy as np 
x = np.linspace(-10,10,200)
y = np.sinc(x)
plt.plot(x,y)
plt.show()

st.pyplot()