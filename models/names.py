import json
import os
from models import algo

united_names = []

def load_name_tables():
    print ('Loading name/surname tables...')
    with open(os.getcwd() + '/models/data/russian_names.json', encoding='utf-8-sig') as fh:
        names = json.load(fh)
    with open(os.getcwd() + '/models/data/russian_surnames.json', encoding='utf-8-sig') as fh:
        surnames = json.load(fh)
    for element in names:
        united_names.append(element['Name'].lower())
    for element in surnames:
        united_names.append(element['Surname'].lower())
    print ('Name/surname table are ready')

def search_by_name(err_word, fixed_list):
    if algo.normalize_word(err_word) in united_names:
        return err_word
    else:
        for word in fixed_list:
            if algo.normalize_word(word) in united_names:
                return word
    return 0

load_name_tables()
