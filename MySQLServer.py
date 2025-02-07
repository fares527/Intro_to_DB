import mysql.connector

def create_database(host, user, password, database):

   try:
       mydb = mysql.connector.connect(
           host = host,
           user = user,
           password = password,
           
        )
       cursor = mydb.cursor()

       cursor.execute(f"CREATE DATABASE IF NOT EXIST {database}")
       mydb.commit()

       print(f"Database '{database}' created successfully!")
       return True
   
   except mysql.connector.Error as err:
       print(f"Error creating database: {err}")
       return False
   
   cursor.close()
   mydb.close()

if __name__ == "__main__":
    # Replace with your actual MySQL server credentials
    host = "localhost"
    user = "your_username"
    password = "your_password"
    database = "alx_book_store"

    if create_database(host, user, password, database):
        print("Database creation successful.")
    else:
        print("Database creation failed.")
       
    

