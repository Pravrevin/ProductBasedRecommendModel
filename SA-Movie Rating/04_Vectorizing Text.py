'''
each token in way that a machine can understand. This is called vectorization.
'''
import spacy
def word_token(model,text):

    nlp = spacy.load(model) #spaCy’s English model
    doc = nlp(text) #nlp constructor
    token_list = [token for token in doc]
    print('Actual Token List is = ',token_list)
    filtered_tokens = [token for token in doc if not token.is_stop]
    print('After Removing Stop words=',filtered_tokens)
    print(filtered_tokens[1].vector) #Dave


text = """
Dave watched as the forest burned up on the hill,
only a few miles from his house. The car had
been hastily packed and Marta was inside trying to round
up the last of the pets. "Where could she be?" he wondered
as he continued to wait for Marta to appear with the pets.
"""

if __name__== '__main__':
    word_token("en_core_web_sm",text)
