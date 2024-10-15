import requests

# Read the tokens from token.txt file
def read_tokens(file_path):
    with open(file_path, 'r') as file:
        tokens = file.readlines()
    # Remove any trailing whitespace (like newlines)
    tokens = [token.strip() for token in tokens]
    return tokens

# Define the URLs of the APIs
api_urls = [
    "https://task-api.infinitar.io/telegramGroupoidAward",
    "https://task-api.infinitar.io/userSignin",
    "https://task-api.infinitar.io/twitterAttentionAward"
]

# File path to the token.txt
token_file_path = "token.txt"

# Get the list of tokens from the file
tokens = read_tokens(token_file_path)

# Define the common headers (except authorization, which will vary per request)
headers_template = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-length": "0",
    "origin": "https://task-telegram.infinitar.com",
    "priority": "u=1, i",
    "referer": "https://task-telegram.infinitar.com/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\", \"Microsoft Edge WebView2\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

# Loop through each token
for token in tokens:
    # Update headers with the current token
    headers = headers_template.copy()
    headers["authorization"] = f"Bearer {token}"

    # Loop through each API URL and make the POST request
    for url in api_urls:
        try:
            response = requests.post(url, headers=headers)
            # Print the response from each request
            print("Join Telegram Grup. https://t.me/dasarpemulung")
            print(f"Response from {url} using token {token}: {response.status_code}, {response.json()}")
        except requests.exceptions.RequestException as e:
            print("Join Telegram Grup. https://t.me/dasarpemulung")
            print(f"Error with {url} using token {token}: {e}")
