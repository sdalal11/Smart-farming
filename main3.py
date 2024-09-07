import os
from model3 import *
from PIL import Image
import streamlit as st
import subprocess

model_disease_path = "/Users/sanjana/Desktop/AMNEX/crop yield/crop_model.h5"
model_disease = load_disease_model(model_disease_path)


def load_image(file):
    image = Image.open(file)
    image.save('image.jpeg')
    return image
 
def main():
    

    if st.button("Go back to Home Page"):
            subprocess.run(["streamlit", "run", "app.py"])

    custom_style = (
    "<style>"
    "h1 {"
    "    font-size: 38px;"
    "    font-family: 'Times New Roman', Times, serif;"
    "}"
    "</style>"
)

    # Render the custom style
    st.markdown(custom_style, unsafe_allow_html=True)

    # Display the title
    st.title("Plant Disease Detection App")

    # Upload image through Streamlit
    file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    # Check if an image is uploaded
    if file is None:
        st.text("Please upload an image file")
    else:
        
        uploaded_img = load_image(file)

        # Make predictions
        predicted_class = predict_image(model_disease, "image.jpeg", class_labels)
        

        st.image(uploaded_img, use_column_width=True, width = 50, caption= predicted_class)
    
        
        

        os.remove('image.jpeg')
        
    
    

if __name__ == "__main__":
    main()