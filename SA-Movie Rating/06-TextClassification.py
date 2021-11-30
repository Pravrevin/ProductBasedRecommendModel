import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import string
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy import displacy, tokenizer
from spacy.lang.en.stop_words import STOP_WORDS
from sklearn.svm import LinearSVC

nlp = spacy.load('en_core_web_sm')

df = pd.read_csv('amazon_alexa.tsv',sep='\t')
#print(df.head)
df2 = df.drop(['rating','date','variation'],axis=1)


column_name = ['Review','Sentiment']
df2.columns=column_name
print(df2.head())
print(df2.shape)
print(df2['Sentiment'].value_counts())
print(df2.isnull().sum())

#Tokenization
punct = string.punctuation
print('punct=',punct)
stopwords= list(STOP_WORDS)
print(stopwords)
def text_data_cleaning(sentence):
    doc = nlp(sentence)
    tokens=[]
    for token in doc:
        if token.lemma_ !="-PRON-":
            temp = token.lemma_.lower().strip()
        else:
            temp = token.lower_
        tokens.append(temp)
    cleaned_tokens= []
    for token in tokens:
        if token not in stopwords and token not in punct:
            cleaned_tokens.append(token)
    return cleaned_tokens

# res = text_data_cleaning("   Hello how are you . Like this tutorial")
# print(res)

#Vectorization Feature Enginnering (TF-IDF)
tfidf = TfidfVectorizer(tokenizer = text_data_cleaning)
classifier = LinearSVC()

x = df2['Review']
y = df2['Sentiment']

X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

#pipeline
print(X_train.shape)
print(X_test.shape)

clf = Pipeline([('tfidf',tfidf),('clf',classifier)])
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print(classification_report(y_test,y_pred))

#print(confusion_matrix(y_test,y_pred))

print(clf.predict(['Aman you are good person bad cooking poor']))
#print(clf.predict(['wow, this is amazing product']))
#print(clf.predict(['wow, this is amazing product']))
