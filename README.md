# room_reservation

room_reservation/
    ├── app/
    |   ├── api/
    |   |   └── __init__.py
    |   ├── core/
    |   |   ├── __init__.py
    |   |   └── config.py
    |   ├── schemas/
    |   |   └── __init__.py
    |   ├── __init__.py
    |   └── main.py
    ├── venv/
    └── .env

установка
```bash
pip install fastapi==0.78.0 "uvicorn[standard]==0.17.6" 
```

uvicorn app.main:app --reload

fastapi
uvicorn[standard]
aiosqlite
pydantic
pydantic-settings
