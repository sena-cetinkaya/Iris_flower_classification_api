import pandas as pd
from sqlmodel import Field, SQLModel, Session, create_engine, select

# SQLModel sınıfını tanımla
class Iris(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    target: int

# Veritabanı bağlantısı oluştur
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/iris_db"
engine = create_engine(DATABASE_URL, echo=True)

# Veritabanında tabloyu oluştur 
def create_db_and_table():
    SQLModel.metadata.create_all(engine)

# CSV'den veriyi oku, target'ı sayısallaştır, nesnelere dönüştür
def load_data_from_csv(csv_path: str):
    # Veri setini pandas ile oku
    df = pd.read_csv(csv_path)

    # Target’ı sayısallaştır
    target_mapping = {label: idx for idx, label in enumerate(df['target'].unique())}
    df['target'] = df['target'].map(target_mapping)

    # id sütunu varsa sil
    if 'id' in df.columns:
        df.drop(columns=['id'], inplace=True)

    # Iris nesnelerine dönüştür
    iris_records = [
        Iris(
            sepal_length=row.sepal_length,
            sepal_width=row.sepal_width,
            petal_length=row.petal_length,
            petal_width=row.petal_width,
            target=row.target
        )
        for row in df.itertuples(index=False)
    ]
    return iris_records

# Verileri veritabanına ekle
def insert_data(records: list[Iris]):
    with Session(engine) as session:
        session.add_all(records)
        session.commit()

# Ana akış
if __name__ == "__main__":
    create_db_and_table()
    data = load_data_from_csv("IRIS.csv")
    insert_data(data)
    print("Veriler başarıyla veritabanına eklendi.")
