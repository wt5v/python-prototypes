import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='wt5v', password="kdog2558", database='classicmodels', host='192.168.1.213')
  cursor = cnx.cursor()
  query = "select customerNumber, customerName, city, state \
             from customers \
            where country = 'USA'"
  cursor.execute(query)

  for (customerNumber, customerName, city, state) in cursor:
      print("{}, {}, {}, {}".format(customerNumber, customerName, city, state));

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor.close()
  cnx.close()
