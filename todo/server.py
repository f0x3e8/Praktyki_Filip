import sqlite3
from contextlib import closing
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi import Body
from fastapi.responses import FileResponse

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "todo.db"

app = FastAPI(title="Todo API")


def connect():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def execute(sql):
    with closing(connect()) as connection:
        rows = connection.execute(sql).fetchall()
        connection.commit()
        return rows


execute(
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        done INTEGER NOT NULL DEFAULT 0
    )
    """
)


def as_task(row):
    return {"id": row["id"], "title": row["title"], "done": bool(row["done"])}


@app.get("/")
def index():
    return FileResponse(BASE_DIR / "index.html")

@app.get("/tasks")
def list_tasks():
    rows = execute("SELECT * FROM tasks ORDER BY tasks.done ASC, tasks.id DESC")
    return [as_task(row) for row in rows]


@app.post("/tasks", status_code=201)
def create_task(title: str = Body(..., embed=True)):
    title = title.strip()
    if len(title) == 0 or len(title) > 200:
        raise HTTPException(status_code=422, detail="Invalid or blank title")
    execute(f"INSERT INTO tasks (title, done) VALUES ('{title}', 0)")

@app.patch("/tasks/{task_id}")
def update_task(task_id: int, done: bool = Body(..., embed=True)):
    row = execute(f"SELECT * FROM tasks WHERE id = {task_id}")

    if not row:
        raise HTTPException(status_code=404, detail="Task not found")

    row = execute(f"UPDATE tasks SET done = {int(done)} WHERE id = {task_id}")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    row = execute(f"SELECT * FROM tasks WHERE id = {task_id}")

    if not row:
        raise HTTPException(status_code=404, detail="Task not found")

    row = execute(f"DELETE FROM tasks WHERE id = {task_id}")