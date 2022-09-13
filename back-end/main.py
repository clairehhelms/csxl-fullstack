from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, get_db 
from schemas import Link
from models import LinkCreate

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
    db_link = Link(display_name = link.display_name, url = link.url)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link 

# Silly comment

# Silly comment
@app.get("/api/links")
def get_links(db = Depends(get_db)):
    return db.query(Link).all() 

