-- Create the table
CREATE TABLE sales_data (
    sale_id SERIAL PRIMARY KEY,
    sale_date DATE,
    region VARCHAR(50),
    amount NUMERIC
);

-- Insert dummy data (Regions: North, South)
INSERT INTO sales_data (sale_date, region, amount) VALUES
('2023-01-01', 'North', 100),
('2023-01-02', 'North', 150), -- Growth
('2023-01-03', 'North', 150), -- Tie
('2023-01-04', 'North', 200),
('2023-01-05', 'North', 100), -- Drop
('2023-01-01', 'South', 500),
('2023-01-02', 'South', 550),
('2023-01-03', 'South', 520);

SELECT * FROM sales_data;

-- shows the cumulative sum of sales per region, ordered by date
SELECT 
    sale_date, 
    region, 
    amount,
    SUM(amount) OVER (PARTITION BY region ORDER BY sale_date) as running_total
FROM sales_data;

-- shows the previous day's sales amount for each region
select 
	sale_date,
    region,
	amount,
	LAG(amount) OVER(partition by region order by sale_date) as previous_day_amount
from sales_data;

-- shows the rank of each sale amount within its region
select 
	sale_date,
	region,
	amount,
	RANK() OVER (partition by region order by amount DESC)
from sales_data;

