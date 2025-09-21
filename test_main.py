from fastapi.testclient import TestClient
from main import api

client = TestClient(api)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Book Management System"}

def test_add_book():
    book_data = {
        "id": 1,
        "name": "Test Book",
        "description": "A sample book",
        "isAvailable": True
    }
    response = client.post("/book", json=book_data)
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Test Book"

def test_get_books():
    response = client.get("/book")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["id"] == 1

def test_update_book():
    updated_data = {
        "id": 1,
        "name": "Updated Book",
        "description": "Updated description",
        "isAvailable": False
    }
    response = client.put("/book/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Book"

def test_delete_book():
    response = client.delete("/book/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_delete_book_not_found():
    response = client.delete("/book/999")
    assert response.status_code == 200
    assert response.json() == {"error": "Book not found, deletion failed"}
