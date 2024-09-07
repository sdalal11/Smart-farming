# import streamlit as st


# def app():

#     st.set_page_config(
#         page_title="Agriculutre App"
#     )

#     st.write("# Agriculture App")

#     st.sidebar.success("Select a functionality you want to access")

#     st.markdown(
#         """
#     This app contains 3 different functionalities namely: 
#     1) Crop Recommendation App
#     2) Fertilizer Recommendation App
#     3) Plant Disease Classification

#     One can access any of these functionalities according to their requirements
#     """
#     )


# if __name__ == "__main__":
#     app()


import streamlit as st
import subprocess

def app():
    custom_style = (
    "<style>"
    "h1 {"
    "    font-size: 38px;"
    "    color: purple;"
    "    font-family: 'Times New Roman', Times, serif;"
    "}"
    "</style>"
)

    # Render the custom style
    st.markdown(custom_style, unsafe_allow_html=True)

    # Display the title
    st.title("AGRICULTURE APP")

    st.write("Choose an app to launch:")

    if st.button("Crop Recommendation"):
        subprocess.run(["streamlit", "run", "main1.py"])

    if st.button("Fertilizer Recommendation"):

        subprocess.run(["streamlit", "run", "main2.py"])

    if st.button("Plant Disease Detection"):

        subprocess.run(["streamlit", "run", "main3.py"])

if __name__ == "__main__":
    app()





