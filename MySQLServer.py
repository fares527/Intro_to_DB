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
       
    

