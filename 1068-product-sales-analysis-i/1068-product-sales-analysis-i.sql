/* Write your PL/SQL query statement below */

select product_name, year, price

from Sales INNER JOIN  Product  
on Sales.product_id=Product.product_id;