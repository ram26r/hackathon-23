import requests

def send_authenticated_request(url, access_token, method='GET', headers=None, data=None):
    headers = headers or {}
    headers['Authorization'] = f'Bearer {access_token}'

    response = requests.request(method, url, headers=headers, data=data)

    return response

# Example usage
url = 'https://gitlab.dx1.lseg.com/api/v4/projects'  # Replace with your desired URL
access_token = 'sdp-3yqMtjss-sC61L1fT8RB'  # Replace with your access token

response = send_authenticated_request(url, access_token)

# Print the response status code and content
print(f"Status code: {response.status_code}")
print(f"Response content: {response.text}")
