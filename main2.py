import os
from model2 import *
from PIL import Image
import streamlit as st
import subprocess


data_path="/Users/sanjana/Desktop/AMNEX/crop yield/Fertilizer Prediction.csv"
df=load_fertilizer_dataset(data_path)

model_fertilizer_path = "/Users/sanjana/Desktop/AMNEX/crop yield/RF.pkl"
fertilizer_model = load_fertilizer_model(model_fertilizer_path)

LE, OHE, df = preprocess_dataset(df)

 
def main():
    
    if st.button("Go back to Home Page"):
            subprocess.run(["streamlit", "run", "app.py"])

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
    st.title("Fertilizer Recommendation App")

    # Upload image through Streamlit
    
    
    number1 = st.number_input('Temparature')
    number2 = st.number_input('Humidity')
    number3 = st.number_input('Moisture')
    number4 = st.number_input('Nitrogen')
    number5 = st.number_input('Potassium')
    number6 = st.number_input('Phosphorous')
   
    

    soil_options = ('Clayey', 'Loamy', 'Red', 'Sandy')

    # Create a selectbox for the user to choose a soil type
    selected_soil = st.selectbox('Soil Type', soil_options)

    # Create a list of binary values (0 or 1) based on the selected option
    binary_values1 = [1 if option == selected_soil else 0 for option in soil_options]


    crop_names=('Cotton', 'Ground Nuts',
       'Maize', 'Millets', 'Oil seeds',
       'Paddy', 'Pulses', 'Sugarcane',
       'Tobacco', 'Wheat')
    

    # Create a selectbox for the user to choose a soil type
    selected_crop = st.selectbox('Crop Type', crop_names)

    # Create a list of binary values (0 or 1) based on the selected option
    binary_values2 = [1 if option == selected_crop else 0 for option in crop_names]

    
    data = np.array([[number1, number2, number3, number4, number5, number6, *binary_values1, *binary_values2 ]])

    if st.button("Predict Fertilizer"):
        # Check if any field is empty
        if None in data:
            st.warning("Please fill in all values.")
        else:
            predictions_fertilizer = predict_fertilizer(LE, data, fertilizer_model)
            st.success(predictions_fertilizer)

   
        
if __name__ == "__main__":
    main()