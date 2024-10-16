class Stump(DecisionTree):
    pass


def tree_gradient_boosting(X,y, alpha, alpha_min):
    # r current residual
    r = y
    h = 0 # like a lambda x: 0
    for i in range(T):
        tree = Stump(h=1)
        ht = tree.fit(X, r)
        h += alpha * ht
        r = residual(X, y, h, loss) # loss=MSE if continuous (loss is lambda function)
        alpha = decay(alpha)
        if alpha < alpha_min:
            break
    return h

def decay(alpha, alpha_decay=0.9):
    return alpha * alpha_decay

def residual(X, y, h, loos):
    pass