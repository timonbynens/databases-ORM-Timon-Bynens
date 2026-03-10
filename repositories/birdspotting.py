from sqlmodel import Session, select
from models.birdspotting import Birdspotting, BirdspottingCreate

class BirdspottingRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_all(self):
        return self.session.exec(select(Birdspotting)).all()

    def get_one(self, spotting_id: int):
        return self.session.get(Birdspotting, spotting_id)

    def insert(self, payload: BirdspottingCreate):
        item = Birdspotting.model_validate(payload)
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item