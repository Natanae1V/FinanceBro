import streamlit as st
import sys
import os

# Add the ui_pages directory to the path so we can import the page modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'ui_pages'))

# Page configuration
st.set_page_config(
    page_title="Finance Wizard",
    page_icon="💰",
    layout="wide"
)

# Sidebar navigation
st.sidebar.title("Finance Wizard")
st.sidebar.markdown("---")

# Navigation
page = st.sidebar.selectbox(
    "Choose a page:",
    ["Main", "Data Viewer", "Visualizations"],
    index=0
)

# Page routing
if page == "Main":
    import main_page
elif page == "Data Viewer":
    import data_viewer
elif page == "Visualizations":
    import visualization_page
