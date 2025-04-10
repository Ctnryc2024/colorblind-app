import streamlit as st
import cv2
import numpy as np
from recolor import recolor_image

st.set_page_config(page_title="Color Blindness Image Converter", layout="centered")

st.title("🎨 Image Converter for Color Blindness")
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)  # Use cv2.IMREAD_COLOR for clarity

    if image is not None:
        st.image(image, caption="Original Image", use_column_width=True)

        if st.button("Convert for Color Blindness"):
            recolored = recolor_image(image)

            # Check if recolored image is valid
            if recolored is not None:
                st.image(recolored, caption="Recolored for Protanopia", use_column_width=True)
            else:
                st.error("Error: The recoloring process failed.")
    else:
        st.error("Error: The uploaded file is not a valid image.")