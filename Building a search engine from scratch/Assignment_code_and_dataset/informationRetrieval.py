from util import *
from collections import Counter
import math
import numpy as np
from numpy.linalg import norm

class InformationRetrieval():

	def __init__(self):
		self.index = None
		self.docIDs = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable
		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""
		assert len(docs)==len(docIDs)
		index = {}

		#Fill in code here
		for i,doc in enumerate(docs):
			docID = docIDs[i]
			terms_in_doc=list(flatten(doc))
			uniq_terms,term_counts=np.unique(np.array(terms_in_doc), return_counts=True)
			for term,term_count in zip(uniq_terms,term_counts):
				
				try:
					index[term].append([docID, term_count])
				except:
					index[term] = [[docID,term_count]]

		self.index = index
		self.docIDs = docIDs

	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []

		#Fill in code here
		index = self.index
		docIDs = self.docIDs

		idf={}

		Total_num_docs = len(docIDs)
		for term in index:
			num_of_doc_containing_term = len(index[term])
			idf[term] = np.log10(float(Total_num_docs/num_of_doc_containing_term))

		# Representing documents in tf-idf vector space
		docvectors = {}
		docnorms = {}
		for docID in docIDs:
			docvectors[docID] = dict.fromkeys(index.keys(),0) # Initializing all docvectors with nullvector
			
		for term in index:
			for docID, tf in index[term]:
				docvectors[docID][term] = tf * idf[term]
                
		for docID in docIDs:
			docnorms[docID] = norm(np.array(list(docvectors[docID].values())))

		for query in queries:
			queryvector = dict.fromkeys(index.keys(),0)
			terms = list(flatten(query)) # Flattening 2d list to 1d
			for term, tf in list(Counter(terms).items()):
				try:
					queryvector[term] = tf * idf[term]
				except:
					pass
			querynorm = norm(np.array(list(queryvector.values())))
			cosine_similarities = {}


			for docID in docIDs:
				try:
					numerator = sum(docvectors[docID][key] * queryvector[key] for key in index) 
					if numerator !=0:
						cosine_similarities[docID] =numerator / (querynorm*docnorms[docID])
					else:
						cosine_similarities[docID] = 0
				except:
					cosine_similarities[docID] = 0
			doc_IDs_ordered.append([docID for docID, tf in sorted(cosine_similarities.items(), key=lambda item: item[1], reverse = True)])

		return doc_IDs_ordered

