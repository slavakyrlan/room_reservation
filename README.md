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
pip install "fastapi-users[sqlalchemy]==10.0.6"
pip install "fastapi-users-db-sqlalchemy<5.0.0"

uvicorn app.main:app --reload

fastapi
uvicorn[standard]
aiosqlite
pydantic
pydantic-settings


{
  "from_reserve": "2025-07-19T15:35",
  "to_reserve": "2025-07-19T15:39"
}

регистрация 
{
  "email": "user@example.com",
  "password": "string",
  "is_active": true, - игнор
  "is_superuser": false, - игнор
  "is_verified": false - игнор
} 
в свагере проходим авторизацию
В поле username введите адрес почты user@example.com, в поле password — пароль string. В выпадающем списке Client credentials location оставьте значение Authorization header, остальные два поля оставьте пустыми; нажмите кнопку Authorize

Получить токен можно и через Postman: на адрес /auth/jwt/login надо отправить POST-запрос с полями формы username и password. При отправке запроса должен быть установлен тип содержимого «данные формы»: Content-Type: application/x-www-form-urlencoded.

миграция добавим: 
batch_op.create_foreign_key('fk_reservation_user_id_user', 'user', ['user_id'], ['id'])
Вместо None в указанных в листинге строчках напишите 'fk_reservation_user_id_user', где имя составлено из следующих частей:
* fk — обозначение внешнего ключа - Foreign Key;
* reservation — таблица, для которой создается внешний ключ;
* user_id — столбец, который содержит внешний ключ;
* user — таблица, на которую ссылается внешний ключ.

в req_dev.txt нет конфликтов библиотек - заменить в будущем requirements.txt