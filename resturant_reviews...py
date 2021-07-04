# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 10:55:51 2021

@author: Aatif
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import re
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
from nltk.corpus import stopwords
stoplist = stopwords.words('english')
import  sklearn 


df=pd.read_csv(r"C:\Users\Aatif\Downloads\Restaurant_Reviews (1).tsv" ,  delimiter = '\t')

clean_reviews=[]




# Data Preprocessing----

for i in range(0,1000):
    review= re.sub("[^a-zA-z]", ' ', df['Review'][i])
    review= review.lower()
    review=review.split()
    ps=PorterStemmer()
    review=[ps.stem(word) for word in review if word not in set(stoplist) ]
    review=' '.join(review)
    clean_reviews.append(review)
    
    
# creating the Bag of Words---
    
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=1000)
X=cv.fit_transform(clean_reviews).toarray()
y=df['Liked'].values



# Seprate the  data using train_test_split---

from sklearn.model_selection  import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=0)





# Fitting Random Forest Classificationto the Training set

from sklearn.ensemble import RandomForestClassifier
RF = RandomForestClassifier(n_estimators = 501,
                            criterion = 'entropy')
                             
RF.fit(X_train, y_train)
RF.score(X_train, y_train)            
RF.score(X_test, y_test)


y_pred = RF.predict(X_test)
y_pred



from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(X,y)
knn.score(X_train, y_train)
knn.score(X_test, y_test)


from sklearn.naive_bayes import GaussianNB
nb=GaussianNB()
nb.fit(X_train, y_train)
nb.score(X_train, y_train)
nb.score(X_test, y_test)






