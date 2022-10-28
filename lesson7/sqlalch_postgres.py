from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base


engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/python_23_2_2", echo=True)

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String)
    price = Column(Integer)


Base.metadata.create_all(engine)
