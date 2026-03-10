from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models.birdspotting import Birdspotting, BirdspottingCreate
from repositories.birdspotting import BirdspottingRepository

router = APIRouter(prefix="/birdspotting", tags=["Birdspotting"])

def get_repo(session: Annotated[Session, Depends(get_session)]) -> BirdspottingRepository:
    return BirdspottingRepository(session)

@router.get("/", response_model=List[Birdspotting])
async def get_all_observations(repo: Annotated[BirdspottingRepository, Depends(get_repo)]):
    return repo.get_all()

@router.get("/{id}", response_model=Birdspotting)
async def get_observation(id: int, repo: Annotated[BirdspottingRepository, Depends(get_repo)]):
    item = repo.get_one(id)
    if not item:
        raise HTTPException(status_code=404, detail="Observation not found")
    return item

@router.post("/", response_model=Birdspotting)
async def add_observation(payload: BirdspottingCreate, repo: Annotated[BirdspottingRepository, Depends(get_repo)]):
    return repo.insert(payload)