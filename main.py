import streamlit as st
import base64
def img_button(img_path):
    # Your local image path
    
    
    # Convert image to base64
    def image_to_base64(img_path):
        with open(img_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    
    img_base64 = image_to_base64(img_path)
    
    # Display the image as a clickable link (fake button)
    st.markdown(f"""
        <a href="?clicked=true">
            <img src="data:image/png;base64,{img_base64}" width="300" style="cursor:pointer;"/>
        </a>
    """, unsafe_allow_html=True)
    
    # Detect if clicked via URL query param
    clicked = st.query_params.get("clicked") == "true"
    
    if clicked:
        return True



if img_button("FAN.png"):
    st.text("FAN clicked")
if img_button("FAN.png"):
    st.text("FAN clicked")
if img_button("FAN.png"):
    st.text("FAN clicked")
if img_button("FAN.png"):
    st.text("FAN clicked")

