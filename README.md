# 🛍️ Shop App 2

> Полнофункциональный REST API для интернет-магазина, построенный на **FastAPI** с поддержкой JWT-аутентификации, административной панели и деплоя через Docker.

---

## 🚀 Технологии

| Категория | Стек |
|---|---|
| **Framework** | FastAPI 0.136 |
| **ORM** | SQLAlchemy 2.0 |
| **База данных** | PostgreSQL 17 |
| **Миграции** | Alembic |
| **Аутентификация** | JWT (python-jose + passlib + bcrypt) |
| **Валидация** | Pydantic v2 |
| **Админ-панель** | SQLAdmin |
| **Веб-сервер** | Uvicorn + Nginx |
| **Контейнеризация** | Docker + Docker Compose |

---

## 📁 Структура проекта

```
shop_app2/
├── shop_app/
│   ├── api/              # Роутеры (users, auth, category, product, review...)
│   ├── admin/            # SQLAdmin настройки
│   ├── models/           # SQLAlchemy модели
│   └── schemas/          # Pydantic схемы
├── migrations/           # Alembic миграции
├── nginx/                # Конфигурация Nginx
├── main.py               # Точка входа приложения
├── Dockerfile
├── docker-compose.yml
├── alembic.ini
└── req.txt
```

---

## ⚙️ API Endpoints

| Модуль | Prefix | Описание |
|---|---|---|
| `auth` | `/auth` | Регистрация, логин, refresh token |
| `users` | `/users` | Управление пользователями |
| `category` | `/category` | Категории товаров |
| `subcategory` | `/subcategory` | Подкатегории |
| `product` | `/product` | Товары |
| `product_image` | `/product-image` | Изображения товаров |
| `review` | `/review` | Отзывы покупателей |

Интерактивная документация доступна по адресу: `http://localhost:8000/docs`

---

## 🐳 Запуск через Docker

### 1. Клонируй репозиторий

```bash
git clone https://github.com/nuray010/shop_app2.git
cd shop_app2
```

### 2. Создай файл `.env`

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
```

### 3. Запусти контейнеры

```bash
docker-compose up --build -d
```

### 4. Примени миграции

```bash
docker-compose exec fastapi alembic upgrade head
```

Приложение будет доступно на `http://localhost:80`

---

## 💻 Локальный запуск (без Docker)

```bash
# Установи зависимости
pip install -r req.txt

# Примени миграции
alembic upgrade head

# Запусти сервер
uvicorn main:shop_app --host 127.0.0.1 --port 8000 --reload
```

---

## 🗄️ Архитектура базы данных

Основные модели:

- **UserProfile** — пользователи с хешированными паролями
- **Category / SubCategory** — иерархия категорий товаров
- **Product** — товары с ценой, описанием, количеством
- **ProductImage** — изображения к товарам
- **Review** — отзывы и рейтинги
- **RefreshToken** — управление сессиями

---

## 🛡️ Аутентификация

Используется схема **JWT Bearer Token**:

1. `POST /auth/register` — регистрация
2. `POST /auth/login` — получение `access_token` и `refresh_token`
3. `POST /auth/refresh` — обновление токена
4. Передавай `Authorization: Bearer <token>` в защищённых запросах

---

## 🖥️ Административная панель

SQLAdmin доступен по адресу: `http://localhost:8000/admin`

---

## 📦 Docker-сервисы

```
fastapi  →  :8000   (FastAPI приложение)
db       →  :5432   (PostgreSQL)
nginx    →  :80     (Реверс-прокси)
```

---

## 📋 Требования

- Python 3.10+
- Docker & Docker Compose
- PostgreSQL 17 (или через Docker)

---

## 👤 Автор

**nuray010** — [github.com/nuray010](https://github.com/nuray010)
