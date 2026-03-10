from sqlmodel import Session, select
from models.birds import Bird, BirdCreate

class BirdRepository:
    def init(self, session: Session):
        self.session = session

    def get_all(self):
        statement = select(Bird)
        items = self.session.exec(statement).all()
        return items

    def insert(self, payload: BirdCreate):
        # Convert the Create model to the Table model
        item = Bird.model_validate(payload)
        self.session.add(item)
        # If species_id doesn't exist, the line below throws an error
        self.session.commit() 
        self.session.refresh(item)
        return item