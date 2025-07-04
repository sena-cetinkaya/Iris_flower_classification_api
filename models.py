from typing import Optional, List
from sqlmodel import Field, SQLModel, Session, create_engine, select
from pydantic import BaseModel

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/iris_db"
engine = create_engine(DATABASE_URL, echo=False)

class Iris(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    target: int

class IrisInput(SQLModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisWithTarget(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    target: int

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def add_iris_data(data: IrisInput, target: int):
    with Session(engine) as session:
        new_row = Iris(**data.dict(), target=target)
        session.add(new_row)
        session.commit()

def get_all_iris_data() -> List[Iris]:
    with Session(engine) as session:
        return session.exec(select(Iris)).all()

