'''
Data Cleaning options
1- Case Normalization
2- Removing Stop Words
3- Removing punctuations & special symbols
4- Lemma or Stemming
5- Parts of speech Tagging
6- Entity Detection (person,organisation etc)
7- Bag of Words
8- TF-IDF
'''
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy import displacy
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load('en_core_web_sm')

# stopwords= list(STOP_WORDS)
# print(stopwords)

# for token in doc:
#     if token.is_stop ==False:
#         print(token)

# #lemma
# doc = nlp('run runs running runner')
# for lem in doc:
#     print(lem.text,lem.lemma_)

# #POS - part of speech
# doc = nlp('All is well at your end!')
# for token in doc:
#     print(token.text,'-',token.pos_)
# displacy.render(doc,style='dep')

# #Entity Detection
# text = """
# Dave watched as the forest burned up on the hill,
# only a few miles from his house. The car had
# been hastily packed and Marta was inside trying to round
# up the last of the pets. "Where could she be?" he wondered
# as he continued to wait for Marta to appear with the pets.
# """
# doc = nlp(text)
# print(displacy.render(doc,style='ent'))