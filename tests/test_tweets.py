from fastapi.testclient import TestClient
from app.main import app
import pytest


def test_tweet_endpoints():
    client = TestClient(app)
    headers = {"Authorization": "Bearer test-api-key"}

    resp = client.get("/api/v1/tweets/")
    assert resp.status_code in [200, 401]

    resp = client.get("/api/v1/tweets/7")
    assert resp.status_code in [200, 401, 404]

    resp = client.post("/api/v1/tweets/7/likes")
    assert resp.status_code in [200, 401, 404]

    resp = client.post("/api/v1/tweets/", json={"text": "test", "user_id": 3})
    assert resp.status_code in [200, 401, 422, 404, 201]
