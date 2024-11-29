import pymysql
from pymysql.cursors import Cursor


class Database:
    def __init__(self, db_name, db_password, db_user, db_port, db_host):
        self.db_name = db_name
        self.db_password = db_password
        self.db_user = db_user
        self.db_port = db_port
        self.db_host = db_host

    def connect(self):
        return pymysql.Connection(
            database=self.db_name,
            user=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            cursorclass=pymysql.cursors.DictCursor
        )

    def execute(self, sql: str, params: tuple = (), commit=False, fetchone=False, fetchall=False) -> tuple | list:
        database = self.connect()
        cursor = database.cursor()
        cursor.execute(sql, params)

        data = None

        if fetchone:
            data = cursor.fetchone()

        elif fetchall:
            data = cursor.fetchall()

        if commit:
            database.commit()

        cursor.close()
        database.close()
        return data

    def create_users_table(self):
        sql = """   
            CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY AUTO_INCREMENT,
            telegram_id VARCHAR(100) NOT NULL UNIQUE,
            fullname VARCHAR(100) NOT NULL,
            username VARCHAR(100)
            )
        """
        self.execute(sql)

    def create_movies_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS movies(
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100) NOT NULL,
            movie_id VARCHAR(50) NOT NULL
            )
        """
        self.execute(sql)

    def get_movie_id(self, movie_id):
        sql = """
            SELECT movie_id FROM movies 
            WHERE id = %s
        """
        return self.execute(sql, (movie_id,), fetchone=True)

    def register_user(self, telegram_id, fullname, username):
        sql = """
            INSERT INTO users(telegram_id,fullname,username)
            VALUES(%s,%s,%s)
        """
        self.execute(sql, (telegram_id, fullname, username), commit=True)

    def get_user(self, telegram_id):
        sql = """
            SELECT * FROM users WHERE telegram_id = %s 
        """
        return self.execute(sql, (telegram_id,), fetchone=True)

    def get_users(self):
        sql = """
            SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)

    def get_movies(self):
        sql = """
            SELECT * FROM movies
        """
        return self.execute(sql, fetchall=True)
