from motionApp import motion_main
from objDetApp import obj_main
from easyocrApp import ocr_main
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")


st.markdown("<h1 style='text-align: center;'>TrioVision</h1>", unsafe_allow_html=True)

selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Detect Objects", "Table Text Extractor", "Motion Detector"],  # required
            icons=["house", "search", "table", "emoji-dizzy"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
if selected == "Home":


    st.success("""
    TrioVision is a powerful, all-in-one visual analysis application designed to meet the diverse needs of modern image and motion analysis. It integrates three cutting-edge technologies—Object Detection using YOLO, Motion Detection, and EasyOCR Table Text Extraction—TrioVision provides a robust solution for professionals across various industries.
    """)

    st.subheader("Key Features")

    st.info("""
    1. **Object Detection using YOLO**:
        - Leverage the power of YOLO (You Only Look Once) for real-time object detection.
        - Identify and classify multiple objects within images with high accuracy and speed.
        - Ideal for security surveillance, inventory management, and automated inspection systems.
""")
    st.image("image copy.png", use_column_width=True)

    st.info("""
    2. **EasyOCR Table Text Extraction**:
        - Extract and digitize text from images of tables and documents with exceptional accuracy using EasyOCR.
        - Supports multiple languages and complex table structures, ensuring comprehensive data capture.
        - Perfect for data entry automation, document digitization, and information retrieval.
    """)
    st.image("image copy 2.png", use_column_width= True)

    st.info("""
    3. **Motion Detection**:
        - Advanced motion detection algorithms to track and analyze movement in video streams.
        - Customizable sensitivity settings to minimize false positives and focus on relevant activity.
        - Essential for security monitoring, wildlife observation, and activity recognition.
""")
    st.image("image copy 3.png", use_column_width=True)


    st.subheader("Why Choose TrioVision?")

    st.warning("""
            - **Efficiency**: Streamline your workflow by using a single application for multiple vision-based tasks.
            - **Accuracy**: This application ensures precise detection, tracking, and extraction.
            - **User-Friendly**: Intuitive interface designed for both technical and non-technical users.
    """)


    st.write("""
    Transform your visual data analysis with TrioVision, the ultimate tool for object detection, motion tracking, and text extraction. Experience the future of intelligent vision technology today!
    """)

    # Add some spacing
    st.write("\n\n")

    # st.image("logo.png", use_column_width=True)

    st.markdown("<footer style='text-align: center;'>For more information </footer>", unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;"><a href="mailto:jeyakumar.nkumaran@gmail.com">Contact Me </a></div>', unsafe_allow_html=True)

            
if selected == "Detect Objects":
    obj_main()

if selected == "Motion Detector":
    motion_main()

if selected == "Table Text Extractor":
    ocr_main()

