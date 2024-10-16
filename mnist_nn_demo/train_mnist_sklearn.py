import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
#from sklearn.externals 
import joblib  # Import joblib for model persistence
import tensorflow as tf

print("*** Loading mnist data set ***")
# Load the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print("*** Loading mnist data set loaded ***")
print(f"*** x_train size {x_train.shape[0]} examples ***")

# Preprocess the data
x_train_flat = x_train.reshape(x_train.shape[0], -1)
x_test_flat = x_test.reshape(x_test.shape[0], -1)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train_flat)
x_test_scaled = scaler.transform(x_test_flat)

# Define and train the logistic regression model
logistic_model = LogisticRegression(max_iter=1000)
print("*** Training starts ***")
logistic_model.fit(x_train_scaled, y_train)
print("*** Training ends ***")

# Evaluate the model
train_accuracy = accuracy_score(y_train, logistic_model.predict(x_train_scaled))
test_accuracy = accuracy_score(y_test, logistic_model.predict(x_test_scaled))

print("Train accuracy:", train_accuracy)
print("Test accuracy:", test_accuracy)

# Save the trained model
model_filename = 'logistic_regression_model.pkl'
print(f"*** Saving model as {model_filename} ***")
joblib.dump(logistic_model, model_filename)
print(f"*** Model saved as {model_filename} ***")

# Load the saved model
print(f"*** LOading pkl model {model_filename} ***")
loaded_model = joblib.load('logistic_regression_model.pkl')

# Example of using the loaded model for prediction
print("*** Testing saved model ***")
example_index = 0
example_data = x_test_scaled[example_index].reshape(1, -1)  # Reshape for prediction
predicted_label = loaded_model.predict(example_data)[0]
probabilities = logistic_model.predict_proba(x_test_scaled)
probability_of_prediction = probabilities[0, predicted_label]
print(f"*** Predicted label for example number {example_index}: y={y_test[example_index]}: y_hat={predicted_label} prob={probability_of_prediction}")
