CREATE VIEW vw_ChurnData AS
SELECT *
FROM Customer
WHERE Customer_Status IN ('Churned', 'Stayed');
