"""
This program creates the database that will be used for the main Program.
It will prompt for username, password and database location/parms so it
is easy to access FOR TESTING PURPOSES ONLY!! 

Version: 0.0.0.2
"""

import pymysql

def askUser():

  # Ask the user for database connection info, this data is NOT saved and will exit Noting

  dbHost = input("What is the Database Host Address?: ") # Ask for Database Host
  dbName = input("What is the Database Name?: ") # Ask for Database Name
  dbUsername = input("What is the Database Username?: ") # Ask for Database Username
  dbPassword = input("What is the Database Password?: ") # Asl for Database Password

  createDatabase(dbHost, dbName, dbUsername, dbPassword)

def createDatabase(hostAddr, dbName, dbUser, dbPass):

  # This function will generate the database

  dbLink = pymysql.connect(host=hostAddr, user=dbUser, passwd=dbPass) # Connect to Database
  dbCursor = dbLink.cursor()
  try:
    # Check if Database exists, if not
    if (checkDatabase(dbCursor, dbName)) == False:
      createUserDefined(dbCursor, dbName, 'no') # Passing 'no' to NOT drop table
    else: # If Database does exits ask user if they wish to rebuild
      print("Database NOT Dropped, Checking tables!...")
    dbLink.close()

  # Reopen Database connection and connect to newly created Database

    dbLink = pymysql.connect(host=hostAddr, user=dbUser, passwd=dbPass, db=dbName)
    dbCursor = dbLink.cursor() # Remake Cursor Pointer

  # Check if 'gametitle' table does not exist
    if (checkTable(dbCursor, "gametitle") == False):
    # Create the table and its parms
      dbSQL = """
                CREATE TABLE IF NOT EXISTS `gametitel` (
                    `gameName` varchar(45) NOT NULL PRIMARY KEY COMMENT 'GameTitle',  
                    `portTCPNumbers` int(5) NOT NULL COMMENT 'Server TCP listen ports',  
                    `portUDPNumbers` int(5) NOT NULL COMMENT 'Server UDP listen ports')"""
      dbCursor.execute(dbSQL)
      print("Table gametitle created!...")

    inputData = input("Would you like us to insert data into the database(y/n)?:  ").lower()
    if inputData in ('y', 'yes'):
      print("Inserting Data...")
      insertData(dbCursor) # Pass Cursor to insert data
    else:
      print("Data NOT added to the database!...")

    dbLink.commit()
    print("Database commited!...")

  except:
    # If error, hault
    raise

  finally:
    # Terminate connection
    dbLink.close()
    print("Connection Terminated!...")

def createUserDefined(cursor, databaseName, input):

  # Create the Dabase with name provided by user

  # If the user wants rebuild, drop first
  if (input == 'DROP'):
    print("Dropping Database!")
    dbSQL = "DROP DATABASE '%s'"%(databaseName)
    Cursor.execute(dbSQL)
  # Create the Database
  dbSQL = "CREATE DATABASE IF NOT EXISTS '{0}'".format(databaseName)
  cursor.execute(dbSQL)
  print("Database Created!...")


def checkDatabase(cursor, databaseName):

  # Check if desired Database exists

  dbSQL = ("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{0}'".format(databaseName))
  cursor.execute(dbSQL) # Run the above SQL statement against Database
  dbExists = cursor.fetchone() # Fetch one colum of query for checking

  if (dbExists is None):
    print("Database '%s' does not exits! Will create Now..."%(databaseName))
    return False
  else:
    print("Database '%s' already exists!, Skipping!...")
    return True

def checkTable(cursor, dbTableName):

  # Check to see if the given table is already created, if not use tabel name and cursor

  # Find Input Table
  dbSQL = ("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{0}'".format(dbTableName.replace('\'', '\'\'')))
  cursor.execute(dbSQL) # Run the above SQL statment against Daatabase

  if cursor.fetchone()[0] == 1:
    print("Table %s already exists!..."%(dbTableName))
    return True # Return that the table exists

  else:
    print("Table %s does NOT exits!..."%(dbTableName))
    return False

def insertData(cursor):

  # Inport cursor data into databse

  dbSQL = ("""INSERT INTO gametitle(gameName, portTCPNumbers, portUDPNumbers)
            VALUES ('Day of Defeat S', '27014-27050', '1200, 27000 27015'),
                ('Minecraft', '25565', '25565')""")
  cursor.execute(dbSQL)

if __name__ == "__main__":
  askUser()
