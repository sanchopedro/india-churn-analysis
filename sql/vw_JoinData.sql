CREATE VIEW vw_JoinData AS
SELECT *
FROM Customer
WHERE Customer_Status = 'Joined';