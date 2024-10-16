import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values to be between 0 and 1
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

epochs = 5
model_filename = 'mnist_model.h5'
print(f"*** Training starts {epochs} ***")
model.fit(x_train, y_train, epochs=5)
print(f"*** Training ends {epochs} ***")

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'*** Accuracy on test ds:{test_acc} ***')

print(f"*** Model will be saved (format h5) at {model_filename} ***")
model.save(model_filename)
