#!/python3
import mysql.connector
import time

#mySQL configuration parameters
config = {
  'user': 'ODBC',
  'password': '123',
  'host': '192.168.84.21',
  'database': 'hmsipspotsign',
  'raise_on_warnings': True,
  'use_pure': False,
  'port': 3306
}

#Connect with mySQL server
print("conectando")
cnx = mysql.connector.connect(**config)
print("conectado :)")
time.sleep(5)

#Buffer cursor
curA = cnx.cursor(buffered=True)

#Configure query
query = ("select * FROM mxr_patrones_terminal WHERE COD_TERMINAL = 1426959; ")
#Launch query
curA.execute(query)
for (cod_patron) in curA:
  print("Probando".format(cod_patron))


cnx.close()
