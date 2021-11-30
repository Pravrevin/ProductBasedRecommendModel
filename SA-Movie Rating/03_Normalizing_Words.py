'''
It entails condensing all forms of a word into a single representation of that word. For instance, “watched,” “watching,” and “watches” can all be normalized into “watch.” There are two major normalization methods:

Stemming :word is cut off at its stem
Lemmatization :uses a data structure that relates all forms of a word back to its simplest form, or lemma
'''

import spacy
def word_token(model,text):

    nlp = spacy.load(model) #spaCy’s English model
    doc = nlp(text) #nlp constructor
    token_list = [token for token in doc]
    print('Actual Token List is = ',token_list)
    filtered_tokens = [token for token in doc if not token.is_stop]
    print('After Removing Stop words=',filtered_tokens)
    lemmas = [f"Token: {token}, lemma: {token.lemma_}" for token in filtered_tokens]
    print('After Normalizing Words=',lemmas)

text = """
Dave watched as the forest burned up on the hill,
only a few miles from his house. The car had
been hastily packed and Marta was inside trying to round
up the last of the pets. "Where could she be?" he wondered
as he continued to wait for Marta to appear with the pets.
"""

if __name__== '__main__':
    word_token("en_core_web_sm",text)
