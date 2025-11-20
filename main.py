import streamlit as st
import cv2
import pytesseract
import numpy as np
from PIL import Image

# Path for tessaract executable (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ---------------------------
# Preprocessing 
# ---------------------------
def preprocess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

# ---------------------------
# Detect Words
# ---------------------------
def detect_words(img):
    out = img.copy()
    data = pytesseract.image_to_data(out)

    for a, b in enumerate(data.splitlines()):
        if a != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(out, (x, y), (x+w, y+h), (50, 50, 255), 2)
                cv2.putText(out, b[11], (x, y-5), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (50, 50, 255), 2)
    return out


# ---------------------------
# Detect Numbers Only
# ---------------------------
def detect_digits(img):
    out = img.copy()
    hImg, wImg, _ = out.shape

    config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
    boxes = pytesseract.image_to_boxes(out, config=config)

    for b in boxes.splitlines():
        b = b.split()
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

        cv2.rectangle(out, (x, hImg-y), (w, hImg-h), (50, 50, 255), 2)
        cv2.putText(out, b[0], (x, hImg-y+25), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (50, 50, 255), 2)

    return out


# ---------------------------
# STREAMLIT UI
# ---------------------------
st.title("OCR Text & Number Detection App")
st.write("Choose detection mode and upload an image")

# Mode selection
mode = st.radio("Select Detection Mode:", ["Detect Words", "Detect Only Digits"])

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Convert to OpenCV format
    img = np.array(Image.open(uploaded_file))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    st.subheader("Original Image")
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Run selected mode
    if mode == "Detect Words":
        result = detect_words(preprocess(img))
        st.subheader("Detected Words")
    else:
        result = detect_digits(preprocess(img))
        st.subheader("Detected Digits")

    st.image(result, channels="RGB")


