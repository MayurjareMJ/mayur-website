# cv_demo.py
import streamlit as st
import cv2
import numpy as np
from PIL import Image

def cv_demo():
    st.title("🎨 Interactive CV Demo: Cartoonify Your Image")
    st.write("Upload an image and see it transformed into a cartoon!")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Original Image", use_column_width=True)

        # Convert to OpenCV
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Cartoonify
        gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
        )
        color = cv2.bilateralFilter(img_cv, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        cartoon_rgb = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)

        st.image(cartoon_rgb, caption="Cartoonified Image", use_column_width=True)

        # Download button
        from io import BytesIO
        buffer = BytesIO()
        Image.fromarray(cartoon_rgb).save(buffer, format="PNG")
        st.download_button("Download Cartoon Image", buffer, file_name="cartoon.png")
