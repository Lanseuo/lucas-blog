import pytest

from blog import app


@pytest.fixture(scope="module")
def test_client():
    testing_client = app.test_client()

    # Establishing an application context
    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


def test_index(test_client):
    response = test_client.get("/")
    assert response.status_code == 200


def test_post(test_client):
    response = test_client.get("/hallo-welt")
    assert response.status_code == 200


def test_api_posts(test_client):
    response = test_client.get("/api/posts")
    assert response.status_code == 200

    for post in response.json:
        assert "content" in post.keys()
        assert "date" in post.keys()
        assert "description" in post.keys()
        assert "image" in post.keys()
        assert "permalink" in post.keys()
        assert "title" in post.keys()


def test_api_post(test_client):
    response = test_client.get("/api/posts/hallo-welt")
    assert response.status_code == 200

    post = response.json
    assert "content" in post.keys()
    assert "date" in post.keys()
    assert "description" in post.keys()
    assert "image" in post.keys()
    assert "permalink" in post.keys()
    assert "title" in post.keys()


def test_feed(test_client):
    response = test_client.get("/feed")
    assert response.status_code == 200

    assert b"</feed>" in response.data
