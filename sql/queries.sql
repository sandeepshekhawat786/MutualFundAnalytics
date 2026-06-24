-- 1 Top 5 Funds by AUM

SELECT scheme_name,aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

---------------------------------------------------

-- 2 Average NAV by Month

SELECT
strftime('%m',full_date) Month,
AVG(nav) Average_NAV
FROM fact_nav
GROUP BY Month;

---------------------------------------------------

-- 3 Total Transactions by State

SELECT
state,
COUNT(*) Transactions
FROM fact_transactions
GROUP BY state
ORDER BY Transactions DESC;

---------------------------------------------------

-- 4 Funds with Expense Ratio below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct<1;

---------------------------------------------------

-- 5 Highest Sharpe Ratio

SELECT
scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

---------------------------------------------------

-- 6 Highest Alpha

SELECT
scheme_name,
alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 10;

---------------------------------------------------

-- 7 Highest 5 Year Return

SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

---------------------------------------------------

-- 8 Average Transaction Amount

SELECT
AVG(amount_inr)
FROM fact_transactions;

---------------------------------------------------

-- 9 Transactions by Type

SELECT
transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

---------------------------------------------------

-- 10 Top Fund Houses

SELECT
fund_house,
COUNT(*) Schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY Schemes DESC;