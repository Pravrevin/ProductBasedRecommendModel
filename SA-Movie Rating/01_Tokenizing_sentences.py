'''
Tokenization is the process of breaking down chunks of text into smaller pieces. spaCy comes with a default processing pipeline that begins with tokenization, making this process a snap. In spaCy, you can do either sentence tokenization or word tokenization:

Word tokenization breaks text down into individual words.
Sentence tokenization breaks text down into individual sentences.
'''

import spacy
from spacy.lang.en import English
def word_token(model,text):

    nlp = spacy.load(model) #spaCy’s English model
    doc = nlp(text) #nlp constructor
    token_list = [token for token in doc]
    print(token_list)

text = """
Dave watched as the forest burned up on the hill,
only a few miles from his house. The car had
been hastily packed and Marta was inside trying to round
up the last of the pets. "Where could she be?" he wondered
as he continued to wait for Marta to appear with the pets.
"""

if __name__== '__main__':
    word_token("en_core_web_sm",text)
    #sent_token("en_core_web_sm",text)