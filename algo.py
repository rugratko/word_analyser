import re
import enchant
from enchant.checker import SpellChecker

def spell_checker(text, dict_language = 'ru_RU', database = 'russian.txt', answer_type = 'cutted'):
    word_checker = enchant.DictWithPWL(dict_language, database)
    text_checker = SpellChecker('ru_RU')
    text_proc = text.split()
    for position in range(len(text_proc) - 1):
        text_checker.set_text(text_proc[position])
        for err in text_checker:
            if len(err.word) > 2:
                fixed = word_checker.suggest(err.word)
                print ('ERROR:', err.word, ', replaced by:', fixed)
                if len(fixed) != 0:
                    if answer_type == 'cutted':
                        text_proc[position] = re.sub(r'\b{}\b'.format(re.escape(err.word)), fixed[0], text_proc[position])           
                    if answer_type == 'full':
                        text_proc[position] = re.sub(r'\b{}\b'.format(re.escape(err.word)), str(fixed), text_proc[position])  

    answer = ' '.join(text_proc)
    return answer





