from fastapi import FastAPI, Depends
from database import Base, engine, get_db
from schemas import Link
from models import LinkCreate

Base.metadata.create_all(bind=engine)
app = FastAPI()

# python -m uvicorn main:app --reload


@app.get("/api/health")
def read_root():
    return "Hello World!"


class Link:
    display_name: str
    url: str


links: list[Link] = []


@app.post("/api/link")
def create_link(link: LinkCreate, db = Depends(get_db)):
    db_link = Link(display_name = link.display_name, url = link.url)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link


@app.get("/api/links")
def get_links(db = Depends(get_db)):
    return db.query(Link).all()
