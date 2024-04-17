
from tensorflow import keras
from Feature_Extractor import extract_features
import numpy as np



# This function takes the url and returns probability value

def get_prediction(url, model_path):
    print("Loading the model...")
    model = keras.models.load_model(model_path)

    print("Extracting features from url...")
    url_features_list = extract_features(url)
    url_features_array = np.array(url_features_list)
    url_features = url_features_array.astype(np.float32)
    print(url_features)

    print("Making prediction...")
    url_features_reshaped= url_features.reshape(1, -1)
    prediction = model.predict([url_features_reshaped])

    i = prediction[0][0] * 100
    i = round(i,3)
    # print("There is ",i,"% chance,the url is malicious !")
    print(" ")

    return i

