from sklearn.tree import DecisionTreeRegressor

from sklearn.tree import export_graphviz
import numpy as np

from graphviz import Source

np.random.seed(42)
X_quad = np.random.rand(200, 1) - 0.5  # a single random input feature
y_quad = X_quad ** 2 + 0.025 * np.random.randn(200, 1)

tree_reg = DecisionTreeRegressor(max_depth=2, random_state=42)
tree_reg.fit(X_quad, y_quad)

DecisionTreeRegressor(max_depth=2, random_state=42)

# save image as dot file
image_path = "dot/regression_tree.dot"
export_graphviz(
    tree_reg,
    out_file=image_path,
    feature_names=["x1"],
    rounded=True,
    filled=True
)
tree = Source.from_file(image_path)

tree.render(view=True)