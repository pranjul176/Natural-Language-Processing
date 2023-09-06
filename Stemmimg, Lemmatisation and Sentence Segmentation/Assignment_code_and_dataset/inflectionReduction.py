from util import *

# Add your import statements here

class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""
		#Fill in code here

		reducedText = []
		for sent_tok_list in text:
			stemmed_tok_list=[]

			for token in sent_tok_list:
				stemmed_token = stemmer.stem(token)
				stemmed_tok_list.append(stemmed_token)

			reducedText.append(stemmed_tok_list)
		


		
		return reducedText


