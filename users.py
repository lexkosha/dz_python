import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Путь до бд
DB_PATH = 'sqlite:///sochi_athletes.sqlite3'

# Базовый класс 
Base = declarative_base()

class User(Base):
    # Указываем имя таблицы
    __tablename__ = 'user'
    id = sa.Column(sa.INTEGER, primary_key=True, autoincrement=True)
    # Имя
    first_name = sa.Column(sa.TEXT)
    # Фамилия
    last_name = sa.Column(sa.TEXT)
    # Пол
    gender = sa.Column(sa.TEXT)
    # почта
    email = sa.Column(sa.TEXT)
    # Дата рождения
    birthdate = sa.Column(sa.TEXT)
    # рост
    height = sa.Column(sa.REAL)

def connect_db():
    """
    Устанавливаем соединение с базой, создаем таблицу если ее нет:
    Base.metadata.create_all(engine)
    """
    # Создаем соединение с бащой
    engine = sa.create_engine(DB_PATH)
    # создаем описание таблицы если ее нет
    Base.metadata.create_all(engine)
    # Создаем фабрику сессию
    session = sessionmaker(engine)

    # Возвращаем сессию 
    return session


def request_user_data():
    """
    Получаем данные у пользователя
    """
    print('Привет! Я запишу данные которые ты введешь ;)')
    # Запрашиваем данне у пользователя
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    gender = input('Введите возраст: ')
    email = input('Введите email: ')
    birthdate = input('Введите дату рождения: ')
    height = float(input('Введите рост: '))

    #Создаем нового пользователя используя class User
    user = User(
        first_name = first_name,
        last_name = last_name,
        gender = gender,
        email = email,
        birthdate = birthdate,
        height = height
    )

    # Возвращаем юзера
    return user

def main():
    """
    Работаем с юзером через терминал)
    """
    session = connect_db()
    # запросим данные у пользователя
    user = request_user_data()
    # Добавим нового пользователя 
    session.add(user)
    # Сохраним накопленные изменения
    session.commit()
    print('Данные сохранены успешно!')

if __name__ == "__main__":
    main()

