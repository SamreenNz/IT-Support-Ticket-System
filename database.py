import mysql.connector


try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="it_support"
    )

    if connection.is_connected():
        print("Successfully connected to MySQL!")
        print("Database: it_support")

except mysql.connector.Error as error:
    print("Database connection failed!")
    print("Error:", error)