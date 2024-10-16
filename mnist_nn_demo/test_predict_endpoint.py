import requests
import base64

# URL of the Flask server
url = 'http://localhost:5000/predict'

# Path to the image file you want to send
image_path = 'images/4_page_image.png' #'images/66_mnist_image.png' #drawing.png'

# Open the image file and read it in binary mode
with open(image_path, 'rb') as f:
    # Encode the image data as base64
    image_base64 = base64.b64encode(f.read()).decode('utf-8')

# Create a JSON payload containing the base64-encoded image data
payload = {'image': 'data:image/png;base64,' + image_base64}

# Send a POST request to the Flask server with the JSON payload
response = requests.post(url, json=payload)

# Print the response from the server
print(response)
print(response.json())
