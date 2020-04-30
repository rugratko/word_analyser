import sqlite3

conn = sqlite3.connect('russian.db')
cur = conn.cursor()
name = '%'+'ост'+'%'
sql = "SELECT * FROM dictionary WHERE word LIKE ?"
cur.execute(sql, (name,))
letters = cur.fetchall()

id = 0
for lt in letters:
    id += 1
    #print("ID: {0}, WORD: {1}, LENGHT: {2}".format(lt[0], lt[1], lt[2]))

print('Amount: {}'.format(id))