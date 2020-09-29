import os
import json

def load_freq_data():
    print('Loading freq data...')
    freq = open(os.getcwd() + '/data/freq_list.txt', encoding='utf-8')
    freq_table = []
    for line in freq:
        freq_table.append(line.split())
    print('Freq data loaded')
    return freq_table

def load_name_data():
    united_names = []
    print ('Loading name/surname data...')
    with open(os.getcwd() + '/data/russian_names.json', encoding='utf-8-sig') as word_list:
        names = json.load(word_list)
    with open(os.getcwd() + '/data/russian_surnames.json', encoding='utf-8-sig') as word_list:
        surnames = json.load(word_list)
    for element in names:
        if int(element['PeoplesCount']) >= 10000:
            united_names.append(element['Name'].lower())
    for element in surnames:
        if int(element['PeoplesCount']) >= 5000:
            united_names.append(element['Surname'].lower())
    print ('Name/surname data are ready')
    return tuple(united_names)
