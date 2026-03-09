import sqlite3

def create_customer(name, email, phone):
    try:
        conn = sqlite3.connect('customers.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, email, telefono) VALUES (?, ?, ?)")
        params = (name, email, phone)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Error creating customer: {e}")
        return False

def list_customers():
    try:
        conn = sqlite3.connect('customers.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, email, telefono FROM customers")
        results = cursor.fetchall()
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Tel: {row[3]}")
    except sqlite3.Error as e:
        print(f"Error listing customers: {e}")
    finally:
        conn.close()

def update_customer(id, name, email, phone):
    try:
        conn = sqlite3.connect('customers.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE customers SET name=?, email=?, telefono=? WHERE id=?", (name, email, phone, id))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Error updating customer: {e}")
        return False

def delete_customer(id):
    try:
        conn = sqlite3.connect('customers.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers WHERE id=?", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting customer: {e}")
        return False

if __name__ == "__main__":
    # Create a new database if it doesn't exist
    if not os.path.exists('customers.db'):
        with open('customers.db', 'w') as conn_file:
            conn_file.write("id,name,email,telefono\n")
    
    print("Welcome to Customers Database")
    # Create a customer
    create_customer("John Doe", "john@example.com", 55555563)
    # List all customers
    list_customers()
    # Update a customer
    update_customer(2, "Jane Smith", "jane@example.com", 88888870)
    # Delete a customer (assuming there is one to delete)
    delete_customer(1)
    print("All operations completed successfully.")