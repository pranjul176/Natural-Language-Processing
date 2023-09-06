from util import *

# Add your import statements here
from nltk.tokenize import TreebankWordTokenizer
import re


class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		# tokenizedText = None
		tokenizedText =[]
		#Fill in code here
		for sentence in text:
			tokenizedSent = re.findall(r'\b\w+\b',sentence)
			tokenizedSent_withoutPunct = []
			for token in tokenizedSent:
				if token not in punctuation_tokens_to_be_removed:
					tokenizedSent_withoutPunct.append(token)
			
			tokenizedText.append(tokenizedSent_withoutPunct)
		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		# tokenizedText = None

		#Fill in code here
		tokenizedText =[]

		for sentence in text:
			tokenizedSent = TreebankWordTokenizer().tokenize(sentence)
			tokenizedSent_withoutPunct = []
			
			for token in tokenizedSent:
				if token not in punctuation_tokens_to_be_removed:
					tokenizedSent_withoutPunct.append(token)
			
			tokenizedText.append(tokenizedSent_withoutPunct)
		return tokenizedText