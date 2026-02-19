# TweeterClone API

FastAPI Twitter-клон. 90% test coverage.

## Запуск
git clone https://github.com/arl-dev-py/TweeterClone.git
cd TweeterClone
docker-compose up -d
pip install -r requirements.txt
uvicorn app.main:app --reload

Docs: http://localhost:8000/docs

## Auth
Bearer test-api-key

## API
POST /api/v1/users/ {"username": "test"} → user_id=3

POST /api/v1/medias/ file=img.jpg tweet_id=3 → media_id=17

POST /api/v1/tweets/ 
{
  "text": "Твит с фото!", 
  "user_id": 3, 
  "media_ids": [17]
} → tweet_id=7

GET /api/v1/tweets/7 → твит + картинки + likes

POST /api/v1/tweets/7/likes → {"likes_count": 2}

Картинка: /media/img.jpg

## Тесты
pytest --cov=app/routers --cov-report=term  # 90%

## Стек
FastAPI + SQLAlchemy async + PostgreSQL + pytest
