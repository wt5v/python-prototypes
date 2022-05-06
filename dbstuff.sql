SELECT *
  FROM customers c;
 
SELECT c.customerName, o2.quantityOrdered, o2.priceEach, o.orderDate, o.status, o.comments
  FROM orders o, customers c, orderdetails o2
 WHERE o.customerNumber = c.customerNumber
   AND o.orderNumber - o2.orderNumber
   AND o.comments IS NOT NULL
   AND o.status in ('On Hold', 'Disputed');

CREATE USER 'wt5v'@'192.168.1.31' IDENTIFIED BY 'kdog2558';
  
 GRANT ALL PRIVILEGES ON * . * TO 'wt5v'@'192.168.1.31';