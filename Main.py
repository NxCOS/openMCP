"""
Primary exec
"""


#Configure Database config file
def saveDBcfg():
  import saveDBcfg
  saveDBcfg.main()

#Check if all is working and cofig save was successful
def checkDB():
  import sqlAccess
  sqlAccess.main()


def main():
  saveDBcfg()
  checkDB()
  print("EOL")

if __name__ == "__main__":
  main()
