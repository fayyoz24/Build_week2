import pandas as pd
import time
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler

def get_model():

  test_data1 = pd.read_csv("test_side1.csv")
  test_data2 = pd.read_csv("test_side2.csv")
  train_data = pd.read_csv("train_side.csv")

  test_data1.target = test_data1.target.replace({'Car':0, 'Train':1, 'Bus':2, 'Still':3, 'Walking':4})
  test_data2.target = test_data2.target.replace({'Car':0, 'Train':1, 'Bus':2, 'Still':3, 'Walking':4})
  train_data.target = train_data.target.replace({'Car':0, 'Train':1, 'Bus':2, 'Still':3, 'Walking':4})


  x_train = train_data.drop(["target"], axis=1)
  y_train = train_data.target

  x_test1 = test_data1.drop(["target"], axis=1)
  y_test1 = test_data1.target

  x_test2 = test_data2.drop(["target"], axis=1)
  y_test2 = test_data2.target

  scaler = StandardScaler()
  x_train_scaled = scaler.fit_transform(x_train)


  tree_classifiers = {
  "GaussianNB": GaussianNB(),
  "Logistic Regression":   LogisticRegression(max_iter=2000),
  "Decision Tree Classifier": tree.DecisionTreeClassifier(random_state=1),
  "KNeighborsClassifier":      KNeighborsClassifier(),
  "Random Forest Classifier":       RandomForestClassifier(random_state=1),
  "XGBoost":       XGBClassifier(random_state = 1)
  }

  results = pd.DataFrame({'Model': [], 'Accuracy': [], 'Bal Acc.': [], 'Time': []})

  results = pd.DataFrame({'Model': [], 'Accuracy': [], 'Bal Acc.': [], 'Time': []})
  for model_name, model in tree_classifiers.items():

      start_time = time.time()
      model.fit(x_train_scaled, y_train)
      total_time = time.time() - start_time
          
      pred = model.predict(x_test1)
      
      results = results.append({"Model":    model_name,
                              "Accuracy": metrics.accuracy_score(y_test1, pred)*100,
                              "Bal Acc.": metrics.balanced_accuracy_score(y_test1, pred)*100,
                              "Time":     total_time},
                              ignore_index=True)

  return pd.read_csv('res.csv', index_col=False), round(pred.mean())



    # results_ord = results.sort_values(by=['Accuracy'], ascending=False, ignore_index=True)
    # results_ord.index += 1 
    # results_ord.style.bar(subset=['Accuracy', 'Bal Acc.'], vmin=0, vmax=100, color='#5fba7d')
print(get_model())