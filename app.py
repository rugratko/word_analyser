from models import rus_classes as rc
import re

from datetime import datetime
import time

start_time = datetime.now()
print('Application is working')

alphabet = 'а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я'.split(', ')
database = 'russian.db'

f = open('russian.txt', 'r')
my_list  = []
id = 0
for line in f.readlines():
    #if id == 5000:
        #break
    my_list.append(re.sub('^\s+|\n|\r|\s+$', '', line))
    #id += 1
f.close()

rc.fill_db(my_list, database, mass_commit=True)



#print(my_list)
print(datetime.now() - start_time)