import streamlit as st

# Load an image
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/512px-React-icon.svg.png"

# Create a clickable image "button" using markdown
clicked = st.markdown(f"""
    <a href="?run=true">
        <img src="{image_url}" width="100" style="cursor: pointer;" />
    </a>
""", unsafe_allow_html=True)

# Check URL param to see if the image-button was clicked
run = st.query_params.get("run") == "true"

if run:
    st.write("Button was clicked!")
