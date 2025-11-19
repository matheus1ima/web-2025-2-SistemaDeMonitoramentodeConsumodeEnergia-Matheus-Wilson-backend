from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class Consumo(Base):
    __tablename__ = "consumo"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, nullable=False)
    kwh = Column(Float, nullable=False)
    custo = Column(Float, nullable=False)
    observacao = Column(String, nullable=True)
