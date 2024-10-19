import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()
    
    # Drop the tables if they exist to prevent errors on rerun
    cursor.execute('DROP TABLE IF EXISTS customers')
    cursor.execute('DROP TABLE IF EXISTS deleted_customers')
    
    # Create customers table
    cursor.execute('''
        CREATE TABLE customers (
            LAST_N TEXT,
            FIRST_N TEXT,
            TITLE TEXT,
            STREET TEXT,
            CITY TEXT,
            ZIP TEXT,
            ID_NO INTEGER PRIMARY KEY,
            INDEX_NO INTEGER,
            ACREAGE REAL,
            ASSESSMENT REAL,
            FORFEIT TEXT,
            M_STREET TEXT,
            M_CITY TEXT,
            M_STATE TEXT,
            M_ZIP TEXT,
            D2000 REAL,
            TotalDue REAL,
            PriorDue REAL,
            FeePaid REAL,
            PostAmount REAL,
            P2000 REAL,
            P2001 REAL,
            P2002 REAL,
            P2003 REAL,
            P2004 REAL,
            P2005 REAL,
            P2006 REAL,
            P2007 REAL,
            P2008 REAL,
            P2009 REAL,
            P2010 REAL,
            P2011 REAL,
            P2012 REAL,
            P2013 REAL,
            P2014 REAL,
            P2015 REAL,
            P2016 REAL,
            P2017 REAL,
            P2018 REAL,
            modified TEXT,
            P2001orig REAL,
            Counter INTEGER,
            P2019 REAL,
            P2020 REAL,
            index2 INTEGER,
            PIN TEXT
        )
    ''')

    # Create deleted_customers table
    cursor.execute('''
        CREATE TABLE deleted_customers (
            LAST_N TEXT,
            FIRST_N TEXT,
            TITLE TEXT,
            STREET TEXT,
            CITY TEXT,
            ZIP TEXT,
            ID_NO INTEGER PRIMARY KEY,
            INDEX_NO INTEGER,
            ACREAGE REAL,
            ASSESSMENT REAL,
            FORFEIT TEXT,
            M_STREET TEXT,
            M_CITY TEXT,
            M_STATE TEXT,
            M_ZIP TEXT,
            D2000 REAL,
            TotalDue REAL,
            PriorDue REAL,
            FeePaid REAL,
            PostAmount REAL,
            P2000 REAL,
            P2001 REAL,
            P2002 REAL,
            P2003 REAL,
            P2004 REAL,
            P2005 REAL,
            P2006 REAL,
            P2007 REAL,
            P2008 REAL,
            P2009 REAL,
            P2010 REAL,
            P2011 REAL,
            P2012 REAL,
            P2013 REAL,
            P2014 REAL,
            P2015 REAL,
            P2016 REAL,
            P2017 REAL,
            P2018 REAL,
            modified TEXT,
            P2001orig REAL,
            Counter INTEGER,
            P2019 REAL,
            P2020 REAL,
            index2 INTEGER,
            PIN TEXT
        )
    ''')
    conn.commit()

    # Load data from CSV
    df = pd.read_csv(r'C:\Users\jcbla\PythonProjects\SideBusiness_Billing_system\CustomerDataCleaned.csv', low_memory=False)
    df.to_sql('customers', conn, if_exists='append', index=False)
    
    conn.close()

if __name__ == '__main__':
    init_db()