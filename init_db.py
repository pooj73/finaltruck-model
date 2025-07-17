import sqlite3

conn = sqlite3.connect("fleet.db")  # or your DB filename
c = conn.cursor()

# Create trips table
c.execute('''
CREATE TABLE IF NOT EXISTS trips (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_id TEXT,
    vehicle_id TEXT,
    start_location TEXT,
    end_location TEXT,
    distance REAL,
    fuel_consumed REAL,
    status TEXT
)
''')

# Create trip_closure table
c.execute('''
CREATE TABLE IF NOT EXISTS trip_closure (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_id TEXT,
    closure_date TEXT,
    remarks TEXT,
    is_closed INTEGER
)
''')

conn.commit()
conn.close()
print("✅ Tables initialized")
