import time
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn import pipeline 
from sklearn import metrics
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.preprocessing import StandardScaler, LabelEncoder


def 
    le = LabelEncoder()

    train_data.target = le.fit_transform(train_data.target)
    train_data.user = le.fit_transform(train_data.user)

    test_data.target = le.fit_transform(test_data.target)
    test_data.user = le.fit_transform(test_data.user)

    train_data