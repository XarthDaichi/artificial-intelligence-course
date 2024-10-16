from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

iris = load_iris(as_frame=True)
X_iris = iris.data[["petal length (cm)", "petal width (cm)"]].values
y_iris = iris.target

hyperparameters = {
                   "max_depth":2, 
                   "random_state":42
                  }

tree_clf = DecisionTreeClassifier(**hyperparameters)
tree_clf.fit(X_iris, y_iris)


iris_tree_path = "./dot/fig_6_1_iris_tree.dot"
export_graphviz(
        tree_clf,
        out_file=iris_tree_path,
        feature_names=["petal length (cm)", "petal width (cm)"],
        class_names=iris.target_names,
        rounded=True,
        filled=True
    )
print(f"*** Dot file saved in {iris_tree_path} ***")

tree = Source.from_file(image_path)

tree.render(view=True)
# Use to generate tree in anaconda cmd: 
# dot -Tpng dot\fig_6_1_iris_tree.dot -o fig_6_1_Iris_tree.png