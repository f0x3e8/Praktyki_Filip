import sqlite3
from contextlib import closing
from pathlib import Path

import secrets
import bcrypt
from fastapi import Cookie, Depends, FastAPI, HTTPException, Response, Body
from fastapi.responses import FileResponse


BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "todo.db"
SESSION_COOKIE = "session_id"

app = FastAPI(title="Todo API")


def connect():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def execute(sql, params=()):
    with closing(connect()) as connection:
        rows = connection.execute(sql, params).fetchall()
        connection.commit()
        return rows


def create_session(user_id, response):
    token = new_session_token()
    execute("INSERT INTO sessions(token, user_id) VALUES(?, ?)",(token, user_id))
    response.set_cookie(SESSION_COOKIE,token,httponly=True,samesite="lax")


execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER NOT NULL PRIMARY KEY,
        login VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    )
    """
)

execute(
    """
    CREATE TABLE IF NOT EXISTS sessions (
        token TEXT NOT NULL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """
)

execute(
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        title VARCHAR(255) NOT NULL,
        done INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """
)


def as_task(row):
    return {"id": row["id"], "title": row["title"], "done": bool(row["done"])}


def as_user(row):
    return {"id": row["id"], "login": row["login"]}


def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password(password, password_hash):
    return bcrypt.checkpw(password.encode(), password_hash.encode())


def new_session_token():
    return secrets.token_hex(32)


def current_session(session_id: str | None = Cookie(default=None)):
    """
    Dependency: resolve the session_id cookie to a session row joined with its user.

    Cookie: session_id
    Returns: row with at least session id, user id and login.
    Raises: HTTPException 401 {"detail": "Not logged in"}  # missing or unknown session_id
    """
    if session_id is None:
        raise HTTPException(status_code=401, detail="Not logged in")

    rows = execute("""SELECT sessions.token, sessions.user_id, users.login FROM sessions JOIN users ON sessions.user_id = users.id WHERE sessions.token = ? """,(session_id,))

    if not rows:
        raise HTTPException(status_code=401, detail="Not logged in")

    return rows[0]

@app.get("/")
def index():
    return FileResponse(BASE_DIR / "index.html")

@app.get("/tasks")
def list_tasks(session=Depends(current_session)):
    user_id = session["user_id"]

    rows = execute("""SELECT * FROM tasks WHERE user_id = ? ORDER BY tasks.done ASC, tasks.id DESC""",(user_id,))

    return [as_task(row) for row in rows]


@app.post("/tasks", status_code=201)
def create_task(session=Depends(current_session),title: str = Body(..., embed=True)):
    user_id = session["user_id"]

    title = title.strip()

    if len(title) == 0 or len(title) > 200:
        raise HTTPException(status_code=422,detail="Invalid or blank title")

    execute("INSERT INTO tasks(title, done, user_id) VALUES(?, ?, ?)",(title, 0, user_id))


@app.patch("/tasks/{task_id}")
def update_task(task_id: int,session=Depends(current_session),done: bool = Body(..., embed=True)):

    user_id = session["user_id"]

    row = execute("SELECT * FROM tasks WHERE id = ? AND user_id = ?",(task_id, user_id))

    if not row:
        raise HTTPException(status_code=404,detail="Task not found")

    execute("UPDATE tasks SET done = ? WHERE id = ? AND user_id = ?",(int(done), task_id, user_id))


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int,session=Depends(current_session)):

    user_id = session["user_id"]

    row = execute("SELECT * FROM tasks WHERE id = ? AND user_id = ?",(task_id, user_id))

    if not row:
        raise HTTPException(status_code=404,detail="Task not found")

    execute("DELETE FROM tasks WHERE id = ? AND user_id = ?",(task_id, user_id))


@app.post("/register", status_code=201)
def register(response: Response, login: str = Body(...), password: str = Body(...)):

    login = login.strip()

    if len(login) > 0 and len(login) <= 50 and len(password) >= 8:
        hashed = hash_password(password)

        try:
            execute("INSERT INTO users(login, password) VALUES(?, ?)",(login, hashed))
        except sqlite3.IntegrityError:
            raise HTTPException(status_code=409,detail="Login already taken")

        rows = execute("SELECT * FROM users WHERE login = ?",(login,))

        user = rows[0]
        create_session(user[0], response)
        return as_user(user)

    else:
        raise HTTPException(status_code=422,detail="Invalid login or password")


@app.post("/login")
def login(response: Response,login: str = Body(...),password: str = Body(...)):
    rows = execute("SELECT * FROM users WHERE login = ?",(login,))

    if not rows:
        raise HTTPException(status_code=401, detail="Invalid login or password")
    user = rows[0]

    if not check_password(password, user[2]):
        raise HTTPException(status_code=401, detail="Invalid login or password")

    create_session(user[0], response)

    return as_user(user)


@app.get("/me")
def me(session=Depends(current_session)):
    return as_user(session)

@app.post("/logout", status_code=204)
def logout(response: Response, session=Depends(current_session)):
    session_id = session["token"]
    execute("DELETE FROM sessions WHERE token = ?",(session_id,))

    response.delete_cookie(SESSION_COOKIE)