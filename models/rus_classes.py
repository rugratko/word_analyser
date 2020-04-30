import sqlite3

class Letter:
    def __init__(self, LETTER):
        self.letter = LETTER
        self.let_id = ord(self.letter)

    def add_to_db(self, database, mass_commit, cur = None):
        if mass_commit == False:
            conn = sqlite3.connect(database)
            cur = conn.cursor()

        task = "INSERT INTO alphabet VALUES(NULL, ?,?)"
        cur.execute(task, (self.let_id, self.letter))
        if mass_commit == False:
            conn.commit()
            conn.close()


class Word:
    def __init__(self, WORD):
        self.word = WORD
        self.len = len(WORD)

    def add_to_db(self, database, mass_commit, cur = None):
        if mass_commit == False:
            conn = sqlite3.connect(database)
            cur = conn.cursor()

        task = "INSERT INTO dictionary VALUES(NULL, ?,?)"
        cur.execute(task, (self.word, self.len))
        if mass_commit == False:
            conn.commit()
            conn.close()


def fill_db(list, database, obj_type = 'word', mass_commit = False):
    if mass_commit:
        conn = sqlite3.connect(database)
        cur = conn.cursor()

    if obj_type == 'word':
        for item in list:
            buffer = Word(item)
            buffer.add_to_db(database, mass_commit, cur)
    elif obj_type == 'letter':
        for item in list:
            buffer = Letter(item)
            buffer.add_to_db(database, mass_commit, cur)
    else:
        print('Wrong object type!')
        return(None)

    if mass_commit:
        conn.commit()
        conn.close()
   

