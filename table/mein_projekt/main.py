import mysql.connector
import pandas as pd
import os

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'mydatabase')
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table():
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    age INT,
                    result FLOAT
                )
            ''')
            print("Table created successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

def insert_data(file_path):
    connection = connect_to_db()
    if connection:
        try:
            data = pd.read_csv(file_path)
            cursor = connection.cursor()
            for _, row in data.iterrows():
                cursor.execute('''
                    INSERT INTO users (name, age, result)
                    VALUES (%s, %s, %s)
                ''', (row['name'], row['age'], row['result']))
            connection.commit()
            print("Data inserted successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

def fetch_data():
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_table()
    insert_data("data/sample_data.csv")
    data = fetch_data()
    if data:
        for row in data:
            print(row)