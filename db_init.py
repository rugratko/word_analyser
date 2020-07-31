import sqlite3
from db_data_reader import load_freq_data, load_name_data

def init_db():
    print('Creating SQLite3 tables...')
    conn = sqlite3.connect("db\word_data.db")
    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS freqList(
                    word_id INTEGER PRIMARY KEY,
                    first_letter TEXT NOT NULL,
                    word TEXT NOT NULL UNIQUE,
                    freq REAL
                    )
                    """)
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS namesList(
                    word_id INTEGER PRIMARY KEY,
                    word TEXT NOT NULL UNIQUE
                    )
                    """)
    conn.commit()
    conn.close()
    print('DB tables are created!')
    

def import_freq():
    conn = sqlite3.connect("db\word_data.db")
    cursor = conn.cursor()
    preloaded_data = load_freq_data()
    for element in preloaded_data:
        try:
            cursor.execute("""INSERT INTO freqList(word, first_letter, freq) VALUES(?, ?, ?)""", (element[0], element[0][0], element[2]))
        except:
            pass
    conn.commit()
    conn.close()
    
    
def import_names():
    conn = sqlite3.connect("db\word_data.db")
    cursor = conn.cursor()
    preloaded_data = load_name_data()
    for element in preloaded_data:
        try:
            cursor.execute("""INSERT INTO namesList(word) VALUES(?)""", (element, ))
        except:
            pass
    conn.commit()
    conn.close()


init_db()
import_freq()
import_names()