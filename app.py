import streamlit as st
from welcome_page import show_page1
from visualize import show_visualizer
from compare import show_comparison

st.set_page_config(page_title="DSAV", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("DSAV")

page = st.sidebar.selectbox(
    'Select Page',
    (
        'Welcome',
        'Visualize',
        'Compare',
    ),
    index=0
)


if page == 'Welcome':
    show_page1()
elif page == 'Visualize':
    show_visualizer()
elif page =='Compare':
    show_comparison()