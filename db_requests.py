import sqlite3

def db_search_name(word):
    conn = sqlite3.connect("db\word_data.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""SELECT * FROM namesList WHERE word=?""", (word, ))
        result = cursor.fetchall()
        if result[0]:
            return result[0][1]
        else:
            return 0
    except:
        return 0
    conn.commit()
    conn.close()
    

def db_get_words_by_firstLetter(word):
    conn = sqlite3.connect("db\word_data.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""SELECT * FROM freqList WHERE first_letter=?""", (word[0], ))
        result = cursor.fetchall()
        if result:
            return result
        else:
            return 0
    except:
        return 0
    conn.commit()
    conn.close()
