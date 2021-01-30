import psycopg2

conn = psycopg2.connect(
    "postgres://bdyfetakcxtjem:18cfa4a4b4672a76b4eaaec4aff9bde1eb1303711fb74f85795577eda7bec83a@ec2-3-230-247-88"
    ".compute-1.amazonaws.com:5432/d1ccsc56pnpc4p")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE SPENDS
(
    number INTEGER PRIMARY KEY,
    name TEXT,
    time TEXT,
    type TEXT,
    amount NUMERIC
)""")
conn.commit()