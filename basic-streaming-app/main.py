import streamlit as st

st.text("Hello World")

###
# 
# Give your app a title

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

# Divider
st.divider()

# st.write
st.write('Thank you for being here')

# ###