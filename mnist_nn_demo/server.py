from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_cors import cross_origin

import base64
from io import BytesIO
from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf

import os

app = Flask(__name__)
#CORS(app) 
CORS(app, resources={r"/predict": {"origins": "*"}})
# Load pre-trained MNIST model
# Downloaded from https://github.com/Shahnawax/HAR-CNN-Keras/blob/master/model.h5
model = tf.keras.models.load_model('mnist_model.h5') #('model.h5') #('mnist_model.h5')


def preprocess_image_v0(image_data):
    splitted_image = image_data.split(',')
    print("preprocess_image:", len(splitted_image))
    i = 0 if len(splitted_image) == 1 else 1
    # Decode base64 string and convert to RGBA image
    img = Image.open(BytesIO(base64.b64decode(image_data.split(',')[i])))
    
    # Convert RGBA image to grayscale
    img = img.convert('L')
    
    # Resize image to (90, 3)
    #img = img.resize((90, 3))
    img = img.resize((28, 28))
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Normalize pixel values
    img_array = img_array / 255.0
    
    # Reshape image for model input
    img_array = img_array.reshape(1, 28,28, 1) #(1, 90, 3, 1)
    
    return img_array
    
# Save the image to the specified directory
def save_image(img, suffix='', save_directory='./images'):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    filename = f'the_image{suffix}.png' #f'image_{uuid.uuid4().hex}.png'  # Generate a unique filename
    img.save(os.path.join(save_directory, filename))
    
def preprocess_image(image_data):
    # Expected format: can be like data:image/png;base64,<base64-encoded-data>
    print(f"Preprocessing image of size {len(image_data)}")
    splitted_image = image_data.split(',')
    
    if len(splitted_image) > 1:
        print(f"Header is: {splitted_image[0]} ")
        img_data = splitted_image[1]
    else:
        print('Image has no header')
        img_data = splitted_image[0]  # Use the whole string if no comma is present

    # Decode base64 string and convert to RGBA image
    img = Image.open(BytesIO(base64.b64decode(img_data)))

    ##################### Just Debugging purposes code #################
    # Convert RGBA image to grayscale
    save_image(img, suffix='_original')
    img_L = img.convert('L')
    save_image(img_L, suffix='_grayscale')

    img_inverted = ImageOps.invert(img_L)
    save_image(img_inverted, suffix='_grayscale_inverted')

    # Create a new RGBA image with white background
    img_white_bg = Image.new("L", img_L.size, "grey")
    
    # Composite the grayscale image onto the white background
    img_white_bg.paste(img_L, (0, 0), img)
    save_image(img_white_bg, suffix='_white')
    
    img_1 = img_white_bg.convert('1')
    save_image(img_1, suffix='_final')
    ####################################################
    img_L = img.convert('L')
    # Resize image to (28, 28) for MNIST model
    img = img_L.resize((28, 28))
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Normalize pixel values
    img_array = img_array / 255.0
    
    # Reshape image for model input
    img_array = img_array.reshape(1, 28, 28, 1)
    
    return img_array


@app.route('/predict', methods=['POST'])
@cross_origin()  # Allow all origins for this route
def predict():
    image_data = request.json['image']
    img_array = preprocess_image(image_data)
    # Make prediction using pre-trained model
    prediction = model.predict(img_array)
    print("Predictions array:", prediction.shape)
    digit = int(np.argmax(prediction))
    for d, pd in enumerate(prediction[0]):
        print(f"{d} --> {round(pd, 5)} {'*' if d == digit else ''}")
    # Return prediction result
    
    return jsonify({'prediction': digit, 'probability':str(prediction[0][digit])})

if __name__ == '__main__':
    app.run(debug=True)
