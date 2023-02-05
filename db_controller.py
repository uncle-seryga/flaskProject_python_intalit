import sqlite3
from datetime import datetime


class DB:
    _connection = sqlite3.connect('app/static/database/database.db', check_same_thread=False)
    _cursor = _connection.cursor()
    table_name: str

    def __init__(self):
        print(f"DB updated @ {str(datetime.now())[:-7]}")
        with open("app/static/database/setStrucure.sql", 'r') as file:
            self._cursor.executescript(file.read())


class Users(DB):
    table_name = "users"

    def add(self, login: str, password: str):
        self._cursor.execute(f"""INSERT INTO {self.table_name} VALUES (NULL,?,?)""", (login, password))
        self._connection.commit()

    def get(self, login) -> list:
        self._cursor.execute(f"""SELECT * FROM {self.table_name} WHERE login =?""", (login,))
        return self._cursor.fetchall()

    def delete(self, login):
        pass

    def update_password(self, login):
        pass


class Support:
    def check_if_password_valid(self, password1, password2):
        if password1 == password2:
            if [self.__condition_1(password1),
                self.__condition_2(password2),
                self.__condition_3(password1)].count(True) == 3:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def __condition_1(password: str):
        """
        If any uppercase letter in password
        :param password:
        :return:
        """
        for x in password:
            if x == x.upper():
                return True
        else:
            return False

    @staticmethod
    def __condition_2(password: str):
        """
        If any number in password
        :param password:
        :return:
        """
        for x in password:
            if x.isdigit():
                return True
        else:
            return False

    @staticmethod
    def __condition_3(password: str):
        """
        if any special sign in password
        :param password:
        :return:
        """
        for x in "-_.,?/=+!@#$%^&*:;":
            if x in password:
                return True
        else:
            return False


class Player(DB):
    table_name = "player"

    def add(self, username, DOB, telegram_id):
        __default_pic = "/app/static/img/users_profile_pics/default.png"
        self._cursor.execute(f"""INSERT INTO {self.table_name} VALUES (NULL,?,?,?,?)""",
                             (username, __default_pic, DOB, telegram_id,))


class Gamefield(DB):
    table_name = 'gamefield'

    def get_all_data(self):
        self._cursor.execute(f"""SELECT * FROM {self.table_name}""")
        return self._cursor.fetchall()


class Words(DB):
    table_name = 'words'

    def get_all(self) -> list:
        self._cursor.execute(f"""SELECT * FROM {self.table_name}""")
        return self._cursor.fetchall()
