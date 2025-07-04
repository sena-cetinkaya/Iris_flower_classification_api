import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from models import get_all_iris_data

def train_model():
    iris_data = get_all_iris_data()
    df = pd.DataFrame([row.model_dump() for row in iris_data])

    if df.empty:
        print("Veritabanında veri yok, model eğitilemedi.")
        return

    X = df.drop(columns=["id", "target"])
    y = df["target"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    with open("rf_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model başarıyla eğitildi ve rf_model.pkl dosyasına kaydedildi.")

if __name__ == "__main__":
    train_model()

