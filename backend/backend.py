from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

def get_db_connection():
    conn = sqlite3.connect('customers.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/customers', methods=['GET'])
def get_customers():
    conn = get_db_connection()
    customers = conn.execute('SELECT * FROM customers').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in customers])

@app.route('/customer', methods=['POST'])
def add_customer():
    new_customer = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO customers (LAST_N, FIRST_N, TITLE, STREET, CITY, ZIP, ID_NO, INDEX_NO, ACREAGE, ASSESSMENT, FORFEIT, M_STREET, M_CITY, M_STATE, M_ZIP, D2000, TotalDue, PriorDue, FeePaid, PostAmount, P2000, P2001, P2002, P2003, P2004, P2005, P2006, P2007, P2008, P2009, P2010, P2011, P2012, P2013, P2014, P2015, P2016, P2017, P2018, modified, P2001orig, Counter, P2019, P2020, index2, PIN) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                 (new_customer['LAST_N'], new_customer['FIRST_N'], new_customer['TITLE'], new_customer['STREET'], new_customer['CITY'], new_customer['ZIP'], new_customer['ID_NO'], new_customer['INDEX_NO'], new_customer['ACREAGE'], new_customer['ASSESSMENT'], new_customer['FORFEIT'], new_customer['M_STREET'], new_customer['M_CITY'], new_customer['M_STATE'], new_customer['M_ZIP'], new_customer['D2000'], new_customer['TotalDue'], new_customer['PriorDue'], new_customer['FeePaid'], new_customer['PostAmount'], new_customer['P2000'], new_customer['P2001'], new_customer['P2002'], new_customer['P2003'], new_customer['P2004'], new_customer['P2005'], new_customer['P2006'], new_customer['P2007'], new_customer['P2008'], new_customer['P2009'], new_customer['P2010'], new_customer['P2011'], new_customer['P2012'], new_customer['P2013'], new_customer['P2014'], new_customer['P2015'], new_customer['P2016'], new_customer['P2017'], new_customer['P2018'], new_customer['modified'], new_customer['P2001orig'], new_customer['Counter'], new_customer['P2019'], new_customer['P2020'], new_customer['index2'], new_customer['PIN']))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": new_id}), 201

@app.route('/customer/<int:id>', methods=['PUT'])
def update_customer(id):
    updated_customer = request.get_json()
    conn = get_db_connection()
    conn.execute('''UPDATE customers SET LAST_N = ?, FIRST_N = ?, TITLE = ?, STREET = ?, CITY = ?, ZIP = ?, INDEX_NO = ?, ACREAGE = ?, ASSESSMENT = ?, FORFEIT = ?, M_STREET = ?, M_CITY = ?, M_STATE = ?, M_ZIP = ?, D2000 = ?, TotalDue = ?, PriorDue = ?, FeePaid = ?, PostAmount = ?, P2000 = ?, P2001 = ?, P2002 = ?, P2003 = ?, P2004 = ?, P2005 = ?, P2006 = ?, P2007 = ?, P2008 = ?, P2009 = ?, P2010 = ?, P2011 = ?, P2012 = ?, P2013 = ?, P2014 = ?, P2015 = ?, P2016 = ?, P2017 = ?, P2018 = ?, modified = ?, P2001orig = ?, Counter = ?, P2019 = ?, P2020 = ?, index2 = ?, PIN = ? WHERE ID_NO = ?''',
                 (updated_customer['LAST_N'], updated_customer['FIRST_N'], updated_customer['TITLE'], updated_customer['STREET'], updated_customer['CITY'], updated_customer['ZIP'], updated_customer['INDEX_NO'], updated_customer['ACREAGE'], updated_customer['ASSESSMENT'], updated_customer['FORFEIT'], updated_customer['M_STREET'], updated_customer['M_CITY'], updated_customer['M_STATE'], updated_customer['M_ZIP'], updated_customer['D2000'], updated_customer['TotalDue'], updated_customer['PriorDue'], updated_customer['FeePaid'], updated_customer['PostAmount'], updated_customer['P2000'], updated_customer['P2001'], updated_customer['P2002'], updated_customer['P2003'], updated_customer['P2004'], updated_customer['P2005'], updated_customer['P2006'], updated_customer['P2007'], updated_customer['P2008'], updated_customer['P2009'], updated_customer['P2010'], updated_customer['P2011'], updated_customer['P2012'], updated_customer['P2013'], updated_customer['P2014'], updated_customer['P2015'], updated_customer['P2016'], updated_customer['P2017'], updated_customer['P2018'], updated_customer['modified'], updated_customer['P2001orig'], updated_customer['Counter'], updated_customer['P2019'], updated_customer['P2020'], updated_customer['index2'], updated_customer['PIN'], id))
    conn.commit()
    conn.close()
    return '', 204

@app.route('/customer/delete/<int:id>', methods=['POST'])
def delete_customer(id):
    conn = get_db_connection()
    try:
        # First, retrieve the customer data
        customer = conn.execute('SELECT * FROM customers WHERE ID_NO = ?', (id,)).fetchone()
        
        if customer is None:
            return jsonify({"error": "Customer not found"}), 404

        # Insert the customer into the deleted_customers table
        conn.execute('''INSERT INTO deleted_customers SELECT * FROM customers WHERE ID_NO = ?''', (id,))
        
        # Now delete the customer from the main customers table
        conn.execute('DELETE FROM customers WHERE ID_NO = ?', (id,))
        
        conn.commit()
        return jsonify({"message": "Customer deleted and moved to archive"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/deleted-customers', methods=['GET'])
def get_deleted_customers():
    conn = get_db_connection()
    deleted_customers = conn.execute('SELECT * FROM deleted_customers').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in deleted_customers])

@app.route('/customer/restore/<int:id>', methods=['POST'])
def restore_customer(id):
    conn = get_db_connection()
    try:
        # First, retrieve the customer data from deleted_customers
        customer = conn.execute('SELECT * FROM deleted_customers WHERE ID_NO = ?', (id,)).fetchone()
        
        if customer is None:
            return jsonify({"error": "Deleted customer not found"}), 404

        # Insert the customer back into the main customers table
        conn.execute('''INSERT INTO customers SELECT * FROM deleted_customers WHERE ID_NO = ?''', (id,))
        
        # Now delete the customer from the deleted_customers table
        conn.execute('DELETE FROM deleted_customers WHERE ID_NO = ?', (id,))
        
        conn.commit()
        return jsonify({"message": "Customer restored successfully"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)