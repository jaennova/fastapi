"""
FastAPI ToDo List API implementation
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List, Optional

app = FastAPI(title="ToDo API")

# Pydantic models
class TodoBase(BaseModel):
    """Base model for Todo items"""
    title: str
    description: str

class TodoCreate(TodoBase):
    """Model for creating Todo items"""
    completed: Optional[bool] = None

class Todo(TodoBase):
    """Model for Todo items with all fields"""
    id: int
    completed: bool
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# Storage
todos = []
todo_id_counter = 1

# Helper functions
def find_todo(todo_id: int) -> Optional[dict]:
    """
    Find a todo by ID.
    
    Args:
        todo_id: The ID of the todo to find
        
    Returns:
        The todo if found, None otherwise
    """
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return None

@app.get("/")
async def read_root():
    """
    Root endpoint.
    
    Returns:
        A welcome message
    """
    return {"message": "Welcome to the ToDo API!"}

# Endpoints
@app.post("/todos/", response_model=Todo, status_code=201)
async def create_todo(todo: TodoCreate):
    """
    Create a new todo item.
    
    Args:
        todo: The todo item to create
        
    Returns:
        The created todo item
        
    Raises:
        HTTPException: If there's an error creating the todo
    """
    global todo_id_counter
    new_todo = {
        "id": todo_id_counter,
        "title": todo.title,
        "description": todo.description,
        "completed": False,
        "created_at": datetime.now()
    }
    todos.append(new_todo)
    todo_id_counter += 1
    return new_todo

@app.get("/todos/", response_model=List[Todo])
async def get_todos():
    """
    Get all todo items.
    
    Returns:
        List of all todo items
    """
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    """
    Get a specific todo item by ID.
    
    Args:
        todo_id: The ID of the todo to get
        
    Returns:
        The requested todo item
        
    Raises:
        HTTPException: If the todo is not found
    """
    todo = find_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo_update: TodoCreate):
    """
    Update a todo item.
    
    Args:
        todo_id: The ID of the todo to update
        todo_update: The updated todo data
        
    Returns:
        The updated todo item
        
    Raises:
        HTTPException: If the todo is not found
    """
    # Encontrar el índice del todo en la lista
    todo_idx = -1
    for idx, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todo_idx = idx
            break
    
    # Si no se encuentra, lanzar error
    if todo_idx == -1:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    # Actualizar los campos
    current_todo = todos[todo_idx]
    updated_todo = {
        "id": current_todo["id"],
        "title": todo_update.title,
        "description": todo_update.description,
        "completed": todo_update.completed if todo_update.completed is not None else current_todo["completed"],
        "created_at": current_todo["created_at"]
    }
    
    # Reemplazar el todo antiguo con el actualizado
    todos[todo_idx] = updated_todo
    return updated_todo

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    """
    Delete a todo item.
    
    Args:
        todo_id: The ID of the todo to delete
        
    Returns:
        Success message
        
    Raises:
        HTTPException: If the todo is not found
    """
    todo_idx = -1
    for idx, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todo_idx = idx
            break
    
    # Si no se encuentra, lanzar error
    if todo_idx == -1:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    # Eliminar el todo de la lista
    todos.pop(todo_idx)
    
    # Retornar mensaje de éxito
    return {"message": "Todo deleted successfully"}