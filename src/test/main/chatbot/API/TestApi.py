import subprocess

def send_curl_request(url, access_token=None):
    curl_command = ['curl', url]

    if access_token:
        curl_command.extend(['-H', f'Authorization: Bearer {access_token}'])

    result = subprocess.run(curl_command, capture_output=True, text=True)

    return result.stdout


# Example usage
url = 'https://gitlab.dx1.lseg.com/api/v4/projects/3544/repository/branches'  # Replace with your desired URL
access_token = 'sdp-3yqMtjss-sC61L1fT8RB'  # Replace with your access token

response = send_curl_request(url, access_token)
# Print the response
print(f"Response: {response}")
