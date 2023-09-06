from util import *

# Add your import statements here




class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = []
		#Fill in code here
		for sent_tok_list in text:
			tok_list_without_stopwords = []
			for token in sent_tok_list:
				if token not in stopword_list:
					tok_list_without_stopwords.append(token)

			stopwordRemovedText.append(tok_list_without_stopwords)
		

		return stopwordRemovedText




	