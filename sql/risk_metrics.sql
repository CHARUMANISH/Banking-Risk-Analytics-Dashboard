WITH risk_base AS (
    SELECT
        customer_id,
        loan_amount,
        annual_income,
        credit_utilization,
        missed_payments,
        (loan_amount / annual_income) AS loan_to_income_ratio
    FROM loan_data
)

SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN missed_payments > 2 THEN 1 ELSE 0 END) AS high_risk_customers,
    ROUND(
        SUM(CASE WHEN missed_payments > 2 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS high_risk_percentage
FROM risk_base;
