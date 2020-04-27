import sqlite3

conn = sqlite3.connect('russian.db')
cur = conn.cursor()

sql = "SELECT id, letter FROM rus_alphabet"
cur.execute(sql)
letters = cur.fetchall()

for lt in letters:
    print("ID: {0}, LETTER: {1}".format(lt[0], lt[1]))
