from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal

router = APIRouter(prefix="/consumo", tags=["Consumo"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Consumo])
def listar_consumos(db: Session = Depends(get_db)):
    return db.query(models.Consumo).all()

@router.post("/", response_model=schemas.Consumo)
def criar_consumo(consumo: schemas.ConsumoCreate, db: Session = Depends(get_db)):
    novo = models.Consumo( 
        data=consumo.data,
        kwh=consumo.kwh,
        custo=consumo.custo,
        observacao=consumo.observacao
        )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo
    
@router.put("/{id}")
def atualizar_consumo(id: int, consumo: schemas.ConsumoCreate, db: Session = Depends(get_db)):
    item = db.query(models.Consumo).filter(models.Consumo.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    item.data = consumo.data
    item.kwh = consumo.kwh
    item.custo = consumo.custo
    item.observacao = consumo.observacao
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{consumo_id}")
def deletar_consumo(consumo_id: int, db: Session = Depends(get_db)):
    consumo = db.query(models.Consumo).filter(models.Consumo.id == consumo_id).first()
    if consumo:
        db.delete(consumo)
        db.commit()
        return {"ok": True}
    return {"error": "Registro não encontrado"}
