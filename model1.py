import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import pickle



def load_crop_model(crop_rec_path):
    model_crop_rec = pickle.load(open(crop_rec_path, 'rb'))
    return model_crop_rec

def predict_crop(data, model):
    data = pd.DataFrame(data, columns=['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall'])
    prediction = model.predict(data)
    return prediction