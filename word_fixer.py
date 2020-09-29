import re
import os
import word_finder
import freq
import names
import threading, queue
from datetime import datetime
from enchant.checker import SpellChecker

def correct_word():
    while True:
        word = q.get()
        fixed = word_finder.candidates(word)
        if err.word[0].isupper():
            result = names.search_by_name(word, fixed)
            if result == 0:
                fixed = freq.get_freq(fixed, word)   
            else:
                try:
                    fixed[0] = result 
                except:
                    fixed = result
        else:
            fixed = freq.get_freq(fixed, err.word)
        fixed = freq.get_freq(fixed, word)
        print('{} = {}'.format(word, fixed))
        q.task_done()

q = queue.Queue(3)
text_checker = SpellChecker('ru_RU')
   
threading.Thread(target=correct_word, daemon=True).start()
start_time = datetime.now()      

my_text = ''
with open(os.getcwd() + '/exam_short.txt', encoding='utf-8') as exam:
    my_text = exam.read()

text_checker.set_text(my_text)
for err in text_checker:
    if len(err.word) > 2:
        q.put(err.word)
        
q.join()
        
print('COMPLETED IN', datetime.now() - start_time)