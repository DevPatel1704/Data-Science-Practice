import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db7"
)

cursor = conn.cursor()

# Create employee table
create_table_query = """
CREATE TABLE IF NOT EXISTS employee (
    eid INT PRIMARY KEY,
    ename VARCHAR(100),
    esalary FLOAT
)
"""
cursor.execute(create_table_query)
print("Employee table created successfully.")

# Close connection
cursor.close()
conn.close()