from app import create_app

def test_users_route():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/users/")  # <-- ruta correcta según tu blueprint

    assert response.status_code == 200
    # assert b"Hello" in response.data
    assert response.get_json() == []  # coincide con la respuesta actual
