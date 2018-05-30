#!/python3
import mysql.connector
import time

config = {
  'user': 'ODBC',
  'password': '123',
  'host': '192.168.84.21',
  'database': 'hmsipspotsign',
  'raise_on_warnings': True,
  'use_pure': False,
  'port': 3306
}

print("conectando")
cnx = mysql.connector.connect(**config)
print("conectado :)")
time.sleep(10)
cnx.close()
