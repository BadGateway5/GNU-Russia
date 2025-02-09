from app.db import pool
from psycopg.errors import Error



class User:
    
    def __init__(self):
        pass


    def all_get_users(self):
        with pool.connection() as conn:
            users = conn.execute("""
                    SELECT * FROM users;
                                """).fetchall()
            return users


    def create_user(self, login, password, email, creation_date):
        try:
            with pool.connection() as conn:
                conn.execute("""
                INSERT INTO users(login, password, 
                            email, creation_date)
                VALUES(%s, %s, %s);
                            """, (login, 
                                  password, 
                                  email,
                                  creation_date))
        except Error as e:
            return e
        
    
    def get_user(self, login, password):
        with pool.connection() as conn:
            user = conn.execute("""
                SELECT * FROM users
                WHERE login = %s AND password = %s
                """, (login, password)).fetchone()
            
            return user