import sqlite3
from datetime import datetime

DB_NAME = "iocs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS iocs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            indicator TEXT NOT NULL,
            type TEXT NOT NULL,
            threat_level TEXT,
            notes TEXT,
            date_added TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_ioc(indicator, ioc_type, threat_level, notes):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO iocs (indicator, type, threat_level, notes, date_added)
        VALUES(?,?,?,?,?)
        ''', (indicator, ioc_type, threat_level, notes, timestamp))
    conn.commit()
    conn.close()

def get_all_iocs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM iocs")
    rows = cursor.fetchall()
    conn.close()
    return rows
def delete_ioc(ioc_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM iocs WHERE id = ?", (ioc_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    add_ioc("185.220.101.1", "IP", "Critical", "Known Tor exit node, high abuse score")
    all_iocs = get_all_iocs()
    for row in all_iocs:
        print(row)