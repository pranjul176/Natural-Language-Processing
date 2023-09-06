# Add your import statements here
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

punctuation_tokens_to_be_removed = ['!',",",".","..","'",";",":","]","[","(",")","\\","/"]
stopword_list=stopwords.words("english")
stemmer = PorterStemmer()

# Add any utility functions here