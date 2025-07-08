from fastapi import APIRouter, HTTPException
from models import IrisInput, add_iris_data, Iris, IrisWithTarget
from classification_model_trainer import train_model
import numpy as np
import pandas as pd
import pickle
import os
from sklearn.datasets import load_iris

router = APIRouter()

@router.post("/predict")
def predict(data: IrisInput):
    if not os.path.exists("rf_model.pkl"):
        raise HTTPException(status_code=500, detail="Model dosyası yok.")

    with open("rf_model.pkl", "rb") as f:
        model = pickle.load(f)

    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(features)

    iris = load_iris()
    class_name = iris.target_names[prediction[0]]

    return {"tahmin": class_name}

@router.post("/add_data")
def add_data(data: IrisWithTarget):
    from models import IrisInput
    iris_input = IrisInput(
        sepal_length=data.sepal_length,
        sepal_width=data.sepal_width,
        petal_length=data.petal_length,
        petal_width=data.petal_width
    )

    add_iris_data(iris_input, data.target)
    train_model()
    return {"mesaj": "Yeni veri eklendi ve model güncellendi."}
