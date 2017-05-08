"""
Local database link test
"""
import pymysql

def importCfg():
  readCfg = open("db.cfg", 'r')
  readLines = readCfg.readlines()
  readCfg.close()
  return readLines

def main():

  saveVals = importCfg()
  vL = []
  for i in saveVals:
    vL.append(i.split('\'')[1].split('\'')[0])

  dbLink = pymysql.connect(host=vL[0], user=vL[2], passwd=vL[3], db=vL[1])
  dbCursor = dbLink.cursor()
  print("Mo Errors!...")
  dbLink.close()



