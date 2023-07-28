import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="space",
    user="admin_space",
    password="adminpassword"
)

# Создание курсора
cur = conn.cursor()

# Заполнение таблицы Menu данными
menu_data = [
    ("Контакты", "/contact"),
    ("О Компании", "/about"),
    ("Гарантии", "/"),
    ("График полетов", "/"),
    ("Технологии", "/"),
    ("Главная", "/")
]

for data in menu_data:
    cur.execute("INSERT INTO edit_menu (title, url) VALUES (%s, %s)", data)

# Заполнение таблицы InfoCard данными
info_card_data = [
    ("путешествие", 597, None, "дней"),
    ("календарик за", 2001, "г.", "в подарок"),
    ("гарантируем", 50, "%", "безопасность"),
    ("МЫ", 1, None, "на рынке")
]

for data in info_card_data:
    cur.execute("INSERT INTO edit_infocard (top, middle_number, middle_text, bottom) VALUES (%s, %s, %s, %s)", data)

# Фиксация изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()

