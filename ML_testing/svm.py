# Kernel SVM

# Importing the libraries
import numpy as np
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('C:\\Users\\Atulya\\Documents\\GitHub\\gender-classifier-using-voice\\Data Preprocessing\\feature extraction\\features.csv')
X = dataset.iloc[:,1:-1].values             
y = dataset.iloc[:,-1:].values

#Taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=0, strategy='mean')
imputer = imputer.fit(X[:,:])
X[:,:] = imputer.transform(X[:,:])

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y.ravel())

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.0125, random_state = None,shuffle=True)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# -----------------------------------SVM Grid Search -------------------------------------------------#
#best_score = 0  
#best_params = {'C': None, 'gamma': None}
#
#C_values = [0.01, 0.03, 0.1, 0.3, 1,3, 10, 30, 100] 
#gamma_values = [0.01, 3, 10, 30, 100, 0.03, 0.1, 0.3, 1] 
#
#for C in C_values:  
#    for gamma in gamma_values:
#        print(C,gamma)
#        svc = svm.SVC(C=C, gamma=gamma,kernel = 'rbf', random_state = 1,max_iter=1000000,class_weight='balanced')
#        svc.fit(X_train, y_train)
#        score = svc.score(X_test, y_test)
#        print(score*100)
#
#        if score > best_score:
#            best_score = score
#            best_params['C'] = C
#            best_params['gamma'] = gamma
#
#print(best_score, best_params)
#-----------------------------------------------------------------------------------------------------

# Fitting Kernel SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(C=3,gamma=0.02,kernel = 'rbf', random_state =None,max_iter=100000)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# And find the final test error
correct_pred=sum(y_pred == y_test)
print(correct_pred, ' classified correctly out of ',np.shape(y_test)[0])
#print('accuracy = ', correct_pred*100/(y_pred.shape[0]))


test_score=classifier.score(X_test,y_test)
print('Train set accuracy = ',classifier.score(X_train,y_train)*100)
print('Test set accuracy = ',test_score*100)


##---------------------------------Testing on recorded audio ---------------------------#
#
#recorded_dataset = pd.read_csv('C:\\Users\\Atulya\\Documents\\GitHub\\gender-classifier-using-voice\\feature extraction\\recorded_audio_features.csv')
#X_recorded = recorded_dataset.iloc[:,1:-2].values          
#y_recorded = recorded_dataset.iloc[:,-2:-1].values
#
##Taking care of missing data
#from sklearn.impute import SimpleImputer
#imputer = SimpleImputer(missing_values=0, strategy='most_frequent')
#imputer = imputer.fit(X_recorded[:,:])
#X_recorded[:,:] = imputer.transform(X_recorded[:,:])
#
## Encoding categorical data
#from sklearn.preprocessing import LabelEncoder
#labelencoder_y = LabelEncoder()
#y_recorded_test = labelencoder_y.fit_transform(y_recorded.ravel())
#
## Feature Scaling
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#X_recorded_test = sc.fit_transform(X_recorded)
#
## Predicting the Test set results
#y_recorded_pred = classifier.predict(X_recorded_test)
#
## And find the final test error
#correct_pred=sum(y_recorded_pred == y_recorded_test)
#print(correct_pred, ' classified correctly out of ',np.shape(y_recorded_test)[0],' recorded files')

#--------------------------------------Save Trained Model --------------------------------#

import pickle

# save the model to disk
filename = 'finalised_model.sav'
pickle.dump(classifier, open(filename, 'wb'))
 
# some time later...
 
# load the model from disk
loaded_classifier = pickle.load(open(filename, 'rb'))
result = loaded_classifier.score(X_test, y_test)
print(result)