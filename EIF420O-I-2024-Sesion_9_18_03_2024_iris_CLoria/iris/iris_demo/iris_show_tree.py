import matplotlib.pyplot as plt
from sklearn import tree



def show_tree(iris_df, iris_tree, class_names, 
              iris_cm_display):
    fig = plt.figure(figsize = (10,10))
    _ = tree.plot_tree(iris_tree, 
                       feature_names = iris_df.columns.tolist(),  
                       class_names = [c for c in class_names],
                       filled=True)
    iris_cm_display.plot()
    plt.show()