# SPACE X site
[live-demo](https://jokechat.online/)
>*просто был свободный домен*
## Чтобы протестировать его работу Вам необходимо:  
### Клонировать репозиторий  
```bash
git clone https://github.com/fulliam/space_x.git
```
#### Перейти в папку репозитория  
```bash
cd /space_X
```
### Установить зависимости  
```bash
pip instal -r requirements.txt
```
## Создать базу данных, роль   
**Вход под суперпользователем**  
```bash
sudo su postgres
```
**Запуск psql**  
```bash
psql
```
**Создать базу данных**  
```bash
CREATE DATABASE space;
```
**Создать роль для базы данных**  
```bash
CREATE USER admin_space WITH LOGIN PASSWORD 'adminpassword';
```
**Выдать все права на базу данных для роли**  
```bash
GRANT ALL PRIVILEGES ON DATABASE space TO admin_space;
```
### Создать в корневом каталоге бэкэнда файл .env  
```bash
cd /back
```
**Содержимое файла:**  
```bash
SECRET_KEY = mysecretkey
DB_USER = admin_space
DB_PASS = adminpassword
DB_HOST = localhost
DB_PORT = 5432
DB_NAME = space
```
### Создать миграции  
```bash
python3 manage.py makemigrations editor
```
```bash
python3 manage.py migrate
```
### Создать суперпользователя
```bash
python3 manage.py createsuperuser
```
### Получить токен
```bash
python3 manage.py drf_create_token <USER-NAME>
```
>*сохраните токен*
### Запустить сервер
```bash
python3 manage.py runserver
```
**Для корректировки данных, вы може воспользоваться админ-панелью django**  
`http://127.0.0.1:8000/admin`
### Заполнить таблицы начальными данными
```bash
python3 data_for_tables.py
```
### Установить модули фронтенда из его корневой папки:
```bash
cd /front
```
```bash
npm install
```
### Запустить разработку/сборку фронтенда
```bash
npm run serve
```
```bash
npm run build
```
# **По умолчанию фронт :8080 стучится на бэк :8000**
### Автоисправление линтера
```bash
npm run lint -- --fix
```




