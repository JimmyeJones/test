import streamlit as st
import base64
def img_button(img_path):
    st.image(img_path, use_container_width=True)
    if st.button("Go", key=img_path, use_container_width=True):
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
        





