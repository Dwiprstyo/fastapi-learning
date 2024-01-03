from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.credential import Credential

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/credential")
def get_all_cred(db: Session = Depends(get_db)):
    print("mask")
    return db.query(Credential).all()