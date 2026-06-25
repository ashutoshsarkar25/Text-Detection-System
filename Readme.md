# 🔍 OCR Text & Number Detection App

## Overview

The **OCR Text & Number Detection App** is a computer vision-based web application that extracts and visualizes text from images using **Tesseract OCR**, **OpenCV**, and **Streamlit**.

The application allows users to upload an image and choose between two detection modes:

1. **Word Detection** – Detects and highlights all words present in the image.
2. **Digit Detection** – Detects and highlights only numerical characters.

Detected text is displayed directly on the image with bounding boxes, making it easy to visualize the OCR results in real time.

---

## Features

### 📝 Text Detection

* Extracts words from uploaded images.
* Draws bounding boxes around detected words.
* Displays recognized text labels above each word.
* Supports printed text in images.

### 🔢 Digit Detection

* Detects only numerical characters.
* Ignores alphabets and special symbols.
* Uses OCR character whitelisting for accurate digit recognition.
* Highlights each detected number with bounding boxes.

### 🖼️ Image Upload Support

* Upload PNG, JPG, and JPEG files.
* Real-time image processing.
* Instant visualization of OCR results.

### 🌐 Interactive Web Interface

* Built using Streamlit.
* Simple and user-friendly interface.
* No coding knowledge required for usage.
* Runs directly in a browser.

---

## Technologies Used

### Programming Language

* Python

### Libraries and Frameworks

#### Streamlit

* Interactive web application framework
* User interface development

#### OpenCV

* Image processing
* Drawing bounding boxes
* Image format conversion

#### Tesseract OCR

* Optical Character Recognition engine
* Text extraction from images

#### NumPy

* Image array processing

#### Pillow (PIL)

* Image loading and handling

---

## Project Architecture

```text
OCR Text & Number Detection App
│
├── Image Upload Module
│
├── Image Preprocessing
│   └── RGB Conversion
│
├── Detection Modes
│   │
│   ├── Word Detection
│   │   ├── OCR Processing
│   │   ├── Word Extraction
│   │   ├── Bounding Box Creation
│   │   └── Label Rendering
│   │
│   └── Digit Detection
│       ├── OCR Processing
│       ├── Digit Filtering
│       ├── Bounding Box Creation
│       └── Label Rendering
│
└── Streamlit User Interface
```

---

## Working Principle

### Step 1: Upload Image

The user uploads an image through the Streamlit interface.

### Step 2: Image Preprocessing

The image is converted into RGB format using OpenCV to improve OCR compatibility.

### Step 3: Select Detection Mode

Users can choose between:

#### Detect Words

* Extracts complete words from the image.
* Uses `pytesseract.image_to_data()`.
* Retrieves coordinates and text information.
* Draws bounding boxes around each detected word.

#### Detect Only Digits

* Uses OCR configuration with digit whitelisting.
* Restricts detection to numbers only.
* Uses `pytesseract.image_to_boxes()`.
* Draws bounding boxes around detected digits.

### Step 4: Display Results

The processed image is displayed with annotations showing detected text or digits.

---

## OCR Configuration

### Word Detection

```python
data = pytesseract.image_to_data(image)
```

Returns:

* Word content
* Confidence values
* Bounding box coordinates
* Position information

### Digit Detection

```python
config = '--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
```

Parameters:

* OEM 3 → Uses Tesseract's default OCR engine.
* PSM 6 → Assumes a block of text.
* Character Whitelist → Restricts recognition to digits 0–9.

This improves numerical recognition accuracy and eliminates unwanted characters.

---

## User Interface Components

### Application Title

```text
OCR Text & Number Detection App
```

### Detection Mode Selection

```text
Detect Words
Detect Only Digits
```

Implemented using Streamlit Radio Buttons.

### Image Upload

Supported formats:

* PNG
* JPG
* JPEG

### Output Display

Shows:

* Original uploaded image
* Processed image with OCR annotations

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/ocr-text-number-detection.git
cd ocr-text-number-detection
```

### Install Dependencies

```bash
pip install streamlit opencv-python pytesseract pillow numpy
```

### Install Tesseract OCR

Download and install Tesseract OCR:

https://github.com/tesseract-ocr/tesseract

Update the executable path:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## Run Application

```bash
streamlit run app.py
```

The application will launch in your default web browser.

---

## Sample Workflow

```text
Upload Image
      │
      ▼
Choose Detection Mode
      │
      ▼
OCR Processing
      │
      ▼
Text/Digit Recognition
      │
      ▼
Bounding Box Generation
      │
      ▼
Display Results
```

---

## Applications

### Document Digitization

* Convert printed text into machine-readable data.

### Invoice Processing

* Extract invoice numbers and amounts.

### Receipt Analysis

* Detect prices and transaction details.

### Form Processing

* Read numerical entries from forms.

### Educational Tools

* Learn OCR and image processing concepts.

### Data Entry Automation

* Reduce manual data entry efforts.

---

## Learning Outcomes

This project demonstrates:

* Optical Character Recognition (OCR)
* Computer Vision fundamentals
* Image preprocessing techniques
* Text extraction from images
* Streamlit web application development
* OpenCV image annotation
* Integration of Tesseract OCR with Python

---

## Future Enhancements

### 🚀 Advanced OCR Preprocessing

* Grayscale conversion
* Thresholding
* Noise reduction
* Edge enhancement

### 🌍 Multi-Language Support

* English
* Hindi
* Marathi
* Other regional languages

### 📄 PDF OCR Support

* Extract text directly from PDF files.

### 📊 OCR Statistics Dashboard

* Confidence scores
* Character count
* Word count

### ☁️ Cloud Deployment

* Streamlit Cloud
* AWS
* Azure
* Google Cloud

### 🤖 AI-Powered Document Understanding

* Form field extraction
* Invoice intelligence
* Named entity recognition

---

## Conclusion

The OCR Text & Number Detection App is a practical computer vision project that demonstrates the integration of Tesseract OCR, OpenCV, and Streamlit for intelligent text recognition. The system provides real-time detection and visualization of words and numerical data from images, making it useful for document processing, automation, and OCR learning applications.
