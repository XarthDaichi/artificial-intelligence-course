import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)


print(f"*** Iris data set read. Shape: {df.shape} ****")


df['target'] = iris.target

X_train, X_test, y_train, y_test = train_test_split(df[iris.feature_names], df['target'], random_state=0)

clf = DecisionTreeClassifier(random_state=0, criterion='entropy')
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

fig = plt.figure(figsize=(15,10))
_ = tree.plot_tree(clf, 
                   feature_names=iris.feature_names,  
                   class_names=[n for n in iris.target_names],
                   filled=True)
plt.show()
                   
                   