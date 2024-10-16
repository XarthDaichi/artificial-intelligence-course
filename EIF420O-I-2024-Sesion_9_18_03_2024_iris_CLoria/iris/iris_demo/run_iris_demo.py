from sklearn.metrics import accuracy_score

from iris_train_tree import train_tree
from iris_show_tree import show_tree
from iris_evaluate_tree import test_tree

import re

def main():

    tree, (df, class_names, X_test, y_test) = train_tree(random_state=666)

    metrics_dict = test_tree(tree, class_names, X_test, y_test)   

    show_tree(df, tree, class_names, metrics_dict["cm_plot"])
    
    return tree, class_names

def get_list(s):
    s = re.sub(r"[ \(\]]*", "", s)
    s = re.split(r"[, ]+", s)
    try:
        s = list((float(n) for n in s))
        assert(len(s) == 4)
    except:
        print(f'Ending with (bad) input {str(s)}')
        s = None
    return s
if __name__ == "__main__":
    tree, class_names = main()
    while True:
        x = get_list(input("Enter 4 numbers delimted  by comma?"))
        if not x: break
        probs = tree.predict_proba([x]).round(3)
        print( list(zip(class_names,probs[0])))
        
        
        
        