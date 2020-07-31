import os
import json

def load_name_data():
    united_names = []
    print ('Loading name/surname data...')
    with open(os.getcwd() + '/data/russian_names.json', encoding='utf-8-sig') as word_list:
        names = json.load(word_list)
    with open(os.getcwd() + '/data/russian_surnames.json', encoding='utf-8-sig') as word_list:
        surnames = json.load(word_list)
    for element in names:
        if int(element['PeoplesCount']) < 10000:
            united_names.append(element['Name'].lower())
    for element in surnames:
        if int(element['PeoplesCount']) < 5000:
            united_names.append(element['Surname'].lower())
    print ('Name/surname data are ready')
    return tuple(united_names)


if __name__ == '__main__':
    f = open('namesList.txt', 'w')
    names = load_name_data()
    for element in names:
        f.write(element + '\n')
    f.close()