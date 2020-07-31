import algo
import os
from datetime import datetime

start_time = datetime.now()
print('Application is working')

my_text = []
fixed_text_short = []
fixed_text_long = []

exam = open(os.getcwd() + '/data/exam.txt', encoding='utf-8')
answer_short = open(os.getcwd() + '/data/answer_short.txt', 'w')
answer_long = open(os.getcwd() + '/data/answer_long.txt', 'w')
my_text = exam.read().splitlines()

exam.close()

for line in my_text:
    if len(line) != 0:
        fixed_text_short.append(algo.spell_checker(line, answer_type = 'cutted'))
        #fixed_text_long.append(algo.spell_checker(line, answer_type = 'full'))

answer_short.writelines("%s\n" % line for line in fixed_text_short)
answer_long.writelines("%s\n" % line for line in fixed_text_long)

answer_short.close()
answer_long.close()

print(datetime.now() - start_time)