import streamlit as st
import pandas as pd

st.text("Hello World")

###
# 
# App a title

st.title('Cloud Gear')

# 
# Header
st.header('cloud-gear.com')
# Subheader
st.subheader('Welcome...')
# Markdown
st.markdown('Welcome to the **cloud gear** website.')
# Caption
st.caption('cloud-gear.com')
# Code
st.code("""
        import pandas as pd
        
        pd.read_csv(my_csv_file)
        """)

# Preformatted text
st.text('Hello, how are you?')

# LaTex
st.latex("x=y * 2^2")

# st.write
st.write('Thank you for being here')
# Divider
st.divider()

# ###


###
# 
# 
# 

# df = pd.read_csv("data.csv", dtype="int")
df = pd.read_csv("data.csv")

st.dataframe(df)
st.write(df)

st.table(df)

st.metric(label="Temperature", value=900, delta=20, delta_color="inverse")
# 
# 
# ###