import streamlit as st
import base64
def img_button(img_path):
    
    # Load local image and convert to base64
    def image_to_base64(img_path):
        with open(img_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    
    img_base64 = image_to_base64(img_path)
    
    # Use a form to simulate an image button
    st.image(img_path)
    if st.button("Go"):
        return True

col1, col2, col3 = st.columns(3)

with col1:
    if img_button("FAN.png"):
        st.text("FAN clicked")

with col2:
    if img_button("WARS.png"):
        st.text("FAN clicked")

with col3:
    if img_button("CENTURIES.png"):
        st.text("FAN clicked")
        





