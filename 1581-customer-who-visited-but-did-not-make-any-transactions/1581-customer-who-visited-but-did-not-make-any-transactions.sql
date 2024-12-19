/* Write your PL/SQL query statement below */

-- select customer_id
-- from Visits LEFT JOIN Transactions on Visits.visit_id=Transactions.visit_id;

select customer_id as customer_id , count(customer_id) as count_no_trans
from Visits 
WHERE Visits.visit_id not in (select visit_id from Transactions) group by customer_id;