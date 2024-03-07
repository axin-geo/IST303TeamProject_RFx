import sqlite3

connection = sqlite3.connect('database.db')

try:
    with open('schema.sql') as f:
        connection.executescript(f.read())
    print("Schema executed successfully.")
except Exception as e:
    print(f"Error executing schema: {e}")

cur = connection.cursor()

try:
    cur.execute("INSERT INTO rfx_owner_tbl (rfx_name, owner_name, email, team) VALUES (?, ?, ?, ?)",
                ('Clip','Aote', 'aote.xin@cgu.edu', "Team3"))
    cur.execute("INSERT INTO rfx_owner_tbl (rfx_name, owner_name, email, team) VALUES (?, ?, ?, ?)",
                ('Plus', 'Akhilesh', 'Akhilesh@cgu.edu', "Team3"))
    cur.execute("INSERT INTO rfx_owner_tbl (rfx_name, owner_name, email, team) VALUES (?, ?, ?, ?)",
            ('Detect Bright Ocean Object', 'Mohammed', 'mohammed.alfawzan@cgu.edu', "Team3"))
    connection.commit()
    print("Data inserted successfully.")
except sqlite3.OperationalError as e:
    print(f"Error inserting data: {e}")

connection.commit()
connection.close()