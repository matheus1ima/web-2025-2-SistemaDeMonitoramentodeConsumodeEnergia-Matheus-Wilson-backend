from fastapi import FastAPI
from routers import consumo, login
from database import Base, engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)
app.include_router(login.router)
app.include_router(consumo.router)

@app.get("/")
def root():
    return {"message": "API está rodando 🚀"}
