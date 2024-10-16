import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


from sklearn.datasets import load_iris

def train_tree(random_state = 666, 
               max_depth = 2, 
               criterion = 'entropy'):

    iris = load_iris()

    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

    print(f"*** Iris data set read. Shape: {df.shape} ****")
    print(df.head())

    df['target'] = iris.target

    X_train, X_test, y_train, y_test = train_test_split(df[iris.feature_names], 
                                                        df['target'], 
                                                        random_state = random_state)

    dt = DecisionTreeClassifier(max_depth=max_depth, 
                                random_state = random_state, 
                                criterion = 'entropy')
                                
    dt.fit(X_train.values, y_train) # .values is to avoid warning when predicting probs
    
    
    return dt, (df, iris.target_names, X_test, y_test)
                   
                   