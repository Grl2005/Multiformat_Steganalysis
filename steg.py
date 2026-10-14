import streamlit as st
from encode import *
from detect import *
from PIL import Image
import os

st.title("Multi-format Steganalysis Tool")

mode = st.sidebar.selectbox("Mode", ["Encode", "Detect"])

uploaded_file = st.file_uploader(
    "Upload file",
    type=["png","jpg","jpeg","txt","docx","pdf"]
)


st.markdown("""
<div class="header-box">
    <div class="header-title">
        Multi-format Steganalysis Tool
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- ENCODE ----------------

if mode == "Encode":

    message = st.text_area("Enter secret message")

    if uploaded_file and message:

        filename = uploaded_file.name
        name, ext = os.path.splitext(filename)
        output_name = f"{name}_enc{ext}"

        if st.button("Encode"):

            # IMAGE
            if ext.lower() in [".png",".jpg",".jpeg"]:

                image = Image.open(uploaded_file)
            
                # convert JPG to PNG internally
                encoded = encode_image(image, message)
            
                output_name = f"{name}_enc.png"
            
                encoded.save(output_name)
            
                with open(output_name,"rb") as f:
                    st.download_button("Download", f, output_name)


            # TXT
            elif ext == ".txt":

                encoded = encode_txt(uploaded_file, message)

                st.download_button(
                    "Download",
                    encoded,
                    output_name
                )


            # DOCX
            elif ext == ".docx":

                doc = encode_docx(uploaded_file, message)
                doc.save(output_name)

                with open(output_name,"rb") as f:
                    st.download_button("Download", f, output_name)


            # PDF
            elif ext == ".pdf":

                encode_pdf(uploaded_file, message, output_name)

                with open(output_name,"rb") as f:
                    st.download_button("Download", f, output_name)


# ---------------- DETECT ----------------

if mode == "Detect":

    if uploaded_file:

        ext = uploaded_file.name.split(".")[-1]

        if st.button("Detect"):

            if ext in ["png","jpg","jpeg"]:
                result = detect_image(uploaded_file)

            elif ext == "txt":
                result = detect_txt(uploaded_file)

            elif ext == "docx":
                result = detect_docx(uploaded_file)

            elif ext == "pdf":
                result = detect_pdf(uploaded_file)

            st.success(result)