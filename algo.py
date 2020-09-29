import re
import enchant
import pymorphy2
import freq
import names
from datetime import datetime
from enchant.checker import SpellChecker

def spell_checker(text, dict_language = 'ru_RU', answer_type = 'cutted'):
    word_checker = enchant.Dict(dict_language)
    text_checker = SpellChecker('ru_RU')
    text_proc = text.split()        
    start_time = datetime.now()
    for position in range(len(text_proc) - 1):
        text_checker.set_text(text_proc[position])
        for err in text_checker:
            if len(err.word) > 1:
                fixed = word_checker.suggest(err.word)
                print ('ERROR:', err.word, 'replaced by:', fixed)
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
    print('CHECK TIME', datetime.now() - start_time)

    answer = ' '.join(text_proc)
    return answer





