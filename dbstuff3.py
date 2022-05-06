import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='wt5v', password="kdog2558", database='classicmodels', host='GK-mini.lan')
  cursor = cnx.cursor()
#  query = "select customerNumber, customerName, city, state from customers"
  query = "SELECT c.customerName, sum(o2.quantityOrdered), sum(o2.priceEach) \
             FROM customers c, orders o, orderdetails o2 \
            WHERE c.customerNumber = o.customerNumber \
              AND o.orderNumber = o2.orderNumber \
          GROUP BY c.customerName"

  cursor.execute(query)

  for (customerName, quantityOrdered, priceEach) in cursor:
      print("{}, {}, {}".format(customerName, quantityOrdered, priceEach));

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
