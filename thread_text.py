import threading, queue
import re
import enchant
import pymorphy2
import freq
import names
import os
from datetime import datetime
from enchant.checker import SpellChecker

def spellch(answer_type = 'cutted'):
    while True:
        text = q.get()
        text_proc = text.split()        
        print(text)
        for position in range(len(text_proc) - 1):
            #print(text_proc[position])
            text_checker.set_text(text_proc[position])
            for err in text_checker:
                if len(err.word) > 1:
                    fixed = word_checker.suggest(err.word)
                    #print ('ERROR:', err.word, 'replaced by:', fixed)
                    if err.word[0].isupper():
                        result = names.search_by_name(err.word, fixed)
                        if result == 0:
                            fixed = freq.get_freq(fixed, err.word)   
                        else:
                            fixed[0] = result 
                    else:
                        fixed = freq.get_freq(fixed, err.word)

                    if len(fixed) != 0:
                        if answer_type == 'cutted':
                            text_proc[position] = re.sub(r'\b{}\b'.format(re.escape(err.word)), fixed[0], text_proc[position])           
                        if answer_type == 'full':
                            text_proc[position] = re.sub(r'\b{}\b'.format(re.escape(err.word)), str(fixed), text_proc[position])  

        answer = ' '.join(text_proc)
        q.task_done()
       
def wordch(answer_type = 'cutted'):   
    while True:
        word = q.get()  
        fixed = word_checker.suggest(word)
        print ('ERROR:', word, 'replaced by:', fixed)
        if word[0].isupper():
            result = names.search_by_name(word, fixed)
            if result == 0:
                fixed = freq.get_freq(fixed, word)   
            else:
                fixed[0] = result 
        else:
            fixed = freq.get_freq(fixed, word)
        q.task_done()
 

q = queue.Queue()
word_checker = enchant.Dict('ru_RU')
text_checker = SpellChecker('ru_RU')

start_time = datetime.now()      

threading.Thread(target=spellch, daemon=True).start()

exam = open(os.getcwd() + '/data/exam.txt', encoding='utf-8')
my_text = exam.read()
exam.close()

text_checker.set_text(my_text)
for err in text_checker:
    if len(err.word) > 1:
        q.put(err.word)
        
print('CHECK TIME 1', datetime.now() - start_time)

print('All task requests sent\n', end='')

q.join()

print('CHECK TIME 2', datetime.now() - start_time)
print('All work completed')






