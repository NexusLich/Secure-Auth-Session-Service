# Secure Authentication & Session Management Microservice

A dedicated backend service providing secure user authentication, authorization, and lightning-fast session management.

## 🚀 Tech Stack
* **Language:** Python
* **Framework:** Django / DRF
* **Session Storage & Caching:** Redis
* **Tools:** Git, Linux

## 📌 Key Features
* **Role-Based Access Control (RBAC):** Granular permission system for different user types.
* **Token & Session Management:** Utilizes Redis for fast, secure storage and validation of user sessions and access tokens.
* **Security Hardening:** Implemented protection measures against common web vulnerabilities, password hashing, and endpoint security testing.

## 🛠️ Getting Started Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/NexusLich/secure-auth-session-service.git](https://github.com/NexusLich/secure-auth-session-service.git)
   cd secure-auth-session-service

2. Set up virtual environment and install requirements:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Run migrations and start the server:
    ```bash
    python manage.py migrate
    python manage.py runserver

#_________________________________________________________________

# Secure Authentication & Session Management Microservice

Специализированный бэкенд-микросервис, обеспечивающий безопасную аутентификацию, авторизацию и высокоскоростное управление пользовательскими сессиями.

## 🚀 Технологический стек
* **Язык программирования:** Python
* **Фреймворк:** Django / DRF
* **Хранение сессий и кэш:** Redis
* **Инструменты:** Git, Linux

## 📌 Основной функционал
* **Контроль доступа на основе ролей (RBAC):** Гибкая система разграничения прав для различных типов пользователей.
* **Управление сессиями и токенами:** Использование Redis для быстрого и безопасного хранения, проверки сессий и токенов доступа.
* **Усиление безопасности:** Реализованы защитные механизмы против распространенных веб-уязвимостей, хеширование паролей и тестирование эндпоинтов.

## 🛠️ Локальный запуск
1. Клонируйте репозиторий:
   ```bash
   git clone [https://github.com/NexusLich/secure-auth-session-service.git](https://github.com/NexusLich/secure-auth-session-service.git)
   cd secure-auth-session-service

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt

4. Выполните миграции и запустите сервер:
    ```bash
    python manage.py migrate
    python manage.py runserver