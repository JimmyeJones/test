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
    with st.form("image_button_form"):
        # Fake image "button" using HTML and CSS
        st.markdown(f"""
            <button type="submit" style="border:none; background:none; padding:0;">
                <img src="data:image/png;base64,{img_base64}" width="150" style="cursor:pointer;" />
            </button>
        """, unsafe_allow_html=True)
        submitted = st.form_submit_button("hidden_button")  # label won't show
    
    # Do something when image is clicked
    if submitted:
        return True

col1, col2, col3, col4 = st.columns(4)

with col1:
    if img_button("FAN.png"):
        st.text("FAN clicked")

with col2:
    if img_button("FAN.png"):
        st.text("FAN clicked")

with col3:
    if img_button("FAN.png"):
        st.text("FAN clicked")
        
with col4:
    if img_button("FAN.png"):
        st.text("FAN clicked")





