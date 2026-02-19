from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from datetime import datetime
from app.models import Media, Tweet
from db.engine import get_async_session
from fastapi import UploadFile, File, Form

router = APIRouter(prefix="/api/v1/medias", tags=["medias"])

class MediaCreate(BaseModel):
    url: str
    tweet_id: int

class MediaOut(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    url: str
    tweet_id: int
    created_at: datetime

@router.get("/", response_model=list[MediaOut])
async def get_medias(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Media))
    return result.scalars().all()


@router.post("/", response_model=MediaOut, status_code=status.HTTP_201_CREATED)
async def create_media(
        file: UploadFile = File(...),
        tweet_id: int = Form(...),
        session: AsyncSession = Depends(get_async_session)
):
    tweet = await session.get(Tweet, tweet_id)
    if not tweet:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Tweet not found")

    contents = await file.read()

    media = Media(url=f"/media/{file.filename}", tweet_id=tweet_id)
    session.add(media)
    await session.commit()
    await session.refresh(media)
    return media
