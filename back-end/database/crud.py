from fastapi import  HTTPException
from sqlalchemy.orm import Session
from database.schemas import Link
from models import LinkCreate

def get_all_links(db : Session):
    return db.query(Link).all()

def create_db_link(link: LinkCreate, db : Session)-> Link:
    db_link = db.query(Link).filter(Link.display_name == link.display_name).first()
    if db_link: 
        raise HTTPException(status_code = 400, detail = "Link with that name already exists!")
    new_link = Link(display_name = link.display_name, url = link.url)
    db.add(new_link)
    db.commit()
    db.refresh(new_link)
    return new_link
    
def delete_db_link(id: int, db : Session) -> str:
    db_link = db.query(Link).filter(Link.id == id).first()
    if db_link is None:
        raise HTTPException(status_code=400, detail="Link with that id does not exist!")
    db.delete(db_link)
    db.commit()
    return f'Link with id {id} was deleted!'


