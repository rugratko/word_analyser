import sqlite3

print('Application is running...')

conn = sqlite3.connect('russian.db')
cur = conn.cursor()

CreateRussianTables = True
CreateAlphabet = True

alphabet = 'а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я'.split(', ')

if CreateAlphabet:
    task = "CREATE TABLE IF NOT EXISTS rus_alphabet (id INTEGER PRIMARY KEY, let_id INTEGER, letter TEXT)"
    cur.execute(task)

if CreateRussianTables:
    task_creator = "CREATE TABLE IF NOT EXISTS dictionary (id INTEGER PRIMARY KEY, word TEXT, lenght TEXT)"
    cur.execute(task_creator)

conn.close()

