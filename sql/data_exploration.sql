SELECT Gender,
    COUNT(Gender) AS TotalCount,
    COUNT(Gender) * 100.0 / (
        SELECT COUNT(*)
        FROM Customer
    ) AS Percentage
FROM Customer
GROUP BY Gender;
GO

SELECT Contract,
    Count(Contract) AS TotalCount,
    Count(Contract) * 100.0 / (
        Select Count(*)
        from Customer
    ) AS Percentage
from Customer
Group by Contract;
GO

SELECT Customer_Status,
    Count(Customer_Status) as TotalCount,
    Sum(Total_Revenue) as TotalRev,
    Sum(Total_Revenue) / (
        Select sum(Total_Revenue)
        from Customer
    ) * 100 as RevPercentage
from Customer
Group by Customer_Status;
GO

SELECT State,
    Count(State) as TotalCount,
    Count(State) * 100.0 / (
        Select Count(*)
        from Customer
    ) as Percentage
from Customer
Group by State
Order by Percentage desc