from util import *

# Add your import statements here
import re
import nltk
nltk.download('punkt')


class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = None
		
		#Fill in code here
		segmentedText = re.split(r'[.!?]+',text)

		if len(segmentedText[-1])==0: #to remove the extra ending spaces to be counted as a separate sentence.
			segmentedText = segmentedText[:-1]

		return segmentedText





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = None

		#Fill in code here
		segmentedText = nltk.sent_tokenize(text)

		return segmentedText