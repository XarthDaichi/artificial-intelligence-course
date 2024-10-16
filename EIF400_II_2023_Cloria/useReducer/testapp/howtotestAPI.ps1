# Define the URL to which you want to send the POST request
$url = "https://example.com/api/endpoint"

# Define the JSON data you want to include in the request body (if applicable)
$body = @{
    key1 = "value1"
    key2 = "value2"
} | ConvertTo-Json

# Set headers if needed (e.g., for authentication)  
$headers = @{
    "Content-Type"  = "application/json"
}

# Send the POST request
$response = Invoke-RestMethod -Uri $url -Method Post -Headers $headers -Body $body

# Display the response (you can access specific properties depending on the API response)
$response

