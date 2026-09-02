import streamlit as st

st.set_page_config(page_title="My Dashboard", layout="wide")
st.title("✨ Hello, World!")
st.metric(label="Visitors", value="1,234", delta="+12%")
st.success("Welcome to your beautiful dashboard!")