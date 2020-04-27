import sqlite3

class Letter:
    def __init__(self, id, LETTER):
        self.id = id
        self.letter = LETTER
        self.let_id = ord(self.letter)

    def add_to_db(self, database):
        conn = sqlite3.connect(database)
        cur = conn.cursor()

        task = "INSERT INTO rus_alphabet VALUES(NULL, ?,?)"
        cur.execute(task, (self.let_id, self.letter))

        conn.commit()
        conn.close()
    
def fill_db(alphabet, database):
    print('Filling alphabet table...')
    id = 1
    for letter in alphabet:
        buffer = Letter(id, letter)
        buffer.add_to_db(database)
        id += 1
