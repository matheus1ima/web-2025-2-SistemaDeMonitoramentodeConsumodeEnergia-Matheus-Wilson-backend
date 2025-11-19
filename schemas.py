from pydantic import BaseModel

class ConsumoBase(BaseModel):
    data: str
    kwh: float
    custo: float
    observacao: str | None = None

class ConsumoCreate(ConsumoBase):
    pass

class Consumo(ConsumoBase):
    id: int

    class Config:
        from_attributes = True