import os
from model1 import *
import cv2
from PIL import Image
import streamlit as st
import subprocess



crop_rec_path = "/Users/sanjana/Desktop/AMNEX/crop yield/RandomForest.pkl"
model_crop_rec = load_crop_model(crop_rec_path)
 
def main():

    if st.button("Go back to Home Page"):
        subprocess.run(["streamlit", "run", "app.py"])
   
    # Main Streamlit code
    # st.title("Crop Recommendation App")

    custom_style = (
    "<style>"
    "h1 {"
    "    font-size: 38px;"
    "    color: black;"
    "    font-family: 'Times New Roman', Times, serif;"
    "}"
    "</style>"
)

    # Render the custom style
    st.markdown(custom_style, unsafe_allow_html=True)

    # Display the title
    st.title("Crop Recommendation App")

    # Upload image through Streamlit
    
    min_limit1= 0.0
    max_limit1= 200.0
    number1 = st.number_input('Nitrogen', min_value=min_limit1, max_value=max_limit1)

    
    if not min_limit1 <= number1 <= max_limit1:
        st.warning(f"Please enter a number between {min_limit1} and {max_limit1}.")

    min_limit2= 0.0
    max_limit2= 100.0
    number2 = st.number_input('Phosphorus', min_value=min_limit2, max_value=max_limit2)

    
    if not min_limit2 <= number2 <= max_limit2:
        st.warning(f"Please enter a number between {min_limit2} and {max_limit2}.")

    
    number3 = st.number_input('Potassium', min_value=min_limit2, max_value=max_limit2)

    
    if not min_limit2 <= number3 <= max_limit2:
        st.warning(f"Please enter a number between {min_limit2} and {max_limit2}.")

    min_limit3= 0.0
    max_limit3= 50.0
    number4 = st.number_input('Temperature', min_value=min_limit3, max_value=max_limit3)

    
    if not min_limit3 <= number4 <= max_limit3:
        st.warning(f"Please enter a number between {min_limit3} and {max_limit3}.")

    number5 = st.number_input('Humidity')
    

    min_limit4= 0.0
    max_limit4= 14.0
    number6 = st.number_input('pH', min_value=min_limit4, max_value=max_limit4)

    if not min_limit4 <= number6 <= max_limit4:
        st.warning(f"Please enter a number between {min_limit4} and {max_limit4}.")

    number7 = st.number_input('Rainfall')


    data = np.array([[number1, number2, number3, number4, number5, number6, number7]])

    if st.button("Predict Crop"):
        # Check if any field is empty
        if None in data:
            st.warning("Please fill in all values.")
        else:
            predictions_crop = predict_crop(data, model_crop_rec)
            st.success(predictions_crop)

    
        
if __name__ == "__main__":
    main()