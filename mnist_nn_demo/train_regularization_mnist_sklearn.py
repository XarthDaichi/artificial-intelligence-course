import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

# Load the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess the data
x_train_flat = x_train.reshape(x_train.shape[0], -1)
x_test_flat = x_test.reshape(x_test.shape[0], -1)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train_flat)
x_test_scaled = scaler.transform(x_test_flat)

# Split the training data into training and validation sets
x_train_split, x_val_split, y_train_split, y_val_split = train_test_split(
    x_train_scaled, y_train, test_size=0.2, random_state=42)

# Define parameter grid for GridSearchCV
param_grid = {
    'alpha': [0.001, 0.01, 0.1, 1.0, 10.0],  # Regularization strength
}

# Define the models
ridge_model = Ridge()
lasso_model = Lasso()

# Perform grid search with cross-validation for Ridge
ridge_grid_search = GridSearchCV(ridge_model, param_grid, cv=5, scoring='neg_mean_squared_error')
ridge_grid_search.fit(x_train_split, y_train_split)

# Perform grid search with cross-validation for Lasso
lasso_grid_search = GridSearchCV(lasso_model, param_grid, cv=5, scoring='neg_mean_squared_error')
lasso_grid_search.fit(x_train_split, y_train_split)

# Get the best models and their parameters
best_ridge_model = ridge_grid_search.best_estimator_
best_ridge_params = ridge_grid_search.best_params_
ridge_val_score = best_ridge_model.score(x_val_split, y_val_split)

best_lasso_model = lasso_grid_search.best_estimator_
best_lasso_params = lasso_grid_search.best_params_
lasso_val_score = best_lasso_model.score(x_val_split, y_val_split)

print(f"*** Best Ridge parameters: {best_ridge_params} ***")
print(f"*** Ridge validation score: {ridge_val_score} ***")

print(f"*** Best Lasso (L1) parameters: {best_lasso_params} ***")
print(f"***Lasso (L1) validation score: {lasso_val_score} ***")

