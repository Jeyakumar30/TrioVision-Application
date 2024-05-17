from table import main
import streamlit as st
import numpy as np
from PIL import Image
from streamlit_paste_button import paste_image_button as pbutton


# Use PIL for reading image from the user as an object instead of cv2 -> reads img using path as an array
def detect(image_file = None, paste_btn = None):
    try:
        if (image_file is not None) and (st.button("Start", key = "1")):
            image = np.array(Image.open(image_file))
            
        elif (paste_btn.image_data is not None) and (st.button("Start", key = 2)):
            image = np.array(paste_btn.image_data)
        
        with st.spinner(text='In progress'):
            output = main(image) # Header, Result, BBox, RoI, df
            st.image(output[2],"Bounding Box Information")
            st.image(output[3],"Region of Interest")
                       
            if output[4] is not None:
                st.markdown("## Tabular Form")
                if output[0] is not None:
                    st.write(output[0])
                st.dataframe(output[4])
            else:
                st.markdown("### No Detections")
        with st.expander("**Eager to know how it works??**", ):
            st.info("""
                    **1. Tabular Region Detection:** It first detects tabular regions within given input images by performing a sequence of OpenCV operations. 
                    
                    **2. Text Extraction:** Building upon the detection of tabular regions, this app evaluate ***EasyOCR's*** efficacy in accurately extracting text data located within these identified tabular regions.
                    
                    **3. Tabular Conversion:** In addition to text extraction, this application converts the extracted text data back into a tabular format accurately. 
                    """)

    except UnboundLocalError or AttributeError:
        st.write("Stay cool! Start Processing.")

    except TypeError:
        st.error("Table Data Not Present in the given image")

def ocr_main():
    try:
        st.markdown("<h2 style='text-align: center;'>Extracting Table Content from an Image</h2>", unsafe_allow_html=True)
        st.info('Avoid loading images that are Blured, Containing Watermarks/background information or tables with too many Missing Values, as it may results with No Detections/Misplacement of data items.', icon="ℹ️")

        st.subheader("Upload Your Image")
        
        with st.sidebar:
            st.subheader("Copy & Paste an Image")
    
            paste_btn = pbutton(
            label="📋 Paste an image",
            text_color="#ffffff",
            background_color="#FF0000",
            hover_background_color="#380909",
            key="paste"
        )

        img_file = st.file_uploader("", type=["png","jpg","jpeg"])
        
        sidebar_action = 0
    
        if paste_btn.image_data is None:
            sidebar_action = 1
               
        if (sidebar_action == 0):
            st.image(paste_btn.image_data, caption="Input Image")
            detect(paste_btn=paste_btn)
        elif (sidebar_action == 1):
            st.image(img_file, caption="Input Image")
            detect(image_file=img_file)

        if paste_btn.image_data is not None:
            st.warning("Suggested to Clear Selection Before Loading New Image", icon='🚨')
            st.write(f'Want to Clear Selection? <a href="{st.session_state.get("url", "")}" target="_self">Click Here</a>', unsafe_allow_html=True)
                    
    except AttributeError:
        st.write("Make sure that you have uploaded an Image 🙄")

# ocr_main()