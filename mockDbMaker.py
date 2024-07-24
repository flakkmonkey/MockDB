import sqlite3
import random

# Function to generate random product names
def generate_product_name(i):
    return f'Product_{i}'

# Function to generate random locations in the format "R-1.2.3"
def generate_location():
    aisle = random.randint(1, 9)  # Choose a random integer between 1 and 9
    bay = random.randint(1, 9)  # Choose another random integer between 1 and 9
    shelf = random.randint(1, 9)  # Choose another random integer between 1 and 9
    return f'R-{aisle}.{bay}.{shelf}'

# Function to generate random quantity
def generate_quantity():
    return random.randint(1, 1000)

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('large_inventory.db')

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create an inventory table if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    location TEXT NOT NULL
)
''')

# Commit the changes to ensure the table is created
conn.commit()

# Generate mock data for the inventory
# Using a list comprehension to create 10,000 records
inventory_data = [(generate_product_name(i), generate_quantity(), generate_location()) for i in range(1, 100)]

# Insert the generated data into the inventory table
cursor.executemany('''
INSERT INTO inventory (product_name, quantity, location)
VALUES (?, ?, ?)
''', inventory_data)

# Commit the changes to save the data in the database
conn.commit()

# Query the data to verify the insertion
# Limit the query to 10 rows for a quick preview
cursor.execute('SELECT * FROM inventory LIMIT 10')

# Fetch all the rows from the query result
rows = cursor.fetchall()

# Print each row to the console
for row in rows:
    print(row)

# Close the database connection
conn.close()
