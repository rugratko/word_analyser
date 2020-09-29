import freq
from db_requests import db_search_name


def search_by_name(err_word, fixed_list):
    if db_search_name(freq.normalize_word(err_word)):
        return err_word
    else:
        for word in fixed_list:
            if db_search_name(freq.normalize_word(word)):
                return word
    return 0