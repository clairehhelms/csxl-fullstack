# from fastapi import FastAPI, Depends
# from database import Base, engine, get_db
# from schemas import Link
# from models import LinkCreate

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
def create_link(display_name: str, url: str) -> Link:
    link = Link()
    link.display_name = display_name
    link.url = url
    links.append(link)
    # return "test"


@app.get("/api/links")
def get_links() -> list[Link]:
    return links
