##################################################
"""
Ejercicio integrado

Entienda y Describa lo que hacen todas las funciones y código que así lo piden
en su docstring

Implemente la función que así se lo pide en su doctring

"""
import numpy as np

def some_utility(X):
    """ Describe what I do """
    return X[:, np.newaxis]

def main_utility(X):
    """ Describe what I do """
    c =  some_utility(np.ones(X.shape[0]))
    return np.hstack([c, X], dtype=X.dtype)

# Example of use
X = np.array([
   [1,2,3],
   [4,5, 6],
   [7, 8, 9]
], dtype="float") 

print("#"*80)
print(X)
print(main_utility(X))

##################################################

import numpy as np
from sklearn.linear_model import LinearRegression
np.random.seed(42)


def lr_setup(m = 100, n = 2, w= (5, 6, 3) ):
    """ Describe what I do """
    X = np.array([np.random.rand(1, n) for _ in range(m)]).reshape(m, n)
    w0, w1, w2 = w
    W = some_utility(np.array([w0, w1, w2]))
    y = main_utility(X) @ W 
    return X, y, W

def lr_train(X, y):
    """ Describe what I do """
    lr = LinearRegression()
    lr.fit(X, y)
    return {"model":lr, "weights": lr_get_weigths(lr)}

def lr_get_weigths(lr):
    """ Describe what I do """
    return (lr.intercept_[0], *lr.coef_[0])
    
def lr_predict_with(model, x, W):
    """ Describe what I do """
    w0_hat, w1_hat, w2_hat = model["weights"]
    W_hat = np.array(model["weights"])
    fixed_x = main_utility(x)
    return {
            'y_hat': (fixed_x @ W_hat)[0], 
            'y': (fixed_x @ W)[0][0]
           }
           
def ls_mse_error(model, X, y):
    """ 
       model: dict as above with the model and the W
       X: Some examples matrix
       y: some corresponding targets vector 
       returns: the MSE error of model on X, y
       You must implement me and test me 
    """
    raise NotImplementedError
#######################################################
if __name__ == "__main__":  
    """ Describe what I do """
    print("#"*80)
    print("\n*** Running Program ***\n")
    X, y, W = lr_setup()
    print(">>> Running Step 1 ")
    model = lr_train(X, y)
    print(">>> Running Step 2 ")
    x = np.array([[2.5, 3.7]])
    print(f">>> {x} --> {lr_predict_with(model, x, W)}")
    print("\n*** end ***")
    
    # Uncomment when implemented
    #print(f"{ls_mse_error(model, y)=:}")