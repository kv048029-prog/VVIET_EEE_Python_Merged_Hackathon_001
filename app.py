import os

folders = [
    "uploads",
    "outputs",
    "temp",
    "assets"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True) 
  
import streamlit as st

from watermark.image_watermark import image_page
from watermark.video_watermark import video_page
from watermark.pdf_watermark import pdf_page
from watermark.word_watermark import word_page

st.set_page_config(
    page_title="AI Watermark Studio",
    page_icon="💧",
    layout="wide"
)

st.title("💧 AI Watermark Studio")

st.markdown("""
### Add Text & Logo Watermarks to

- 🖼 Images
- 🎥 Videos
- 📄 PDF Files
- 📝 Word Documents
""")

option = st.sidebar.selectbox(
    "Choose File Type",
    [
        "Image",
        "Video",
        "PDF",
        "Word"
    ]
)

if option == "Image":
    image_page()

elif option == "Video":
    video_page()

elif option == "PDF":
    pdf_page()

else:
    word_page()
