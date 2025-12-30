# 🚗 OnlineCarShop

**OnlineCarShop** — backend-приложение онлайн-магазина автомобилей, реализованное на **FastAPI**.  
Проект предоставляет REST API для работы с пользователями, автомобилями и заказами.

---

## ✨ Возможности

- 👤 Регистрация и авторизация пользователей  
- 🔐 JWT-аутентификация  
- 🚗 Каталог автомобилей  
- 🛒 Создание заказов  
- 📄 Swagger-документация  

---

## 🧰 Стек технологий

- Python 3.10+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- JWT
- Uvicorn

---

## 🚀 Установка и запуск

```bash
git clone https://github.com/Spirit-ctrl/OnlineCarShop.git
cd OnlineCarShop
python -m venv .venv
```

Активация виртуального окружения:

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

Установка зависимостей:
```bash
pip install -r requirements.txt
```

Запуск сервера:
```bash
uvicorn app.main:app --reload
```

---

## 📄 Документация API

- Swagger UI: http://127.0.0.1:8000/docs

---

## 🔌 Примеры эндпоинтов

### Регистрация пользователя
`POST /user/`

```json
{
  "first_name": "Ivan",
  "last_name": "Ivanov",
  "email": "user@mail.com",
  "password": "password123"
}
```

### Авторизация
`POST /auth/login`

```json
{
  "login": "ivan",
  "password": "password123"
}
```

### Получение автомобилей
`GET /cars/`

---

## 📁 Структура проекта

```
OnlineCarShop/
├── app/
│   ├── main.py
│   ├── methods/
│   ├── models/
│   ├── schemas/
│   └── database/
├── requirements.txt
└── README.md
```

---

## 👤 Автор

Spirit-ctrl  
https://github.com/Spirit-ctrl
