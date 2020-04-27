from models.alphabet import Letter, fill_db
import models.word as word

print('Application is working')

alphabet = 'а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я'.split(', ')
database = 'russian.db'

fill_db(alphabet, database)



