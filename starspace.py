

'''
Please run the code with CUDA_AVAILABLE_DEVICES set to 0 in env.
'''
from sklearn import svm
from sklearn import preprocessing
import pandas
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import time
from sklearn.model_selection import GridSearchCV

from sklearn.model_selection import train_test_split

dataset = np.load('star_space_embeddings.npy') # Use this if the ds is already saved


data = dataset[:,:-1]
labels = dataset[:,-1]

def acc(clf,X_train_scaled,X_test_scaled,y_train,y_test):
    start = time.time()
    training_results = clf.predict(X_train_scaled)
    #print('Training accuracy', accuracy_score(df_train,df_train_label, normalize=True)) #Normalize = false for number of correctly classified
    print('Training accuracy', accuracy_score(training_results,y_train, normalize=True))
    results = clf.predict(X_test_scaled)
    print('Testing accuracy', accuracy_score(results, y_test, normalize=True))
    end = time.time()
    print(end-start)

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.1, random_state=42)
X_train_scaled = preprocessing.scale(X_train)
X_test_scaled = preprocessing.scale(X_test)
para = {'C': [50,20,10,5,1,0.1,0.01] , 'gamma':[5,0.5,0.05,0.005,0.0001,0.0005,0.00005] }
svc = svm.SVC(verbose = True)
clf = GridSearchCV(svc, para)
clf.fit(X_train_scaled, y_train).score(X_test, y_test)
import IPython  #Comment out for no interactivity
IPython.embed()

## The above Grid Search takes over 1 day to run intotal and the best accuracy score is 62.1% for binary helpful not helpful classification.

'''
clf = svm.SVC(gamma = 0.0005,C = 5, verbose = True) 
start = time.time()
clf.fit(X_train_scaled, y_train)
end = time.time()
print(end-start)
acc(clf,X_train_scaled,X_test_scaled,y_train,y_test)
'''