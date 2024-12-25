# Write your MySQL query statement below

WITH CTE AS (
    SELECT 
        s.user_id, 
        COUNT(*) AS Total, 
        SUM(IF(c.action = 'confirmed', 1, 0)) AS ConfirmedAmount
    FROM Signups s 
    LEFT JOIN Confirmations c ON s.user_id = c.user_id
    GROUP BY s.user_id
)
SELECT 
    c.user_id,
    ROUND(c.ConfirmedAmount / c.Total, 2) AS Confirmation_Rate
FROM CTE AS c;