-- ==========================================
-- Dimension Table : Fund
-- ==========================================

CREATE TABLE IF NOT EXISTS dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,

    launch_date DATE,

    benchmark TEXT,

    expense_ratio_pct REAL,
    exit_load_pct REAL,

    min_sip_amount INTEGER,
    min_lumpsum_amount INTEGER,

    fund_manager TEXT,

    risk_category TEXT,

    sebi_category_code TEXT
);
-- ==========================================
-- Dimension Table : Date
-- ==========================================

CREATE TABLE IF NOT EXISTS dim_date (

    date_id INTEGER PRIMARY KEY AUTOINCREMENT,

    full_date DATE UNIQUE,

    day INTEGER,

    month INTEGER,

    month_name TEXT,

    quarter INTEGER,

    year INTEGER,

    weekday TEXT
);
-- ==========================================
-- Fact Table : NAV History
-- ==========================================

CREATE TABLE IF NOT EXISTS fact_nav (

    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    full_date DATE,

    nav REAL,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY(full_date)
        REFERENCES dim_date(full_date)
);
-- ==========================================
-- Fact Table : Investor Transactions
-- ==========================================

CREATE TABLE IF NOT EXISTS fact_transactions (

    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    investor_id TEXT,

    transaction_date DATE,

    amfi_code INTEGER,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    city_tier TEXT,

    age_group TEXT,

    gender TEXT,

    annual_income_lakh REAL,

    payment_mode TEXT,

    kyc_status TEXT,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code),

    FOREIGN KEY(transaction_date)
        REFERENCES dim_date(full_date)
);
-- ==========================================
-- Fact Table : Scheme Performance
-- ==========================================

CREATE TABLE IF NOT EXISTS fact_performance (

    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,

    beta REAL,

    sharpe_ratio REAL,

    sortino_ratio REAL,

    std_dev_ann_pct REAL,

    max_drawdown_pct REAL,

    aum_crore REAL,

    expense_ratio_pct REAL,

    morningstar_rating INTEGER,

    risk_grade TEXT,

    FOREIGN KEY(amfi_code)
        REFERENCES dim_fund(amfi_code)
);
-- ==========================================
-- Fact Table : AUM
-- ==========================================

CREATE TABLE IF NOT EXISTS fact_aum (

    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_house TEXT,

    month TEXT,

    aum_crore REAL
);