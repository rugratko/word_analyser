import sqlite3

print('Application is running...')

conn = sqlite3.connect('russian.db')
cur = conn.cursor()

CreateRussianTables = True
CreateAlphabet = True

alphabet = 'а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я'.split(', ')

if CreateAlphabet:
    for letter in alphabet:
        task = "CREATE TABLE IF NOT EXISTS rus_alphabet (id INTEGER PRIMARY KEY, let_id INTEGER, letter TEXT)"
        cur.execute(task)

if CreateRussianTables:
    print('Filling word table...')
    task_export = "SELECT letter FROM rus_alphabet"
    letter_list = cur.execute(task_export)
    for letter in letter_list:
        task_creator = "CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, word TEXT, lenght TEXT)"
        cur.execute(task_creator)
        print('LETTER:{} - OK'.format(letter))

conn.close()

#query_create = "CREATE TABLE IF NOT EXISTS vacancys (id INTEGER PRIMARY KEY, title TEXT, company TEXT, salary INT)"
#cur.execute(query_create)

