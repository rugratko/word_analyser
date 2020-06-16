import os
from models import algo
from models import word_def as wd
from operator import attrgetter

print('Loading freq table...')
freq = open(os.getcwd() + '/models/data/freq_list.txt', encoding='utf-8')
freq_table = []
for line in freq:
    freq_table.append(line.split())
print('Freq table loaded')

def get_freq(word_list, err_word):
    ans_list = []
    for word in word_list:
        word_a = algo.normalize_word(word)
        word_b = wd.Word(word, err_word)
        #print('Word {} = {}'.format(word_b.word, word_a))
        for element in range(len(freq_table)):
            if wd.destroy_yo(word_a) == freq_table[element][0]:
                word_b.rarity = float(freq_table[element][2])
                #print('Found! The word is {}, converted to {}, rarity = {}.'.format(word_b.word, word_a, word_b.rarity))
                ans_list.append(word_b)
                break
    
    buff_list = sorted(ans_list, key=attrgetter('rarity'), reverse = True)
    ans_list = sorted(buff_list, key=attrgetter('leven'))
    result = []
    for i in ans_list:
        print('List for {}: fixed word = {}, leven dist = {}, rarity = {};'.format(i.err_word, i.word, i.leven, i.rarity))
        result.append(i.word)

    return result


