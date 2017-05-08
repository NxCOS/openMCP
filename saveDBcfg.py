"""
Save Database Config and Check if exists
"""
#Read config file
def fileRead():
  readFile = open(dbFileName, 'r')
  readLines = readFile.readlines()
  readFile.close()
  return readLines

#Wipe config file for new save
def purgeFile():
  clearFile = open(dbFileName, 'w')
  clearFile.close()

#Save new databse valuse to file
def fileWrite(val):
  writeFile = open(dbFileName, 'a')
  writeFile.write(val)
  writeFile.close()

def main():
  global dbFileName

  valDefine = ['dbHost = ', 'dbName = ', 'dbUserName = ', 'dbPassword = ', "'None'"]
  prompts = ['Please enter Database address: ', 'Please enter Database Name: ', 'Please enter Database UserName: ', 'Please enter Database Password: ']
  dbFileName = 'db.cfg'

  fRead = fileRead()
  clear = purgeFile()

  if 'None' not in fRead[0]:
    resetFile = input("File is already configured, Reset(y/n)?: ")
    if resetFile.lower() in ('y', 'yes'):
      count = 0
      while count < 4:
        reset = ("%s"%(valDefine[count]) + "\'None\' \n")
        fileWrite(reset)
        count += 1
    main()


  count = 0
  for i in fRead:
    if "None" in i:
      promptUser = str(input(prompts[count]))
      fileWrite(valDefine[count] + "\'" + promptUser + "\'" + "\n")
      count += 1

