class Word():
    def __init__(self, word, err_word, rarity = 0):
        self.word = word
        self.err_word = err_word
        self.leven = self.define_leven()
        self.rarity = rarity
    
    def define_leven(self):
        a = self.word
        b = self.err_word
        n, m = len(a), len(b)
        if n > m:
            a, b = b, a
            n, m = m, n
        current_row = range(n + 1) 
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
                if a[j - 1] != b[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)
        return current_row[n]

def destroy_yo(word):
    result = word.replace('ё', 'е')
    return result