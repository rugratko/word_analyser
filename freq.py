import os
import algo
import word_def as wd
from datetime import datetime
from operator import attrgetter
from db_requests import db_get_words_by_firstLetter

def get_freq(word_list, err_word):
    ans_list = []
    #start_time = datetime.now()
    for word in word_list:
        word_a = algo.normalize_word(word)
        word_b = wd.Word(word, err_word)
        #print('Word {} = {}'.format(word_b.word, word_a))
        word_to_search = wd.destroy_yo(word_a)
        freq_table = db_get_words_by_firstLetter(word_to_search)
        if freq_table:
            for element in range(len(freq_table)):
                #print('word_to_search == freq_table[element][0]', word_to_search, freq_table[element][2])
                if word_to_search == freq_table[element][2]:
                    word_b.rarity = float(freq_table[element][3])
                    #print('Found! The word is {}, converted to {}, rarity = {}.'.format(word_b.word, word_a, word_b.rarity))
                    ans_list.append(word_b)
                    break
        else:
            print('Error in freq!')
    #print('FREQ TIME', datetime.now() - start_time)
    
    buff_list = sorted(ans_list, key=attrgetter('rarity'), reverse = True)
    ans_list = sorted(buff_list, key=attrgetter('leven'))
    result = []
    for i in ans_list:
        #print('List for {}: fixed word = {}, leven dist = {}, rarity = {};'.format(i.err_word, i.word, i.leven, i.rarity))
        result.append(i.word)

    return result


