import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder



def load_fertilizer_dataset(data_path):
    df=pd.read_csv(data_path)
    return df

def load_fertilizer_model(model_path):
    fertilizer_model = pickle.load(open(model_path, 'rb'))
    return fertilizer_model

def preprocess_dataset(df):
    columns_dtypes_dict = df.columns.to_series().groupby(df.dtypes).groups
    columns_dtypes_dict = {k.name: list(v) for k, v in columns_dtypes_dict.items()}
    numerical_columns = columns_dtypes_dict["int64"]
    categorical_columns = columns_dtypes_dict["object"]
    categorical_columns.remove("Fertilizer Name")
    LE = LabelEncoder()
    OHE = OneHotEncoder(sparse = False, drop = 'first')
    for col in categorical_columns:
        
        encoded_col = OHE.fit_transform(df[[col]].values.reshape(-1, 1))
        new_col_names = [f"{class_}" for class_ in OHE.get_feature_names_out([col])]
        encoded_data = pd.DataFrame(encoded_col, columns = new_col_names, index = df.index)
        df= pd.concat([df, encoded_data], axis=1)
        df= df.drop(columns = [col]) 

    df["Fertilizer Name"] = df[["Fertilizer Name"]].apply(LE.fit_transform)
    fertilizer_name = df['Fertilizer Name']
    df.pop("Fertilizer Name")
    df["Fertilizer Name"] = fertilizer_name
    return LE, OHE, df



    

# def predict(data, model):
#     data = pd.DataFrame(data, columns=['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall'])
#     prediction = model.predict(data)
#     return prediction

def predict_fertilizer(LE, data, model):
    data = pd.DataFrame(data, columns=['Temparature', 'Humidity ', 'Moisture', 'Nitrogen', 'Potassium',
       'Phosphorous', 'Soil Type_Clayey', 'Soil Type_Loamy', 'Soil Type_Red',
       'Soil Type_Sandy', 'Crop Type_Cotton', 'Crop Type_Ground Nuts',
       'Crop Type_Maize', 'Crop Type_Millets', 'Crop Type_Oil seeds',
       'Crop Type_Paddy', 'Crop Type_Pulses', 'Crop Type_Sugarcane',
       'Crop Type_Tobacco', 'Crop Type_Wheat'])
    prediction = model.predict(data)
    prediction=LE.inverse_transform(prediction)[0]
    return prediction