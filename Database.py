import sqlite3
import pandas as pd

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect('rohith.sqlite')

# Load CSV files into pandas DataFrames
df = pd.read_csv("https://github.com/RohithMukkamula/DataBase/blob/main/Customers.csv", encoding='ISO-8859-1')
df1 = pd.read_csv("https://github.com/RohithMukkamula/DataBase/blob/main/Sales.csvv", encoding='ISO-8859-1')
df2 = pd.read_csv("https://github.com/RohithMukkamula/DataBase/blob/main/Exchange_rates.csv", encoding='ISO-8859-1')
df3 = pd.read_csv("https://github.com/RohithMukkamula/DataBase/blob/main/Products.csv", encoding='ISO-8859-1')
df4 = pd.read_csv("https://github.com/RohithMukkamula/DataBase/blob/main/Stores.csv", encoding='ISO-8859-1')

# Write DataFrames to SQLite tables
df.to_sql('Customers', conn, if_exists='replace', index=False)
df1.to_sql('Sales', conn, if_exists='replace', index=False)
df2.to_sql('Exchange_rates', conn, if_exists='replace', index=False)
df3.to_sql('Products', conn, if_exists='replace', index=False)
df4.to_sql('Stores', conn, if_exists='replace', index=False)

# Execute SQL query on the 'Customers' table
cursor = conn.execute('SELECT * FROM Customers')
results = cursor.fetchall()
print(results)

# Close connection
conn.close()
