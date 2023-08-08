## Fastapi project

Проект для торговли, включает в себя: Аутентификация по jwt токену, базу данных с таблицами для пользователей, ролями пользователей и их операциями, реализован динамичный онлайн чат, разработаны фоновые задачи с возможностью отправки отчета по email, написал тесты на проверку добавления данных в тестовую БД, создан образ проекта запушен на dockerhub и развернут в контейнерах.

## Стек

- Python
- Fastapi
- Docker
- sqlalchemy
- pydantic
- celery
- Postgres
- aiohttp

## Запуск проекта

Клонируем репозиторий

```bash
  git clone git@github.com:EgorFedotov/trading_app.git
```

Устанавливаем и активируем виртуальное окружение

```bash
  py -3.7 -m venv venv
  source venv/Scripts/activate
```

Устанавливаем зависимости из файла requirements.txt
```bash
  pip install -r requirements.txt
```

В корне проекта создаем файл .env и добавляем туда:

- DB_USER= <имя пользователя бд>
- DB_PASS= <пароль от бд>
- DB_HOST= localhost
- DB_PORT= 5432
- DB_NAME= <имя бд>

- REDIS_HOST=redis
- REDIS_PORT=5050
  
- FASTAPI_USER= <google почту для отправики отчетов >
- FASTAPI_PASS= <В настройках включить двухфакторную аутентификация, далее в разделе «пароли приложений» добавить приложение и записать пароль>

Создаем в корне прокта файл .env-docker и добавляем туда:

- DB_USER= <имя пользователя бд>
- DB_PASS= <пароль от бд>
- DB_HOST= localhost
- DB_PORT= 5432
- DB_NAME= <имя бд>

- POSTGRES_DB=<название БД>
- POSTGRES_USER=<имя пользователя БД>
- POSTGRES_PASSWORD=<пароль к БД>

- REDIS_HOST=redis
- REDIS_PORT=5050

- FASTAPI_USER=egorfedotovarz@gmail.com
- FASTAPI_PASS=wfnuhrudtyqkgrck

# Для запуска контейнеров в корне проекта выполните команду:

```bash
  docker compose up
```

После запуска контейнеров документация доступна по адресу
 http://localhost:9999/docs/

Фоновые задачи можно посмотреть по адресу 
 http://localhost:8888/tasks
