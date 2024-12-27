# Write your MySQL query statement below
 
 

seLECT prices.product_id, COALESCE(round(sum(units*price )/sum(units),2),0)  AS average_price

from prices 
left join UnitsSold on prices.product_id=UnitsSold.product_id AND UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date group by prices.product_id ;
