from app import create_app

def test_users_route():
    app = create_app()
    client = app.test_client()

    response = client.get("/users")

    assert response.status_code == 200
    assert b"Hello" in response.data
