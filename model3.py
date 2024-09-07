import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import pickle
from tensorflow.keras.models import load_model as lm
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt



class_labels = ['Strawberry__healthy', 'Grape_Black_rot', 'Potato_Early_blight', 'Blueberry_healthy', 'Corn(maize)__healthy', 'Tomato_Target_Spot', 'Peach_healthy', 'Potato_Late_blight', 'Tomato_Late_blight', 'Tomato_Tomato_mosaic_virus', 'Pepper,_bell_healthy', 'Orange_Haunglongbing(Citrus_greening)', 'Tomato__Leaf_Mold', 'Grape_Leaf_blight(Isariopsis_Leaf_Spot)', 'Cherry_(including_sour)__Powdery_mildew', 'Apple_Cedar_apple_rust', 'Tomato_Bacterial_spot', 'Grape_healthy', 'Tomato_Early_blight', 'Corn(maize)__Common_rust', 'Grape__Esca(Black_Measles)', 'Raspberry__healthy', 'Tomato_healthy', 'Cherry(including_sour)__healthy', 'Tomato_Tomato_Yellow_Leaf_Curl_Virus', 'Apple_Apple_scab', 'Corn(maize)__Northern_Leaf_Blight', 'Tomato_Spider_mites Two-spotted_spider_mite', 'Peach_Bacterial_spot', 'Pepper,_bell_Bacterial_spot', 'Tomato_Septoria_leaf_spot', 'Squash_Powdery_mildew', 'Corn(maize)__Cercospora_leaf_spot Gray_leaf_spot', 'Apple_Black_rot', 'Apple_healthy', 'Strawberry_Leaf_scorch', 'Potato_healthy', 'Soybean__healthy']

def dice_coef(y_true, y_pred):
    return (2. * K.sum(y_true * y_pred) + 1.) / (K.sum(y_true) + K.sum(y_pred) + 1.)



def load_disease_model(model_disease_path):
    model_disease = lm(model_disease_path, custom_objects = {"dice_coef": dice_coef})
    return model_disease

def dice_coef(y_true, y_pred):
    return (2. * K.sum(y_true * y_pred) + 1.) / (K.sum(y_true) + K.sum(y_pred) + 1.)



def predict_image(model, image_path, class_labels):
    # Load and preprocess the image
    new_img = image.load_img(image_path, target_size=(256, 256))
    img = image.img_to_array(new_img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    # Perform prediction
    prediction = model.predict(img)

    # Get the predicted class
    predicted_class_index = np.argmax(prediction)
    predicted_class = class_labels[predicted_class_index]

    return predicted_class







