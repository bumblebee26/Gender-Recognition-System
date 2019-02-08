#Logistic Regression

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

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.02, random_state=None, shuffle=True)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#Fitting logistic regression to the training set
from sklearn.linear_model import LogisticRegression 
classifier = LogisticRegression(penalty='l2',random_state=None, max_iter=10000, solver='lbfgs',class_weight='balanced')
classifier.fit(X_train, y_train)

#Prediciting the test set results
y_pred = classifier.predict(X_test)

#Making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

correct_pred=sum(y_pred == y_test)
print(correct_pred)
print('accuracy = ', correct_pred*100/(y_pred.shape[0]))
