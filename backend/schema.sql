CREATE TABLE customers (
    id_no INTEGER PRIMARY KEY,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    title TEXT,
    street TEXT,
    city TEXT,
    zip TEXT,
    m_street TEXT,
    m_city TEXT,
    m_state TEXT,
    m_zip TEXT,
    acreage REAL,
    assessment REAL,
    pin TEXT,
    total_due REAL,
    fee REAL
);
