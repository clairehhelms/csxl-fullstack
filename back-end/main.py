from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from requests import delete
from database.settings import Base, engine, get_db
from models import LinkCreate
from database.crud import get_all_links, create_db_link, delete_db_link

Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/health")
def read_root():
    return "Hello World!"

@app.post("/api/link")
def create_link(link: LinkCreate, db = Depends(get_db)):
    return create_db_link(link, db)

# Silly comment

# Silly comment
@app.get("/api/links")
def get_links(db = Depends(get_db)):
    return get_all_links(db)

@app.delete("/api/link/delete")
def delete_link(id: int, db = Depends(get_db)):
    return delete_db_link(id, db)