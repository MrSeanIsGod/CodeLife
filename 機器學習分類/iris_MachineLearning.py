import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm

def train_evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    #print("Ground Truth:", y_test[0:10])
    #print("Prediction:", predictions[0:10])
    #print()
    #print("Classification Report:")
    #print(classification_report(y_test, predictions))
    #print("Confusion Matrix:")
    #print(confusion_matrix(y_test, predictions))
    accuracy = accuracy_score(y_test, predictions)
    return accuracy
    
#資料處理
df=pd.read_csv('iris.csv')

filtered_df = df[df['variety'].isin(['Setosa', 'Versicolor'])]
#print(filtered_df.head())
#print(filtered_df.describe())
#print(filtered_df.info())

X= df.drop(columns=['variety'])
#print(X.head())
y = df["variety"].values
#print(y[0:5])

X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)


#KNN
print("K Nearest Neighbors")
knn = KNeighborsClassifier(n_neighbors=3)
knn_accuracy = train_evaluate_model(knn, X_train, X_test, y_train, y_test)
print("KNN_Accuracy=", knn_accuracy)
print()

#LogisticRegression
print("Logistic Regression")
lr_model = LogisticRegression()
lr_accuracy = train_evaluate_model(lr_model, X_train, X_test, y_train, y_test)
print("LogisticRegression_Accuracy=", lr_accuracy)
print()

#DecisionTree
print("Decision Tree")
dt_model = tree.DecisionTreeClassifier(criterion="entropy")
dt_accuracy = train_evaluate_model(dt_model, X_train, X_test, y_train, y_test)
print("DecisionTree_Accuracy = ", dt_accuracy)
print()

#RandomForest
print("Random Forest")
rf_model = RandomForestClassifier(n_estimators=100, random_state=0)
rf_accuracy = train_evaluate_model(rf_model, X_train, X_test, y_train, y_test)
print("RandomForest_Accuracy = ", rf_accuracy)
print()

#SVM
print("SVM")
svm_model = svm.SVC(kernel='linear', C=1.0)
svm_accuracy = train_evaluate_model(svm_model, X_train, X_test, y_train, y_test)
print("SVM_Accuracy = ", svm_accuracy)
