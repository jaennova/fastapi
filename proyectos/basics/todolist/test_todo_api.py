"""
Test cases for the ToDo API endpoints.
"""
from fastapi.testclient import TestClient
from datetime import datetime
from todo_api import app

client = TestClient(app)

def test_create_todo():
    """Test creating a new todo item"""
    response = client.post(
        "/todos/",
        json={"title": "Test todo", "description": "Test description"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test todo"
    assert data["description"] == "Test description"
    assert not data["completed"]
    assert "id" in data
    assert "created_at" in data

def test_get_todos():
    """Test getting all todos"""
    response = client.get("/todos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_todo():
    """Test getting a specific todo"""
    # First create a todo
    create_response = client.post(
        "/todos/",
        json={"title": "Get Test", "description": "Test get endpoint"}
    )
    todo_id = create_response.json()["id"]
    
    # Then try to get it
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id

def test_get_nonexistent_todo():
    """Test getting a todo that doesn't exist"""
    response = client.get("/todos/9999")
    assert response.status_code == 404

def test_update_todo():
    """Test updating a todo"""
    # First create a todo
    create_response = client.post(
        "/todos/",
        json={"title": "Update Test", "description": "Test update endpoint"}
    )
    todo_id = create_response.json()["id"]
    
    # Then update it
    response = client.put(
        f"/todos/{todo_id}",
        json={
            "title": "Updated Title",
            "description": "Updated description",
            "completed": True
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["completed"]

def test_delete_todo():
    """Test deleting a todo"""
    # First create a todo
    create_response = client.post(
        "/todos/",
        json={"title": "Delete Test", "description": "Test delete endpoint"}
    )
    todo_id = create_response.json()["id"]
    
    # Then delete it
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200
    
    # Verify it's gone
    get_response = client.get(f"/todos/{todo_id}")
    assert get_response.status_code == 404