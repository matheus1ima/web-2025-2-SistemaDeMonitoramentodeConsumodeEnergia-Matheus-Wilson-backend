from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal
from auth_utils import get_current_user
from auth_utils import get_bearer_token

router = APIRouter(prefix="/consumo", tags=["Consumo"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Consumo])
def listar_consumos(db: Session = Depends(get_db), authorization: str | None = Header(default=None)):
    token = get_bearer_token(authorization)
    user = get_current_user(token, db)
    return db.query(models.Consumo).filter(models.Consumo.user_id == user.id).all()

@router.get("/{consumo_id}", response_model=schemas.Consumo)
def obter_consumo(consumo_id: int, db: Session = Depends(get_db), authorization: str | None = Header(default=None)):
    token = get_bearer_token(authorization)
    user = get_current_user(token, db)

    item = db.query(models.Consumo).filter(
        models.Consumo.id == consumo_id,
        models.Consumo.user_id == user.id
    ).first()

    if not item:
        raise HTTPException(404, "Registro não encontrado")

    return item

@router.post("/", response_model=schemas.Consumo)
def criar_consumo(consumo: schemas.ConsumoCreate, db: Session = Depends(get_db), authorization: str | None = Header(default=None)):
    token = get_bearer_token(authorization)
    user = get_current_user(token, db)

    novo = models.Consumo(
        data=consumo.data,
        kwh=consumo.kwh,
        custo=consumo.custo,
        observacao=consumo.observacao,
        user_id=user.id
    )

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.put("/{id}", response_model=schemas.Consumo)
def atualizar_consumo(id: int, consumo: schemas.ConsumoCreate,
                      db: Session = Depends(get_db),
                      authorization: str | None = Header(default=None)):

    token = get_bearer_token(authorization)
    user = get_current_user(token, db)

    item = db.query(models.Consumo).filter(
        models.Consumo.id == id,
        models.Consumo.user_id == user.id
    ).first()

    if not item:
        raise HTTPException(404, "Registro não encontrado")

    item.data = consumo.data
    item.kwh = consumo.kwh
    item.custo = consumo.custo
    item.observacao = consumo.observacao

    db.commit()
    db.refresh(item)
    return item

@router.delete("/{consumo_id}")
def deletar_consumo(consumo_id: int, db: Session = Depends(get_db), authorization: str | None = Header(default=None)):
    token = get_bearer_token(authorization)
    user = get_current_user(token, db)

    consumo = db.query(models.Consumo).filter(
        models.Consumo.id == consumo_id,
        models.Consumo.user_id == user.id
    ).first()

    if not consumo:
        raise HTTPException(404, "Registro não encontrado")

    db.delete(consumo)
    db.commit()

    return {"ok": True}
