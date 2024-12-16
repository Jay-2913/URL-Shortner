# URL-Shortner
This Python script uses the requests library to interact with the Cutt.lyAPI, providing a simple way to shorten URLs. By sending a request to the Cutt.lyAPI with the full URL and a custom link name, the script generates a shortened version of the provided URL.

Prerequisites
Before running the script, ensure you have the requests library installed. You can install it using pip:

bash
pip install requests
Usage
The script allows you to shorten URLs by providing the full URL and a desired custom link name. It sends a request to the Cutt.lyAPI and prints the response containing the shortened URL.

Features
API Integration: Uses the Cutt.lyAPI to shorten URLs.

Custom Link Names: Allows specifying a custom name for the shortened link.

JSON Response Handling: Processes and prints the JSON response from the API.

Example
Below is the full code of the script:

python
import requests

def shorten_link(full_link, link_name):
    API_KEY = '85325ee5d898de1cb360c311378f11f1e5c10'
    BASE_URL = 'https://cutt.ly/api/api.php'
    
    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    response = requests.get(BASE_URL, params=payload)
    data = response.json()
    
    print(data)

# Example usage
shorten_link('https://hianime.to/search?keyword=arcane+', 'codepalace123')
How It Works
Import the requests Library:

The script begins by importing the requests library, which is used to make HTTP requests.

Define the shorten_link Function:

This function takes two parameters: full_link (the original URL to be shortened) and link_name (the desired custom name for the shortened link).

It sets up the API key and the base URL for the Cutt.lyAPI.

Create the Payload:

The payload dictionary contains the API key, the full URL to be shortened, and the custom link name.

Send the Request:

The script sends a GET request to the Cutt.lyAPI with the payload parameters.

It then processes the response and converts it to JSON format.

Print the Response:

The script prints the JSON response, which includes information about the shortened URL.

Conclusion
This URL shortener script is a straightforward tool for converting long URLs into short, easy-to-share links using the Cutt.lyAPI. It allows for custom link naming and handles the API response in JSON format, making it a useful utility for various applications



Message Copilot
