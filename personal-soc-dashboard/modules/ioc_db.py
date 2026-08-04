import os
import psycopg2
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS iocs (
            id SERIAL PRIMARY KEY,
            indicator TEXT NOT NULL,
            type TEXT NOT NULL,
            threat_level TEXT,
            notes TEXT,
            date_added TEXT
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def add_ioc(indicator, ioc_type, threat_level, notes):
    conn = get_connection()
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO iocs (indicator, type, threat_level, notes, date_added)
        VALUES (%s, %s, %s, %s, %s)
        ''', (indicator, ioc_type, threat_level, notes, timestamp))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_iocs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM iocs ORDER BY id DESC")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def delete_ioc(ioc_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM iocs WHERE id = %s", (ioc_id,))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized (PostgreSQL).")