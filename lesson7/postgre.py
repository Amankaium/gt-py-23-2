import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(dbname="python_23_2_2", user="postgres", password="postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
sql_command = 'SELECT * FROM Student;'
cur.execute(sql_command)
conn.commit()
records = cur.fetchall()
print(records)
cur.close()
conn.close()

